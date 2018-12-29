# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 06:06:23 2018

@author: dewan
"""
#steps = [0, 10000]
steps = range(0, 650000, 10000)

import sys
import operator
import pandas as pd
from bs4 import BeautifulSoup as Soup
import pickle
import math

try:
  mt
except NameError:
    mt = {}
    mt["null"] = {'TOKENS':0, 'LABEL':'null' }
    total = 0

def merge (a, b):
    
    ''' merge two dictionaries, each is bag of word of topic '''
    ''' P(A U B) = P(A) + P(B) - P(A n B) '''
    
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
    
def count(t):
    if t in mt:
        return mt[t]['TOKENS']
    else:
        return 0

def merge_all():
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
    m = 0
    
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
                    m = m + 1
                    # label is already there, so we merge the two, adjusting the TOKENS variable 
                    # and probability of each word in the topic bag
                    existing = mt[topic['LABEL']]
                    newtopic = merge(existing, topic)
                    mt[topic['LABEL']] = newtopic
                    
                else:
                    mt[topic['LABEL']] = topic
        print "current# labels " + str(len(mt))    
    print "merging count:" + str(m)
    #sort
    #mm.sort_values("LABEL", inplace=True)
    
def merge_topic(s1,s2,newlabel):
    newtopic = merge(mt[s1], mt[s2])
    mt[newlabel] = newtopic
    

def cosine_topic(s1,s2):
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
    if dena == 0 or denb == 0 : return 0
    return numerator/math.sqrt(dena*denb)

def topic2(s, w=None):
    ''' 
    return keywords of a topic, sorted 
    '''
    i = 0
    t = mt[s]
    s = sorted(t.iteritems(), key=operator.itemgetter(1), reverse=True)[:20]
    str = ""
    for w in s:
        str = str + w[0] + " "
    print str
        
    
def topic(s, w=None):
    ''' 
    return keywords of a topic, sorted 
    '''
    t = mt[s]
    return sorted(t.iteritems(), key=operator.itemgetter(1), reverse=True)
    #for key, value in sorted(t.iteritems(), key=lambda (k,v): (v,k)):
        #if w is not None and (key == w): 
        #    print "*"
        #print "%s: %s" % (key, value)
        #result[key] = value
        
def search(s):
    ''' returns list of topic labels and probs which contains the label string '''
    result = []
    for key in mt:
        if s in mt[key]['LABEL']:
            res = [[mt[key]['LABEL'],mt[key]['TOKENS']]]
            result.append(res)
    return result

        
def st(s):
    ''' returns list of topic labels which contains the label string '''
    result = []
    for key in mt:
        if s in mt[key]['LABEL']:
            res = mt[key]['LABEL']
            result.append(res)
    return result

def tsort(list):
    ''' sort the list of topic labels, sorted by probability of the topic'''
    result = {}
    for key in list:
        result[key] = mt[key]['TOKENS']
    return sorted(result.iteritems(), key=operator.itemgetter(1), reverse= True)

def wsort(list, w):
    ''' 
    sort the list of topic labels, sorted by probability of 
    the word in the topic normalized by the topic count
    '''
    result = {}
    for key in list:
        result[key] = mt[key][w] * mt[key]['TOKENS']
    return sorted(result.iteritems(), key=operator.itemgetter(1), reverse=True)

def word(w):
    ''' return list of topic labels in which topics word w appear '''
    result = []
    for key in mt:
        if w in mt[key]:
            result.append(mt[key]['LABEL'])
    return wsort(result, w)

def w(_w):
    ''' return list of topic labels in which topics word w appear '''
    result = []
    for key in mt:
        if _w in mt[key]:
            result.append(mt[key]['LABEL'])
    return result

def savet():
    with open("mergedtopics.pickle", 'wb') as f:
        pickle.dump(mt, f)
        
def loadt():
    global mt
    global total
    
    pickle_in = open("mergedtopics.pickle", "rb")
    mt = pickle.load(pickle_in)
    total = gettotal()
    
def coh(s):
    # find coherence of a topic
    t = mt[s]
    # list all keywords
    words = topic(s)
    
    M = 30
 
    words.pop(0) #['TOKENS']
    words.pop(0) #words['LABEL']
    score = 0
    if M > len(words): M = len(words) - 1
    for m in range(1, M):
        for l in range(0, m):
            print "m = " + str(m)
            print "l = " + str(l)
            print words[m][0]+","+ words[l][0]
            try:
                num = cooc(words[m][0],words[l][0]) + 0.01 
                den = oc(words[l][0]) + 0.01
                score = score + math.log( float(num) / float(den) )
            except:
                print num
                print den
    return score


def coh2(t):
    words =t
    M = 20
    words.pop(0) #['TOKENS']
    words.pop(0) #words['LABEL']
    score = 0
    if M > len(words): M = len(words) - 1
    for m in range(1, M):
        for l in range(0, m):
            print "m = " + str(m)
            print "l = " + str(l)
            print words[m][0]+","+ words[l][0]
            try:
                num = cooc(words[m][0],words[l][0]) + 0.01 
                den = oc(words[l][0]) + 0.01
                score = score + math.log(  float(num) / float(den)  )
            except:
                print num
                print den
    return score

cache1 = {}
cache2 = {}

def cooc(w1,w2):
    if (w1,w2) in cache2: return cache2[(w1,w2)]
    cur.execute("""
    SELECT COUNT(*)
    FROM article
    WHERE content_idx_col @@ to_tsquery('%s&%s')
    """%(w1,w2))
    rows = cur.fetchall() 
    cache2[(w1,w2)]=rows[0][0]
    return rows[0][0]


def oc(w1):
    if w1 in cache1 : return cache1[w1]
    cur.execute("""
    SELECT COUNT(*)
    FROM article
    WHERE content_idx_col @@ to_tsquery('%s')
    """%(w1))
    rows = cur.fetchall() 
    cache1[w1] = rows[0][0]
    return rows[0][0]

import psycopg2
import psycopg2.extras
try:
    conn = psycopg2.connect("dbname='gatotkaca' user='postgres' host='localhost' password='Raisonne'")
except:
    print "I am unable to connect to the database"
    
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

'''
s = "0.071*banjir + 0.066*air + 0.039*sungai + 0.021*warga + 0.020*hujan + 0.020*cm 
+ 0.014*tergenang + 0.014*rumah + 0.013*surut + 0.013*deras + 0.013*jalan + 0.012*ketinggian 
+ 0.012*wilayah + 0.012*pompa + 0.011*meter + 0.010*terendam + 0.010*kawasan + 0.010*menggenangi 
+ 0.008*lokasi + 0.008*meluap + 0.008*airnya + 0.008*tanggul + 0.007*aliran + 0.007*mengguyur 
+ 0.006*titik + 0.006*mencapai + 0.006*daerah + 0.006*akibat + 0.006*luapan + 0.006*detikcom 
+ 0.006*dummy"

s = "0.201*gempa + 0.055*bumi + 0.047*mengguncang + 0.044*tsunami + 0.038*berkekuatan + 0.027*kerusakan + 0.025*kilometer + 0.021*akibat + 0.016*warga + 0.016*barat + 0.015*korban + 0.015*petang + 0.015*wilayah + 0.011*rumah + 0.011*peringatan + 0.010*pantai + 0.010*pusat + 0.010*bencana + 0.009*orang + 0.009*jiwa + 0.009*dampak + 0.008*laporan + 0.008*tewas + 0.008*stroke + 0.008*sebelah + 0.007*berolahraga + 0.007*dilaporkan + 0.007*dilansir + 0.006*tersumbat + 0.006*terserang + 0.006*dummy"
terms = s.split("*")
terms.pop(0)
terms.pop()
gs = []


gs.append(("x",0))
gs.append(("y",0))

for w in terms:
    wt = w.split()[0]
    gs.append((wt,0))
    
    '''
    
epsilon = 0.0000001
def wt(w,t):
    ''' return the probability of w appear in topic T '''
    if t in mt[t]:
        if w in mt[t]:
            return mt[t][w]
        else:
            return epsilon
    else:
        return epsilon
    
def wT(w,T):
    ''' return the probability of w given set of topics T '''
    p = 0
    sumt = 0
    for t in T:
        p = p + wt(w,t)
        sumt = sumt + prob(t)
    print "total " + str(sumt)
    print "p " + str(p)
    return p

def probt(t):
    global total
    return count(t) / total

def gettotal():
    res = 0
    for t in mt:
        res = res + int(mt[t]['TOKENS'])
    return float(res)

def checkprob(): 
    s = 0
    for k in mt:
        s = s + probt(k)
    return s
    
def ww(w1,w2):
    ''' mengembalikan peluang w1 dan w2 muncul bersama dalam sembarang topic '''
    tt1 = w(w1) # list of topics that contains word w1
    tt2 = w(w2)
    tt = isec(tt1,tt2)
    return tt

def isec(lst1, lst2): 
    ''' intersect '''
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 
    
    
    
    
    
    
    
