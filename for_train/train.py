#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymorphy2
from modules import *
from featureExtractor import FeatureExtractor
from sklearn import metrics

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

extract_features_train = features.features(tweets_with_features_train[0:22])
labels = features.labels(extract_features_train[0:22])

training_set = extract_features_train[0:22]
#print len(extract_features)
target = labels[0:22]
lab = [0]

label_test = [1,0,0,0]
vec = DictVectorizer(sparse=True)
#cross - validation in production

train = vec.fit_transform(training_set).toarray()
clf = MultinomialNB()
clf = clf.fit(train, target)

tweet = dict()
tweet[0] = u'мой прекрасный юрист выиграла в суде!'

features1 = MorphFeatures
tweets1 = [features1.split_string(features1.remove_punctuation(tweet[t])) for t in tweet]


for i in range(0,len(tweets1)):

    tweets1[i] = [(word.lower(),morph.parse(word)[0].tag.POS,morph.parse(word)[0].tag.case) for word in tweets1[i] if morph.parse(word)]

#print tweets1

extract_features_test = features1.features_test(tweets1)


#print extract_features_test

test = vec.transform(extract_features_test).toarray()

pred_proba = clf.predict_proba(test)

pred = clf.predict(test)

print pred_proba

for word in extract_features_test:
    print word.get('word')
print "result:", pred

