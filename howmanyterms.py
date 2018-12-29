# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:32:29 2018

@author: dewan
"""

#steps = [0, 10000]
doc_steps = range(0, 650000, 10000)
#doc_steps = [0]
#docs_xml = ["total-"+str(x)+".xml" for x in docs_step]
#docs_keys = ["total-"+str(x)+".keys" for x in docs_step]



import sys
import pandas as pd
from bs4 import BeautifulSoup as Soup


labels = [] # dictionary of labels. each of the element contains list of labels for the step model.
words = {}
#first pass is to construct the topwords vocabulary from the topwords of each topics,
#this is done faster from the smaller .keys file in the case of MALLET
for s in doc_steps:
    doc_csv = "total-"+str(s)+".csv"
    df = pd.read_csv(doc_csv,sep='\t',header=None)
    for index, row in df.iterrows():
        try:
            lines = row[2].lower().split()
            for w in lines:
                if w not in words:
                    words[w]=1
        except:
            continue
        #print len(words)
print "numwords:" + str(len(words))
