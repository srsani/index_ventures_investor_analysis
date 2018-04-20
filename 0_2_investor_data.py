#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 14:48:40 2018

@author: srs

This scrip initially relevant information for future NLP process on based on “description” 
and “short_description” of companies. And only save the English despites to a csv file. 
This process takes around 10 min when 28 process is utilized. 

"""

import pandas as pd
import psycopg2
#from pandas_summary import DataFrameSummary
from langdetect import detect
import multiprocessing ## great tool to keep track of loop process

def lang (x):
    try:
        language = detect(x)
        return (language)
    except:
        return('Bad value:', x)
        
if __name__ == '__main__':
    host= open('host.txt', 'r').read()
    password= open('password.txt', 'r').read()
    user= open('user.txt', 'r').read()
    dbname= open('dbname.txt', 'r').read()
    port= open('port.txt', 'r').read()
    
    try:
        conn = psycopg2.connect(dbname=dbname , user=user, host=host, password=password, port = '5432')
        cur = conn.cursor()
    except:
        print ("I am unable to connect to the database")
    
    df = pd.read_sql('SELECT companies_funding.investor, companies_funding.clean_url, companies_funding.ds_uuid, companies_description.description, companies_description.short_description FROM companies_funding LEFT JOIN companies_description ON companies_funding.ds_uuid = companies_description.ds_uuid ORDER BY investor, clean_url', conn)
    #display(DataFrameSummary(df).summary())
    df_nonan = df.dropna()
   # display(DataFrameSummary(df_nonan).summary())
    
    with multiprocessing.Pool(processes=28) as pool:
        df['short_language'] = pool.map(lang, df['short_description'])
        df['description_language'] = pool.map(lang, df['description'])
        
    df_description= df[['investor', 'clean_url','ds_uuid', 'description' ]]
    df_description_nonan = df_description.dropna()
    
    df_short_description = df[['investor', 'clean_url','ds_uuid', 'short_description' ]]
    df_short_description_nonan = df_short_description.dropna()
    
    df_description_nonan.to_csv('./data/df_description_nonan.csv')
    df_short_description_nonan.to_csv('./data/df_short_description_nonan.csv')