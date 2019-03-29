#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 23:49:32 2019

@author: tinahuang
"""

import nltk
import urllib.request

#load data from wikipedia related to SpaceX
response=urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()
print(html)

#Clean webpage texts of HTML tags
from bs4 import BeautifulSoup#pull out data from HTML and XML files
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
print(text)

#Tokenize
tokens = [t for t in text.split()]
print(tokens)

#Count word frequency
from nltk.corpus import stopwords
sr= stopwords.words('english')
clean_tokens = tokens[:]
for text in tokens:
    if text in stopwords.words('english'):
        clean_tokens.remove(text)
        
freq = nltk.FreqDist(clean_tokens)
freq

for key,val in freq.items():
    print(str(key) + ':' + str(val))
    
freq.plot(20, cumulative=False)