import os
import time
import json
from Constants import Parameters
from pymongo import MongoClient

reviews_collection = MongoClient("mongodb://localhost:27017/")["Dataset_Challenge_Reviews"]["Reviews"]

business_collection = MongoClient("mongodb://localhost:27017/")["Dataset_Challenge_Reviews"]["Business2"]

with open(Parameters.DATASET_FILE +'yelp_academic_dataset_business.json') as dataset:
    for line in dataset:
        data = json.loads(line)
        if 'Restaurants' in data["categories"] and data['city'] == 'Phoenix':
           business_collection.insert({
             "_id": data["business_id"],
             "lat": data['latitude'],
             "lon":data['longitude'],
             "name":data['name']
           })
