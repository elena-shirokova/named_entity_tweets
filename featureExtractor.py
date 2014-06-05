#!/usr/bin/env python
# -*- coding: utf8 -*-

class FeatureExtractor:

    def __init__(self,msg):
        self.msg = msg

    @staticmethod
    def trainFeatureExtractor(msg,vec):
        train = vec.fit_transform(msg).toarray()
        return train

    @staticmethod
    def testFeatureExtractor(msg,vec):
        return vec.transform(msg).toarray()


    @staticmethod
    def fitData(clf,msg,label):
        return clf.fit(msg,label)


