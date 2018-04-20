#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:05:49 2018

@author: srs

This scrip generates a dictionary file with investors and their investments. 
This file speeds up the process of acquiring investor network dataset.
Takes about 10 min to finish. 
"""

import pandas as pd
from collections import defaultdict
import numpy as np

if __name__ == '__main__':
    
    df = pd.read_csv('df_short_description_nonan.csv')
    d = defaultdict(list)
    for inves in df.investor.unique():
        for v in df[df.investor == inves].clean_url.unique():
            d[inves]  += [v]
    
    np.save('./data/company_url.npy', d)        