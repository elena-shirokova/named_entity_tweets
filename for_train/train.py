#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymorphy2
from modules import *
from featureExtractor import FeatureExtractor

filePath = '/Users/lena/Downloads/tweets.json'
read = ReadFile(filePath)
all_tweets = read.openFile(filePath) #all tweets are stored here
tweets_for_analyze1 = read.read_tweets(all_tweets)
#rint tweets_for_analyze
features = MorphFeatures
tweets = [features.split_string(features.remove_punctuation(tweets_for_analyze1[t])) for t in tweets_for_analyze1]
tweets_with_features_train = features.morph_parse(tweets)


#print tweets_with_features
categories = ["not obj","obj"]

extract_features_train = features.features(tweets_with_features_train)
labels = features.labels(extract_features_train)


#print extract_features[0:2], labels[0:2]

training_set = extract_features_train[0:12172]
#print len(extract_features)
target = labels[0:12172]
lab = [0]

test_set = [{'word':u'иск','pos':'NOUN','case':'nomn'},{'word':u'удовлетворили','pos':'VERB','case':'none'},{'word':u'полностью','pos':'ADVB','case':'none'},{'word':u'юристу','pos':'NOUN','case':'datv'}]
label_test = [1,0,0,0]
vec = DictVectorizer(sparse=True)
#cross - validation in production

train = vec.fit_transform(training_set).toarray()
clf = MultinomialNB()
clf = clf.fit(train, target)


test = vec.transform(test_set).toarray()

pred_proba = clf.predict_proba(test)

pred = clf.predict(test)

print  metrics.csore(test,label_test)



