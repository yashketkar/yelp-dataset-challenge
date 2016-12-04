import os
import time
import json
import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from pymongo import MongoClient

class Parameters:
    def __init__(self):
        pass
    DATASET_FILE = '../yelp_dataset_challenge_academic_dataset/'
    MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
    REVIEWS_DATABASE = "Dataset_Challenge_Reviews"
    REVIEWS_COLLECTION = "Reviews"
    BUSINESS_COLLECTION = 'Business'
    TOPIC_RATING_COLLECTION ='TopicRating'
    CORPUS_COLLECTION = "Corpus"
    BUSINESS_INFO_COLLECTION ="BusinessInfo"

    Dictionary_path = "DataModels/dictionary.dict"
    Corpus_path = "DataModels/corpus.mm"
    Lda_num_topics = 60
    Lda_model_path = "DataModels/lda_model_topics.lda"

reviews_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][Parameters.REVIEWS_COLLECTION]
business_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][Parameters.BUSINESS_COLLECTION]
corpus_collection = MongoClient(Parameters.MONGO_CONNECTION_STRING)[Parameters.REVIEWS_DATABASE][Parameters.CORPUS_COLLECTION]

stopset = set(stopwords.words('english'))
stopwords = {}
with open('stopwords.txt', 'rU') as f:
    for line in f:
        stopwords[line.strip()] = 1
# print stopwords
lmtzr = WordNetLemmatizer()

with open(Parameters.DATASET_FILE +'yelp_academic_dataset_business.json') as dataset:
    for line in dataset:

            data = json.loads(line)

            if 'Restaurants' in data["categories"] and data['city'] == 'Phoenix':
               business_collection.insert({
                 "_id": data["business_id"]
               })

n=0
with open(Parameters.DATASET_FILE +'yelp_academic_dataset_review.json') as dataset:
    for line in dataset:
        data = json.loads(line)
        isRestaurant = business_collection.find({"_id": data["business_id"]}).count();
        n+=1
        print n
        if data["type"] == "review" and isRestaurant !=0:
            reviews_collection.insert({
            "reviewId": data["review_id"],
            "business": data["business_id"],
            "text": data["text"],
            "stars": data['stars'],
            "votes":data["votes"]
            })
            words = []
            sentences = nltk.sent_tokenize(data["text"].lower())
            for sentence in sentences:
                tokens = nltk.word_tokenize(sentence)
                filteredWords = [word for word in tokens if word not in stopwords]
                tagged_text = nltk.pos_tag(filteredWords)
                for word, tag in tagged_text:
                    if tag in ['NN','NNS'] :
                        words.append(lmtzr.lemmatize(word))
            corpus_collection.insert({
                  "reviewId": data["reviewId"],
                  "business": data["business"],
                  "stars": data['stars'],
                  "votes":data["votes"],
                  "text": data["text"],
                  "words": words
            })
