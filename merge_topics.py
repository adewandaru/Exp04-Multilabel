# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 06:06:23 2018

@author: dewan
"""
steps = [0, 10000]
#docs_step = range(0, 650000, 10000)
#docs_xml = ["total-"+str(x)+".xml" for x in docs_step]
#docs_keys = ["total-"+str(x)+".keys" for x in docs_step]



import sys
import pandas as pd
from bs4 import BeautifulSoup as Soup


labels = {} # dictionary of labels. each of the element contains list of labels for the step model.

#first pass is to construct the topwords vocabulary from the topwords of each topics,
#this is done faster from the smaller .keys file in the case of MALLET
for s in steps:
    doc_keys = "total-"+str(s)+".keys"
    dictionary = [] # list of all words in all topic models
    df = pd.read_csv(doc_keys,sep='\t',header=None)
    labels[s] = {}   # create list to contain labels for each Model
    for index, row in df.iterrows():
        words = row[3].split(" ")
        labels[s][row[0]]=row[1].lower()  # store the label for this topic id of this step
        for w in words:
            if w not in dictionary:
                dictionary.append(w)

# construct dataframes with specific columns.
mm = pd.DataFrame({'header': dictionary.sort()}, index=[0])

# second pass is to fill them up
for s in steps:
    docs_xml = "total-"+str(s)+".xml"   # the diagnostic filename for this step
    handler = open(docs_xml).read()
    soup = Soup(handler)
    topics = soup.find_all('topic')
    topics_list = []
    for t in topics:
        words = t.find_all('word')
        tokens = t['tokens'] 
        topic_id = int(t['id'])
        words_dict = {}
        words_dict['TOKENS'] = float(tokens)
        words_dict['ACTIVE'] = True
        
        if topic_id in labels[s]:
            words_dict['LABEL'] = labels[s][topic_id]  # the label for this topic
            for w in words:
                words_dict[w.text] = float(w['prob'])
            topics_list.append(words_dict)
            
    mm = mm.append(topics_list, ignore_index = True)

#sort
mm.sort_values("LABEL", inplace=True)
      
def merge (t1, t2):
    global mm
    '''
    for t1,t2 index duplicates of the label, do the merge:
    '''
    s1 = mm.loc[t1]
    s2 = mm.loc[t2]
    s3 = s1.add(s2, fill_value=0)
    s3['LABEL'] = s1['LABEL']
    mm = mm.append(s3, ignore_index=True)
    
    #mark original rows as dropped
    mm.at[t2, 'ACTIVE'] = False
    mm.at[t1, 'ACTIVE'] = False
    #s1.drop(t1, t2)
    
                
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