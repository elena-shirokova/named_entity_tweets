#!/usr/bin/env python
# -*- coding: utf8 -*-
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

word  = u'Мария'

print morph.parse(word)[0].tag

    #Иск удовлетворили полностью!!
#              u'как выгнать ляскина из новокосино? достал уже')
#Рада сообщить,что мой прекрасный юрист Мария Князева в очередной раз выиграла дело против Яуза-пресс!