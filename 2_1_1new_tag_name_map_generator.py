#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 12:21:07 2018

@author: srs
This code saves the new cluster name dictionary to “clustername.p” for future use.
"""

clustername = {-1:'noise',
            0:'Classifieds Locations',
            1:'Networking Solutions',
           2: 'Country/Continent',
           3:'Medical Procedures',
              4:'Life Sciences',
              5:'Healthcare',
              6:'Pharmaceutical',
              7:'Media',
              8:'Fashion',
              9:'Food And Beverages',
              10: 'Agriculture',
              11:'Operating System',
              12: 'Nonprofits',
              13:'Education',
              14:'Physical Retail',
              15:'Mobility',
              16:'Advertising',
              17:'noise',
              18:'Music',
              19:'Real Estate',
              20:'Waste Management',
              21:'Energy',
              22:'Social Media',
              23:'noise',
              24:'Travel Tourism',
              25:'Events Management',
              26:'Sports',
              27:'Film And Media',
              28:'Web Infrastructure',
              29:'Saas',
              30:'Staffing',
              31: 'Finance',
              32:'Cosmetic Industry',
              33: 'noise',
              34: 'Tech Buzzwords',
              35: 'Lifestyle Family',
              36:'Language',
              37:'Professional Services',
              38:'Analytics',
              39:'Telecom And Networking',
              40:'Virtual And Augmented Reality',
              41: 'noise',
              42: 'Furniture',
              43:'Semiconductors',
              44:'Hardware',
              45:'Hardware',
              46:'Enterprise',
              47:'Advertisement',
              48:'Litigation',
              49:'noise',
              50:'Cyber Security',
              51: 'noise',
              52:'Security',
              53:'Workflow Automation',
              54:'Events',
              55:'noise',
              56:'noise',
              57:'Defense',
              58:'noise',
              59:'Productivity',
              60:'Architecture/Construction',
              61:'Personal Development'}

try:
    import cPickle as pickle
except ImportError:  # python 3.x
    import pickle

with open('clustername_ver3.p', 'wb') as fp:
    pickle.dump(clustername, fp, protocol=pickle.HIGHEST_PROTOCOL)
