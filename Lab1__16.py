#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import re

line=""

while (True):
    try:
        x = str(raw_input(u"Введите имя текстового файла:\n"))
        with codecs.open(x, encoding='utf-8') as fin:
            while (True):
                try:
                    l = next(fin)
                    line+=l.strip()
                except:
                    break
    except:
        print u"Ошибка!\n"
    else:
        break

letters = {}

for litera in line:
    counter = letters.get(litera,0)
    counter += 1
    if (len(re.findall(ur'[A-Za-zА-Яа-я]', litera))!=0):
        letters[litera] = counter

s1=sorted(letters.items(), key=lambda (k, v): v, reverse=True)
s2=u''.join(str(e) for e in s1).replace('\u','\\u').decode('unicode-escape')
s3=re.findall(ur'[A-Za-zА-Яа-я]', s2)

print (''.join(e for e in s3))[1::2]
