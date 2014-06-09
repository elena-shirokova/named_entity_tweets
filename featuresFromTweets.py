__author__ = 'lena'

import pymorphy2
import nltk
import re
from collections import defaultdict
morph = pymorphy2.MorphAnalyzer()
import ast

tweets_tokenized = defaultdict(list)
tweets_with_features = []
target = []
extract_features = []

class MorphFeatures:
    tweets = defaultdict(list)
    def __init__(self,msg):
        self.msg = msg

    @staticmethod
    def remove_punctuation(msg):
        punctuation = ['(', ')', '?', ':', ';', '!', '/', '"', "'","#",'*','^','_','.',',']
        for i in punctuation:
            msg = msg.replace(i," ")
        return msg

    @staticmethod
    def split_string(msg):
        tokenize_msg = msg.split()
        return tokenize_msg

    @staticmethod
    def morph_parse(tokenized):
        for i in range(0,len(tokenized)):
           tokenized[i] = [(word.lower(),morph.parse(word)[0].tag.POS,morph.parse(word)[0].tag.case) for word in tokenized[i] if morph.parse(word)]

        return tokenized

    @staticmethod
    def features(tweets_with_features):
        for i in range(0,len(tweets_with_features)):
            for (w,pos,cas) in tweets_with_features[i]:
                if (pos == "NOUN" or pos == 'NPRO'):
                    tweets_with_features[i] = dict({'word':w,'pos':pos,'case':cas})
        return tweets_with_features

    @staticmethod
    def labels(extract_features):
        for sentence in extract_features:
                if (sentence.get('case') == u'nomn'):
                    target.append(1)
                else:
                    target.append(0)
        return target

    @staticmethod
    def features_test(tweets_with_features):
        for i in range(0,len(tweets_with_features)):
            for (w,pos,cas) in tweets_with_features[i]:
                if (w,pos,cas) == (w,"NOUN",'nomn'):
                    tweets_with_features[i] = dict({'word':w,'pos':pos,'case':cas})
        return tweets_with_features




