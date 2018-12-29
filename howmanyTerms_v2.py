# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:32:29 2018

@author: dewan
"""

#steps = [0, 10000]
docs_step = range(0, 650000, 10000)
#docs_xml = ["total-"+str(x)+".xml" for x in docs_step]
#docs_keys = ["total-"+str(x)+".keys" for x in docs_step]



import sys
import pandas as pd
from bs4 import BeautifulSoup as Soup


labels = [] # dictionary of labels. each of the element contains list of labels for the step model.

#first pass is to construct the topwords vocabulary from the topwords of each topics,
#this is done faster from the smaller .keys file in the case of MALLET
for s in steps:
    doc_keys = "total-"+str(s)+".keys"
    dictionary = [] # list of all words in all topic models
    df = pd.read_csv(doc_keys,sep='\t',header=None)
    labels.append   # create list to contain labels for each Model
    for index, row in df.iterrows():
        label = row[1].lower()
        if label not in labels:
            labels.append(label)
print "numlabels:" + str(len(labels))
