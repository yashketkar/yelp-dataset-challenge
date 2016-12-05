from Constants import Parameters
from pymongo import MongoClient
import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
import gensim
from gensim import corpora
from gensim.corpora import BleiCorpus

corpus_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][Parameters.CORPUS_COLLECTION]
corpus_cursor = corpus_collection.find()
mycorpus_cursor = corpus_collection.find()

print corpus_cursor.count()

dictionary = corpora.Dictionary(review['words'] for review in corpus_cursor)
dictionary.filter_extremes(keep_n=10000)
dictionary.compactify()
corpora.Dictionary.save(dictionary,Parameters.Dictionary_path)
ncorpus =[]
i=0
for review in mycorpus_cursor:
    print i
    i+=1
    ncorpus.append(dictionary.doc2bow(review["words"]))
corpora.BleiCorpus.serialize(Parameters.Corpus_path,ncorpus)
dcorpus = corpora.BleiCorpus(Parameters.Corpus_path)
lda = gensim.models.LdaModel(dcorpus, num_topics=Parameters.Lda_num_topics, id2word=dictionary)
lda.save(Parameters.Lda_model_path)
i=0
for topic in lda.show_topics(num_topics=Parameters.Lda_num_topics):
    print '#' + str(i) + ': ' + str(topic)
    i += 1
