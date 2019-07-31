# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:52:27 2019

@author: VACALDER
"""


import math  as math
import numpy as np
import matplotlib.pyplot as plt
import csv


# EARTHQUAKE SELECTION PROGRAM
# Data base is taken fron NGA West 2 database from  PEER
with open('MS-AS_PEER_Website.csv',newline='') as peer:

    PeerReader = csv.reader(peer)
    
    EqNames = []
    Mws = []
    Rrups=[]
    PGAs=[]
    PGVs=[]
    Vs30s=[]
    for row in PeerReader:
        EqName = row[3]
        Mw = row[10]

        EqNames.append(EqName)
        Mws.append(Mw)

    #print(EqNames)
    #print(Mws) 
    

# LOAD DATASET