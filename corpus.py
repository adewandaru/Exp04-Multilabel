# -*- coding: utf-8 -*-
"""
This will fetch articles to CascadeLDA's module Labeled LDA.

"""

import psycopg2
import psycopg2.extras
import nltk
import string
import re
from string import maketrans

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

cur.execute("""select title, content, keywords, id from article where content like limit 10""")
rows = cur.fetchall() 

print (str(len(rows)) + "rows")

articles = []

for article in rows:
    content = clean(article['content'])
    from nltk.tokenize import word_tokenize
    
    print article['title']
    #tokenize article content
    tokens = word_tokenize (content)
    tokens = [ tok for tok in tokens if tok not in stopwords ]
    content = " ".join(tokens)
    try:
        keywords = [ w.strip().replace(" ", "_") for w in article['keywords'].split(",") ]
    except:
        keywords = ["N/A"]
        
    keywords = " ".join(keywords)
   
    row = [article['id'], keywords, content]
    articles.append(row)

import pandas as pd
df = pd.DataFrame.from_records(articles)

df.to_csv("result.csv", sep="\t", header=None, index=False)
    

