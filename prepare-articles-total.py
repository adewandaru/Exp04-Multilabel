# -*- coding: utf-8 -*-
"""
This will prepare training of MALLET Labeled LDA, splitting the entire dataset into 10K "steps" in form of CSVs.
each of this step will be converted into ".seq" file, then that file will be trained using Labeled LDA,
outputting .keys, .xml diagnostics file.
"""

import psycopg2
import psycopg2.extras
import nltk
import string
import re
from string import maketrans
import numpy as np

import csv

stopwords = ['detikcom']
try:
    conn = psycopg2.connect("dbname='gatotkaca' user='postgres' host='localhost' password='Raisonne'")
except:
    print "I am unable to connect to the database"
    

def clean(line):
    # first we change the "." to space so it won't get removed by translate(string.punctuation) on the next line
    line = line.replace(".", " ")
    line = line.replace("-", " ")
    line = line.replace("\xc2\xa0", "")
    
    '''
    ins = string.digits
    outs = "XXXXXXXXXX"
    trans = maketrans(ins, outs)
    line = line.translate(trans)
    '''
    line = line.translate(None, string.punctuation + string.digits)
    return line.lower()
    
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#cur.execute("""select title, content, keywords, id from article where  date_part( 'year', date ) = 2018""")
import pandas as pd
def dump_rec(fp):
        
    cur.execute("""select title, content, keywords, id, date from article ORDER BY date LIMIT 100""")
    for article in cur:
        
        #print article['date']
        content = clean(article['content'])
        from nltk.tokenize import word_tokenize
        
        #print article['title']+" ==> "+str(article['keywords'])
        
        #tokenize article content
        tokens = word_tokenize (content)
        tokens = [ tok for tok in tokens if tok not in stopwords ]
        content = " ".join(tokens)
        
        try:
            keywords = [ w.strip().replace(" ", "_") for w in article['keywords'].split(",") ]        
        except:
            keywords = ["N/A"]

        #reduce topic label for better memory constraint. use this ONLY for particular step which 
        #triggers out of memory errors.
        if len(keywords)>1:
            del keywords[-1]
        keywords = " ".join(keywords)
        row = [article['id'], keywords, content] # third element is suggested keywords
        #print row
        #list1=[58,100,'dir1/dir2/dir3/file.txt',0.8]
        wr = csv.writer(fp, delimiter='\t')
        wr.writerow(row)
         



with open("output.csv", "a") as fp:
    dump_rec(fp)

