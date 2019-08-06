# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:52:27 2019

@author: VACALDER
"""


import math  as math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


# EARTHQUAKE SELECTION PROGRAM
# Data base is taken fron NGA West 2 database from  PEER

PeerDB = pd.read_csv('MS-AS_PEER_Website.csv')
# Converting column names to lowercase and spaces changed to lower hyphen _
PeerDB.columns=PeerDB.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

# Data is filtered according to the following criteria:
# * Moment Magnitude M=>5
# * PGA>0.04
# * PGV>1 cm/s
# * Vs30>100m/s & Vs30<1000m/s
# * Lowest ussable frequency is less than 1Hz
# * Rrup<60km

magnitude_filter=(PeerDB.earthquake_magnitude>=5)
pga_filter=(PeerDB.pga_g>=0.04)
pgv_filter=(PeerDB.pgv_cm_sec>=1)
vs30_filter=(PeerDB.vs30_m_s_selectedforanalysis.between(100,1000))
freq_filter=(PeerDB.lowestusablefreq_h1_hz<=1)
rrup_filter=(PeerDB.joyner_booredist_km <= 60)
all_filters=magnitude_filter & pga_filter & pgv_filter & vs30_filter & freq_filter & rrup_filter


Peer_Filtered=PeerDB[all_filters]

# Plotting Data Points

Peer_Filtered.plot(kind='scatter',x='joyner_booredist_km',y='earthquake_magnitude')
#plt.show

# Selecting Mainshocks and generate string to download RSN

dwnstr=''

for x in range(0,2):
    print('the valu of x is ',x)
    Main_Shocks=Peer_Filtered[Peer_Filtered['earthquake_name'].str.contains('0'+str(x))]

for i, row in Main_Shocks.iterrows():
    dwnstr=','+str(row['record_sequence_number'])+dwnstr
    
MSstr=dwnstr[1:]
# Accesing  PEER Website

browser = webdriver.Chrome() 
url="https://ngawest2.berkeley.edu/users/sign_in?unauthenticated=true"    
browser.get(url)
browser.find_element_by_id("user_email").send_keys('vacalder@ncsu.edu')
browser.find_element_by_id("user_password").send_keys("ViCk2016")
browser.find_element_by_id("user_submit").click()
url2="https://ngawest2.berkeley.edu/spectras/223218/searches/new"
browser.get(url2)
browser.find_element_by_xpath('//*[@id="search_search_nga_number"]').send_keys(MSstr)
browser.find_element_by_xpath('//*[@id="new_search"]/div[2]/fieldset/button').click()

    
# SelectiNG Aftershocks and generate String to download RSN

    
for y in range (2,3):
    print('the valu of y is ',y)
    Aftershocks=Peer_Filtered[Peer_Filtered['earthquake_name'].str.contains('0'+str(y))]
    
    
for y in range (3,8):
    print('the valu of y is ',y)
    df=Peer_Filtered[Peer_Filtered['earthquake_name'].str.contains('0'+str(y))]
    Aftershocks=Aftershocks.append(df)

