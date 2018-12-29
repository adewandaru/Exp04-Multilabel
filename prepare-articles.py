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


cur.execute(""" select title, content, keywords, id from article where content like '%meter%' limit 50 """)
rows = cur.fetchall() 

print (str(len(rows)) + "rows")

articles = []

for article in rows:
    content = clean(article['content'])
    from nltk.tokenize import word_tokenize
    
    tokens = word_tokenize (content)
    tokens = [ tok for tok in tokens if tok not in stopwords ]
    content = " ".join(tokens)
    
    keywords = article["keywords"].split(",")
    keywords = " ".join(keywords)
    print keywords
    
    #print(tokens)
    print article['keywords']
    print article['title']
    row = [article['id'], content, keywords]
    articles.append(row)
    
    
    
import pandas as pd
df = pd.DataFrame.from_records(articles)
print df
df.to_csv("output1.csv", header=None, index=False)
    
    
    
    



'''

# this script will prepare the dictionary based on sample corpora.
import re
from gensim import corpora, models, similarities
stoplist = set(line.rstrip() for line in open("stopwords.txt"))

list_of_list = [re.findall(r"[\w']+", line.lower()) for line in open('detik2013-2016.cleaned.lower.txt')]
list2 = [[item for item in list if not item.isdigit() and not item.isupper()] for list in list_of_list]
dictionary = corpora.Dictionary(list2)

stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids)
dictionary.compactify()
print dictionary
dictionary.save("detik.dict")

'''
