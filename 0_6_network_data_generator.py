#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 14:15:45 2018
This code generates “investor_network_data.csv” for farther network analysis 
@author: srs
"""

import pandas as pd
import  multiprocessing
import numpy as np

def intersect(a, b): return list(set(a) & set(b))

def network_data_gen(company1):
    output = []
    company_list_1 = comp_dic[company1]
        
    for company2 in complist:
        company_list_2 = comp_dic[company2]
        interlen  = len(intersect(company_list_1,company_list_2))
            
        if interlen >0 and company1 != company2:
            output.append([company1, company2, interlen, intersect(company_list_1,company_list_2), len(company_list_1), len(company_list_2)])

    return(output)

def dataframe(x):
    try:
        df = pd.DataFrame.from_records(network_data[x], columns = labels)
        if df.empty:
            print (x)
        else :
            return (df)
    except:
        pass
        
if __name__ == '__main__':
    network_data = []
   
    labels = ['investor1', 'investor2', 'weight', 'overlapping_companies', 'unique_investments_company_1','unique_investments_company_2' ]

    df = pd.read_csv('df_short_description_nonan.csv')
    
    complist = df.investor.unique()
    comp_dic = np.load('dicsave.npy').item()
    
    df2 = pd.DataFrame(columns = labels)
    
    with multiprocessing.Pool(processes=28) as pool:
        network_data = (pool.map(network_data_gen, complist))
        df2 = df2.append(pool.map(dataframe, range(len(network_data)))) 
        
    df2.to_csv('./data/investor_network_data.csv')
    