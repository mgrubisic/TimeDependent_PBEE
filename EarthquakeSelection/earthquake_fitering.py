# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:52:27 2019

@author: VACALDER
"""


import math  as math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


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
plt.show