#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:02:40 2018

@author: srs

This 
"""

from utils import *
import utils

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
import sqlalchemy

from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.dialects.postgresql import JSONB

import importlib
from collections import defaultdict
from collections import Counter
try:
    import cPickle as pickle
except ImportError:  # python 3.x
    import pickle
importlib.reload(utils)

def update_tages(x):
    tag_list_out = []
    tag_list_in = x.replace(',','').split()
    for i in tag_list_in:
        if i in tag_dict:
            if tag_dict[i] != 'noise':
                tag_list_out.append(str(tag_dict[i]))
    return ((tag_list_out))

def tag_dic(x):
    tags = (Counter(x))
    out_dic = {}
    for i,j in tags.items():
        out_dic[i] = j
    return(out_dic)
        

if __name__ == '__main__':
    
    df_cluster_1 = pd.read_csv('./data/cluseter_1.csv')
    df_cluster_1 = df_cluster_1.drop('Unnamed: 0', axis=1)
    
    with open('/data/clustername.p', 'rb') as fp:
        clustername = pickle.load(fp)
        
    cluster_tag=  pd.DataFrame.from_dict(clustername, orient = 'index')
    cluster_tag.columns = ['tags']
    cluster_tag = cluster_tag.reset_index()
    df_cluster_manual_tag = pd.merge(df_cluster_1, cluster_tag,  how='left', left_on=['dbscan'], right_on = ['index'])
    
    df_cluster_manual_tag_dic = df_cluster_manual_tag[['Unnamed: 0.1','tags' ]]
    df_cluster_manual_tag_dic.columns = ['original_tags', 'clean_tags']
    d = df_cluster_manual_tag_dic.to_dict(orient="index")
    
    tag_dict = df_cluster_manual_tag_dic.set_index('original_tags')['clean_tags'].to_dict()
    
    df1 = pd.read_csv('./data/companies_funding_tag_reshape_description_short_description.csv')
    df2 = pd.read_csv('./data/investor_description_nonan.csv')
    
    df_main = df1.groupby([ 'investor','clean_url','tag_reshape'],as_index = False)[['short_description']].count()
    df_main['tag_len'] = df_main.tag_reshape.apply(lambda x: len(x))
    
    df_main['tag_update'] = df_main.tag_reshape.apply(update_tages)
    df_main_tag= df_main.groupby([ 'investor'],as_index = True)[['tag_update']].sum()
    df_main_tag = df_main_tag.reset_index()
    
    df_main_tag['tag_count'] = df_main_tag.tag_update.apply(tag_dic)
    df_main_tag = df_main_tag[['investor','tag_count']]
    
    df_url = pd.read_csv('./data2/investor_url.csv')
    df_url_mer = df_url[['investor','clean_url']].copy()

    df_main_tag = pd.merge(df_main_tag, df_url_mer, on= 'investor')
    ### Creat or update a table on DB:
    
    host= open('host.txt', 'r').read()
    password= open('password.txt', 'r').read()
    user= open('user.txt', 'r').read()
    dbname= open('dbname.txt', 'r').read()
    port= open('port.txt', 'r').read()
        
    db_credentials = {
            'database': dbname,
            'drivername': 'postgres',
            'host': host,
            'password': password,
            'port': '5432',
            'username': user}
    
    engine = create_engine(URL(**db_credentials))     
    df_main_tag.to_sql('investor_clustered_tag', engine, index= False, if_exists = 'replace', dtype={'tag_count':JSONB})