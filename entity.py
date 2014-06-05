#!/usr/bin/env python
# -*- coding: utf8 -*-

import json
import pymorphy2
import nltk
import re
from collections import defaultdict
import sqlite3
morph = pymorphy2.MorphAnalyzer()
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.naive_bayes import BernoulliNB


def remove_punctuation(msg):
    punctuation = ['(', ')', '?', ':', ';', '!', '/', '"', "'","#",'*','^','_','.',',']
    for i in punctuation:
        msg = msg.replace(i," ")
    return msg

def split_string(msg):
    tokenize_msg = msg.split()
    return tokenize_msg

tweets_tokenized = defaultdict(list)

tweets = [split_string(remove_punctuation(tweets[t])) for t in tweets]

features_morph = defaultdict(list)
case_morph = defaultdict(list)





#print len(tweets_with_features1)
target = []
extract_features = []
id = 1
for sentence in tweets_with_features:
    for (w,pos,cas) in sentence:
        if ((w,pos) == (w,"NOUN") or (w,pos) == (w,'NPRO')) and (w,cas) == (w,'nomn'):
            #extract_features.append({'word':w,'pos':pos,'case':cas})
            target.append(1)
        elif not((w,pos) == (w,"NOUN") or (w,pos) == (w,'NPRO') and (w,cas) == (w,'nomn')) :
            target.append(0)



X_train = extract_features[0:10]

vec = DictVectorizer()

Y_train = vec.fit_transform(X_train).toarray()

#print vec.get_feature_names()


label = target[0:10]
#X_test = [{'word':u'кошка','pos':'NOUN','case':'nomn'}]

#X_test = vec.fit_transform(test_set).toarray()
#{'word':u'кошка','pos':'NOUN','case':'nomn'},

#
#clf = clf.fit(Y_train, label)

#test = vec.transform(X_test).toarray()

#result = clf.predict_proba(test)

#metrics = clf.score(Y_train,label)

#print(result)

#print(metrics)

#print clf.predict(test)


#crossvalidation

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X_train, label, test_size=0.4, random_state=0)

#print X_train.shape, y_train.shape

#print X_test.shape, y_test

X = np.array(X_train)
Y = np.array(y_train)
clf = BernoulliNB().fit(X_train, y_train)

























