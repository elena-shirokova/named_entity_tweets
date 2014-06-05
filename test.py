#!/usr/bin/env python
# -*- encoding: utf8 -*-

from modules import *
tweet = dict()
tweet[0] = u'Иск удовлетворили полностью!!'
    #Рада сообщить,что мой прекрасный юрист Мария Князева в очередной раз выиграла дело против Яуза-пресс!
#              u'как выгнать ляскина из новокосино? достал уже')


features1 = MorphFeatures
tweets1 = [features1.split_string(features1.remove_punctuation(tweet[t])) for t in tweet]
tweets_with_features_test = features1.morph_parse(tweets1)
print tweets_with_features_test
global extract_features_test
extract_features_test = features1.features(tweets_with_features_test)





