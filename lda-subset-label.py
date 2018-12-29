# -*- coding: utf-8 -*-
"""
Spyder Editor

This is checking how many labels that our corpus presented.
"""

import psycopg2
try:
    conn = psycopg2.connect("dbname='gatotkaca' user='postgres' host='localhost' password='Raisonne'")
except:
    print "I am unable to connect to the database"
    
    
    
cur = conn.cursor()


cur.execute(""" select sum(array_length(regexp_split_to_array(keywords, '\s+'),1)) from article """)
rows = cur.fetchall() 
print (rows)