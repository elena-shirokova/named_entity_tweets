#!/usr/bin/env python
# -*- encoding: utf8 -*-

from modules import *
tweet = dict()
tweet[0] = u'Иск удовлетворили полностью!!'
    #Рада сообщить,что мой прекрасный юрист Мария Князева в очередной раз выиграла дело против Яуза-пресс!
#              u'как выгнать ляскина из новокосино? достал уже')


features1 = MorphFeatures
tweets1 = [features1.split_string(features1.remove_punctuation(tweet[t])) for t in tweet]


for i in range(0,len(tweets1)):

    tweets1[i] = [(word.lower(),morph.parse(word)[0].tag.POS,morph.parse(word)[0].tag.case) for word in tweets1[i] if morph.parse(word)]

print tweets1





