#!/usr/bin/env python
# -*- coding: utf8 -*-

import json
from collections import defaultdict
tweets = defaultdict(list)

class ReadFile:

    def __init__(self,filePath):
        self.filePath = filePath

    def openFile(self,filePath):
        file = open(self.filePath, 'r')
        with open(self.filePath) as json_file:
            json_data = json.load(json_file)
        return json_data

    def object_count(json_data):
        n = 0
        for tweet in json_data:
            n = n + 1
        return n

    @staticmethod
    def read_tweets(json_data):
        for i in range(0,len(json_data)):
            if json_data[i]['polarity'] == 'negative':
                tweets[i] = json_data[i]['text']
            elif json_data[i]['polarity'] == 'positive':
                tweets[i] = json_data[i]['text']
        return tweets



