# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 02:45:22 2018

@author: dewandaru@gmail.com
This is for getting the uncrawled keywords and put it on to the database.

"""
from collections import Counter
from nltk import FreqDist
from nltk import word_tokenize
import geopandas as gpd
import json
import string
import urllib2
from bs4 import BeautifulSoup
import psycopg2.extras

import psycopg2
try:
    conn = psycopg2.connect("dbname='gatotkaca' user='postgres' host='localhost' password='Raisonne'")
except:
    print "I am unable to connect to the database"
    


cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
cur.execute("""SELECT url, id FROM article WHERE url NOT LIKE '%20.detik.com%'""")

rows = cur.fetchmany(10)
for r in rows:
    print r
    _id = r["id"]
    # scrap
    html = urllib2.urlopen (r["url"]).read()
    soup = BeautifulSoup(html, 'html.parser')
    attrs = soup.find('meta', attrs={'name': 'keywords'}).attrs
    keyword = attrs['content']
    
    # now let's save the keyword back into db
    cur.execute("UPDATE article SET keywords = (%s) WHERE id=%s ",(keyword, _id))
    print str(cur.rowcount) + " rows affected"
    

print len(rows)
