#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:54:15 2018

@author: srs
"""

import pandas as pd
import numpy as np
from numpy.random import random, permutation, randn, normal, uniform, choice

import psycopg2
from IPython.display import display, Audio
import re
# from IPython.html.widgets import HTML
# import IPython.html 

# from IPython.html.widgets import HTML

# from IPython.html import widgets
# from IPython.display import display, Image, HTML, clear_output

from isoweek import Week
from pandas_summary import DataFrameSummary
import calendar
import os
import matplotlib.pyplot as plt

import numpy as np
import datetime as df
import time

import matplotlib.image as mpimg
import statsmodels.nonparametric.api as smnp
import seaborn as sns

import plotly as pl

from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Bar, Scatter, Figure, Layout
import plotly.graph_objs as go
from plotly.graph_objs import *
import cufflinks as cf

import folium
from folium.plugins import MarkerCluster
from folium import plugins
from folium.plugins import HeatMap
import folium

from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk import word_tokenize
import pyLDAvis
import pyLDAvis.sklearn
pyLDAvis.enable_notebook()

from nltk.corpus import stopwords
my_stops = stopwords.words('english')
from gensim.models import word2vec  
import logging  

import gensim
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
from os import listdir
from os.path import isfile, join
import sys

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
from bokeh.io import output_notebook

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

print ("plotly ",__version__)
init_notebook_mode(connected=True)

def join_df(left, right, left_on, right_on=None, col_on = None):
    if right_on is None: right_on = left_on
    return left.merge(right[col_on], how='left', left_on=left_on, right_on=right_on, 
                      suffixes=("", "_y"))


import importlib
from collections import defaultdict

current_dir = os.getcwd()
print ('current folder: ',current_dir)

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils.data_utils import get_file
import bcolz
from sklearn.cluster  import KMeans
from scipy.cluster.vq import kmeans

from sklearn.cluster import DBSCAN

from MulticoreTSNE import MulticoreTSNE as TSNE
from bs4 import BeautifulSoup
import re
import multiprocessing ## great tool to keep track of loop process
from itertools import product

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle
from sklearn.model_selection import train_test_split
from numpy.random import random, permutation, randn, normal, uniform, choice
import sklearn.manifold

from hdbscan import HDBSCAN
from collections import Counter

from spacy.lang.en.stop_words import STOP_WORDS
from collections import defaultdict

country_name= pd.read_html('https://gist.github.com/kalinchernev/486393efcca01623b18d')[0][1].tolist()
def load_array(fname):
    return bcolz.open(fname)[:]
                     