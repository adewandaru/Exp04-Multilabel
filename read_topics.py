# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 06:06:23 2018

@author: dewan
"""
docs_step = [0]
#docs_step = range(10000, 650000, 10000)
docs_xml = ["total-"+str(x)+".xml" for x in docs_step]
docs_keys = ["total-"+str(x)+".keys" for x in docs_step]



import sys
import pandas as pd
from bs4 import BeautifulSoup as Soup


labels = []

#first pass is to construct the topwords vocabulary from the topwords of each topics,
#this is done faster from the smaller .keys file in the case of MALLET
for d in docs_keys:
    dictionary = []
    df = pd.read_csv(d,sep='\t',header=None)
    for index, row in df.iterrows():
        words = row[3].split(" ")
        labels.append( row[1] )
        for w in words:
            if w not in dictionary:
                dictionary.append(w)

# construct dataframes with specific columns.
mm = pd.DataFrame({'header': dictionary.sort()}, index=[0])

i = 0
# second pass is to fill them up
for d in docs_xml:
    handler = open(d).read()
    soup = Soup(handler)
    topics = soup.find_all('topic')
    topics_list = []
    for t in topics:
        words = t.find_all('word')
        tokens = t['tokens']
        words_dict = {}
        words_dict['TOKENS'] = tokens
        words_dict['LABEL'] = labels [i]
        for w in words:
            #print w['prob']
            #print w.text
            words_dict[w.text] = float(w['prob'])
        #topic_row = pd.DataFrame(words_dict, index=[0])
        topics_list.append(words_dict)
    mm = mm.append(topics_list)
    i = i + 1    
            
            
            
    #df = pd.read_csv(docs_keys[i],sep='\t',header=None)
    #i = i + 1
    
    '''
    Merged Matrix
        awan    banjir    cerita    delima  eropa
        --------------------------------------------
    T1  w1      w2        w3        w4      w5 ... 
    T2  ..
    T3  ..
    
    '''
#third step to merge