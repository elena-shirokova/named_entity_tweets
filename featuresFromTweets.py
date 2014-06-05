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
        for sentence in tokenized:
           sentence = [(word.lower(),morph.parse(word)[0].tag.POS,morph.parse(word)[0].tag.case) for word in sentence if morph.parse(word)]
           tweets_with_features.append(sentence)
        return tweets_with_features

    @staticmethod
    def features(tweets_with_features):
        for sentence in tweets_with_features:
            for (w,pos,cas) in sentence:
                if ((w,pos) == (w,"NOUN") or (w,pos) == (w,'NPRO')):
                    extract_features.append(dict({'word':w,'pos':pos,'case':cas}))
        return extract_features

    @staticmethod
    def labels(extract_features):
        for item in extract_features:
                if (item['case']== u'nomn'):
                    target.append(1)
                else:
                    target.append(0)
        return target





