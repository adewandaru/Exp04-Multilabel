# -*- coding: utf-8 -*-


import psycopg2
import psycopg2.extras
import nltk
import string
import re


from collections import Counter
from nltk import FreqDist
from nltk import word_tokenize
import geopandas as gpd
import json
import string

import psycopg2
try:
    conn = psycopg2.connect("dbname='gatotkaca' user='postgres' host='localhost' password='Raisonne'")
except:
    print "I am unable to connect to the database"
    

'''
PROV = gpd.read_file('../data/geojson/IDN_adm_1_province.json')
KABKOTA = gpd.read_file('../data/geojson/IDN_adm_2_kabkota.json')
KEC = gpd.read_file('../data/geojson/IDN_adm_2_kabkota.json')
'''
D = gpd.read_file('../data/ina-geoportal/DesaIndonesia.shp')
K = gpd.read_file('../data/geojson/IDN_adm_2_kabkota.json')
P = gpd.read_file('../data/geojson/IDN_adm_1_province.json')

d1 = P.set_index('NAME_1')    # prop
d11 = P.set_index('VARNAME_1')# alias prop 
d2 = K.set_index('NAME_2')    # kabkota
d3 = D.set_index('KECAMATAN') # kec
d4 = D.set_index('DESA')      # desa



try:
    conn = psycopg2.connect("dbname='gatotkaca' user='postgres' host='localhost' password='Raisonne'")
except:
    print "I am unable to connect to the database"
    

def clean_symbols(line):
    
    for char in string.punctuation:
        line = re.sub("\(...\/...\)","",line)
        line = line.replace(char, ' ')
    return line.lower()
    
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


cur.execute(""" select title, content, keywords, id from article where keywords like '%banjir%' limit 100 """)
rows = cur.fetchall() 

print (str(len(rows)) + "rows")

for article in rows:
    content = clean_symbols(article['content'])
    from nltk.tokenize import word_tokenize
    tokens = word_tokenize (content)
    print "---" 
    print "Title:" + article['title']
    print(article['content'])
    print "Keywords: " + article['keywords']




