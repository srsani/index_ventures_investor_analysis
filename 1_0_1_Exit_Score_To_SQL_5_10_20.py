#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 11:56:14 2018

@author: Sohrab Redjai Sani

1. Reads "companies_funding" and "companies_status" and make a new dataset,
2. Calculate the exit score for 5, 10 and 20 years.
3. Either make a new table or update the already exiting table in the data base.
"""

from utils import *

def exit_score (x):
   # takes an integer number that reflects how many years back the score needs to be calculated from.
    df1 = pd.read_csv('./data/companies_funding.csv')
    df2 = pd.read_csv('./data/companies_status.csv')
    df_main = join_df(df1, df2, "ds_uuid", "ds_uuid", col_on = ['ds_uuid','status'])
    df_main['date_pars'] = pd.to_datetime(df_main.date)
    df_main['year'] = df_main.date_pars.dt.year

    df_main = df_main[df_main.year >=2018-x]

    def successes_value_20(x):
        if x == 'operating':
                return(0)
        elif x == 'acquired':
                return (1)
        elif x == 'closed':
                return (-2)
        elif x == 'ipo':
                return (2)

    def period(xx): return (x)

    df_main['exit_scores'] = df_main['status'].apply(successes_value_20)
    df_main['period'] = df_main['status'].apply(period)
    df_g1 = df_main.groupby([ 'investor','period'],)[['exit_scores',]].sum()
    df_sql_20 = df_g1.reset_index()
    return (df_sql_20)


if __name__ == '__main__':
    ## make 3 data set for 20, 10, and 5 years

    df20 = exit_score(20)
    df10 = exit_score(10)
    df5 = exit_score(5)

    result = df20.append([df10,df5 ])
    result = result[result.investor != 'Unknown']

    df_url = pd.read_csv('./data2/investor_url.csv')
	df_url_mer = df_url[['investor','clean_url']].copy()

	result = pd.merge(result, df_url_mer, on = 'investor')

    ## Uploed the df to the DB
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
        'username': user
    }

    engine = create_engine(URL(**db_credentials))

    result.to_sql('investors_exit_score', engine, index= False,if_exists = 'replace')
