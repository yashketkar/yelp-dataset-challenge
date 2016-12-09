# yelp-dataset-challenge
ILS - Z534 Yelp Dataset Challenge

## Group 4 Team Members:
* [Dhvani Deven Kotak](https://github.com/dhvanikotak) (dkotak@indiana.edu)  
* [Manikandan Murugesan](https://github.com/manikandan5) (murugesm@indiana.edu)  
* [Rohit Dandona](https://github.com/rohitdandona) (rdandona@indiana.edu)  
* [Vikrant Kaushal](https://github.com/KaushalVikrant) (vkaushal@indiana.edu)  
* [Yash Sumant Ketkar](https://github.com/yashketkar) (yketkar@indiana.edu)  

Task 2

Configuration used for executing scripts and deploying the application:
Python Version - 2.7.12
MongoDB Version - 3.4

Installation
------------
Dependencies
- Download and extract the source files and yelp dataset.
- Run `pip install pymongo`
- Run `pip install nltk`
- Run `import nltk` and `nltk.download()` in a python shell
- Run `pip install gensim`
- Run `pip install bottle`

Order to run the files and use.
- python CorpusLoader.py
	- Populates the reviews for Phoenix from the dataset json where type of business equals to the restaurant
	- Makes Reviews more simplified for Online Analysis

- python TopicModelling.py
	- Gensim python library creates a LDA model for different reviews.

- python DisplayTopics.py
	- Displays the six major topics and the sub-topics with maximum weightages Respectively
	- All 60 topics were categorised so as to highlight the sub-topic they represent
	- The 60 subtopics highlighted in _topics.txt_

- python getBusinessRating.py
 - Create Ratings Collection in MongoDB

- python SaveBusinessInfo.py
 - Create Business Info Collection in MongoDB

- python getFreqBusinessTopic.py
 - Business Frequency Topic is plotted by data generated

- python ShowTopicsForReview.py
 - Displays the topics for review.

- iPython Google_Maps_Heat_Map.ipynb
 - Displays a heatmap of restaurants based on topic
