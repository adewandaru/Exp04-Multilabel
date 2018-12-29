# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 06:06:23 2018

@author: dewan
"""
#steps = [0, 10000]
steps = range(0, 650000, 10000)
steps.remove(450000)
steps.remove(470000)
steps.remove(550000)
steps.remove(560000)
steps.remove(570000)
steps.remove(580000)
steps.remove(590000)

#docs_xml = ["total-"+str(x)+".xml" for x in docs_step]
#docs_keys = ["total-"+str(x)+".keys" for x in docs_step]



import sys
import pandas as pd
from bs4 import BeautifulSoup as Soup

def merge (a, b):
    ''' merge two dictionaries, each is bag of word of topic '''
    t1 = a['TOKENS']
    t2 = b['TOKENS']
    keys = []
    c = {}
    
    for w in a:
        if w not in keys:
            keys.append(w)
    for w in b:
        if w not in keys:
            keys.append(w)
    keys.remove('TOKENS') # not gonna use this.
    keys.remove('LABEL')
    for w in keys:
        if w in a and w in b:            
            c[w] = ( a[w] * t1 + b[w] * t2 ) / ( t1 + t2 )
        elif w in a:
            c[w] = a[w] * t1 / (t1 + t2)
        else:  # w in b
            c[w] = b[w] * t2 / (t1 + t2)
            
    c['TOKENS'] = t1 + t2
    c['LABEL'] = a['LABEL']
    return c
    #df = pd.read_csv(docs_keys[i],sep='\t',header=None)
    #i = i + 1

labels = {} # dictionary of labels. each of the element contains list of labels for the step model.

#first pass is to collect the topic labels
for s in steps:
    doc_keys = "total-"+str(s)+".keys"
    dictionary = [] # list of all words in all topic models
    df = pd.read_csv(doc_keys,sep='\t',header=None)
    labels[s] = {}   # create list to contain labels for each Model
    for index, row in df.iterrows():
        words = row[3].split(" ")
        labels[s][row[0]]=row[1].lower()  # store the label for this topic id of this step

mt = {}
# second pass is to fill the MM (merged topics)
for s in steps:
    docs_xml = "total-"+str(s)+".xml"   # the diagnostic filename for this step
    print "processing " + docs_xml
    
    handler = open(docs_xml).read()
    soup = Soup(handler)
    topics = soup.find_all('topic')
    topics_list = []
    for t in topics:
        words = t.find_all('word')
        tokens = t['tokens'] 
        topic_id = int(t['id'])
        topic = {}
        topic['TOKENS'] = float(tokens)
        if topic_id in labels[s]: # prevent degenerate topic from being processed
            topic['LABEL'] = labels[s][topic_id] 
            if topic_id in labels[s]: # each topic is represented by words_dict ( a dictionary )
                topic['LABEL'] = labels[s][topic_id]  # the label for this topic
                for w in words:
                    topic[w.text] = float(w['prob'])
                
            if topic['LABEL'] in mt:
                # label is already there, so we merge the two, adjusting the TOKENS variable 
                # and probability of each word in the topic bag
                existing = mt[topic['LABEL']]
                newtopic = merge(existing, topic)
                mt[topic['LABEL']] = newtopic
                
            else:
                mt[topic['LABEL']] = topic
    print "current# labels " + str(len(mt))    

#sort
#mm.sort_values("LABEL", inplace=True)

def cosine(s1,s2):
    t1 = mt[s1]
    t2 = mt[s2]
    numerator = 0
    dena = 0

    for key1,val1 in t1.iteritems():
        if key1 in ['TOKENS','LABEL'] : continue #remove TOKENS and LABEL
        numerator += val1*t2.get(key1,0.0)
        dena += val1*val1
    denb = 0
    for key2,val2 in t2.iteritems():
        if key2 in ['TOKENS','LABEL'] : continue #remove TOKENS and LABEL
        denb += val2*val2
    return numerator/math.sqrt(dena*denb)
    
def topic(s):
    ''' print keywords of a topic, sorted '''
    t = mt[s]
    for key, value in sorted(t.iteritems(), key=lambda (k,v): (v,k)):
        print "%s: %s" % (key, value)
        
def search(s):
    ''' print keyword of a topic, sorted '''
    for key in mt:
        if s in mt[key]['LABEL']:
            print mt[key]['LABEL']

def word(w):
    ''' return in which topics this word appear '''
    for key in mt:
        if w in mt[key]:
            print mt[key]['LABEL']
    
def savetopics():
    with open("mergedtopics.pickle", 'wb') as f:
        pickle.dump(mt, f)
        
def loadtopics():
    pickle = open("mergedtopics.pickle", "rb")
    mt = pickle.load(pickle)
    