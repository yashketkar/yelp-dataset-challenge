from pymongo import MongoClient
from gensim.models import LdaModel
from gensim import corpora
from Constants import Parameters
import json
from collections import Counter,defaultdict

dictionary = corpora.Dictionary.load(Parameters.Dictionary_path)
corpus = corpora.BleiCorpus(Parameters.Corpus_path)
lda = LdaModel.load(Parameters.Lda_model_path)

business_collection = MongoClient("mongodb://localhost:27017/")["Dataset_Challenge_Reviews"]["Business"]
corpus_collection = MongoClient("mongodb://localhost:27017/")["Dataset_Challenge_Reviews"]["Corpus"]
rating_collection = MongoClient("mongodb://localhost:27017/")["Dataset_Challenge_Reviews"]["TopicRating"]

i=0
business_cursor = business_collection.find()
corpus_cursor = corpus_collection.find()

for i in range(business_cursor.count()):
        try :
             business =business_cursor.__getitem__(i)
        except Exception:
             print 'Exceptions..!!!!!!'
             continue
        prob_count =Counter()
        count =Counter()
        score_count =Counter()
        corpus_cursor =corpus_collection.find({"business": business["_id"]})
        for corpus in corpus_cursor:
            print 'My Rating******'
            topics =  lda[dictionary.doc2bow(corpus["words"])]
            for topic,prob in topics:
                prob_count[topic]+=prob
                score_count[topic]+=corpus["stars"]
                count[topic]+=1
           #     print topic , prob

        avg =defaultdict()
        fcount = defaultdict()
        for topics in score_count.keys():
            avg[topics]= 1.0*score_count[topics]/count[topics]
            fcount[topics] = count[topics]

        rating_collection.insert({
              "business": business["_id"],
              "ratings": json.loads(json.dumps(avg,ensure_ascii=False)),
              "counts":json.loads(json.dumps(fcount,ensure_ascii=False)),

        })
        print avg
