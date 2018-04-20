#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:06:08 2018

@author: srs
"""

from utils import *

def operating_profile_score(val1, val2, year):
    """ take two investment rounds and the period in
    which the “operating score” should be calculated."""

    def period(xx): return (year)
    def rfround(xx): return (val1+' / '+val2)
    df_main = pd.read_csv('companies_funding_dollar_adjusted_status.csv')
    df_main_operating = df_main[df_main.status == 'operating']
    df_main_operating = df_main_operating[df_main_operating.amount_raised > 10000]

    df_main_operating['date_pars'] = pd.to_datetime(df_main_operating.date)
    df_main_operating['year'] = df_main_operating.date_pars.dt.year

    df_main_operating = df_main_operating[df_main_operating.year >=2018-year]

    df_main_operating_seed = df_main_operating[(df_main_operating.round_type_fixed == val1) ]
    df_main_operating_ven = df_main_operating[(df_main_operating.round_type_fixed == val2)]
    df_main_operating_ve_seed =  pd.concat([df_main_operating_seed, df_main_operating_ven])

    money = df_main_operating_ve_seed.groupby([ 'clean_url','date','round_type_fixed','investor'],as_index = False)[['adjusted_amount_raised']].mean()
    money2 = money.groupby([ 'clean_url','round_type_fixed','date'],as_index = False)[['adjusted_amount_raised']].mean()
    money22 = money2.groupby([ 'clean_url','round_type_fixed'],as_index = False)[['adjusted_amount_raised']].sum()

    money22['difference_money_raised'] = money22.groupby([ 'clean_url',],as_index = False)[['adjusted_amount_raised']].diff()
    money22['operating_profile_score'] = money22.groupby([ 'clean_url'],as_index = False)[['adjusted_amount_raised']].pct_change(1)

    money3 = money22.groupby([ 'clean_url'],as_index = True)[['operating_profile_score']].sum()
    money3_as = money3.sort_values('operating_profile_score', ascending=False)

    money4 = money3_as.reset_index()

    df_main_operating_seed = join_df(df_main_operating_seed, money4, "clean_url", "clean_url", col_on = ['clean_url','operating_profile_score'])

    df_main_operating_seed_nan = df_main_operating_seed.dropna()
    df_main_operating_seed_nan['year_s'] = df_main_operating_seed_nan.year.apply(lambda x: str(x))

    df_g1 = df_main_operating_seed_nan.groupby([ 'investor'],)[['operating_profile_score']].mean()
    df_des = df_g1.sort_values('operating_profile_score', ascending=False)
    df_return = df_des.reset_index()
    df_return['period'] = df_main['investor'].apply(period)
    df_return['funding_round'] = df_main['investor'].apply(rfround)
    return (df_return)

if __name__ == '__main__':
    """ make 9 data set for 20, 10, and 5 years
        seed, venture a
        venture a, venture b
        venture b, venture c

    """
    ops_s_a20 = operating_profile_score('seed', 'venture a', 20)
    ops_s_a_10 = operating_profile_score('seed', 'venture a', 10)
    ops_s_a_5 = operating_profile_score('seed', 'venture a', 5)

    ops_a_b_20 = operating_profile_score('venture a', 'venture b', 20)
    ops_a_b_10 = operating_profile_score('venture a', 'venture b', 10)
    ops_a_b_5 = operating_profile_score('venture a', 'venture b', 5)

    ops_b_c_20 = operating_profile_score('venture b', 'venture c', 20)
    ops_b_c_10 = operating_profile_score('venture b', 'venture c', 10)
    ops_b_c_5 = operating_profile_score('venture b', 'venture c', 5)
    result = ops_s_a20.append([ops_s_a_10,ops_s_a_5, ops_a_b_20, ops_a_b_10, ops_a_b_5, ops_b_c_20,ops_b_c_10 ,ops_b_c_5])

    df_url = pd.read_csv('./data2/investor_url.csv')
    df_url_mer = df_url[['investor','clean_url']].copy()

    result = pd.merge(result, df_url_mer, on= 'investor')

   # Creat a table or update a table on DB
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
    result.to_sql('operating_profile_score', engine, index= False,if_exists = 'replace')
