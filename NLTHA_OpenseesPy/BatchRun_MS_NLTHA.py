# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:32:05 2019

@author: VACALDER
"""

#------------------------------------------------------------------------------
#|      PROGRAM TO CHECK TIME DEPENDENT PROPERTIES EFFECTS ON STRUCTURES      |
#|      
#|
#|          Victor A Calderon
#|          PhD Student/ Research Assistant
#|          NC STATE UNIVERSITY 
#|          2019 (c)
#|
#|
#------------------------------------------------------------------------------

# ----------------------------------------------------------------------------
#| VARIABLES THAT CHANGE WITH TIME
# ----------------------------------------------------------------------------
#
#
# *cover = Cover of concrete in cm
# *Tcorr = Time to corrosion in yrs
# *Time  = Different times that are being analyzed
# *wcr   = Water to cement ratio
# *dbi   = Initial longitudinal bar diameter
# *dti   = Initial transverse steel diameter



icover=[4.,5.,7.5]
iTcorr= [1.1307,1.7667,3.975]
iTime= [5.,10.,15., 20., 25., 30., 35., 40., 45., 50., 55., 60., 65., 70., 75.]
iwcr= [0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70]
dbi= 0.75   
dti= 0.375  
MS_path=r'C:\Users\vacalder\Documents\TimeDependent_PBEE\EarthquakeSelection\MainShock_Test'
MSListing = os.listdir(MS_path)

for GM in MSListing:
    for cover in icover:
        for Tcorr in iTcorr:
            for Time in iTime:
                for wcr in iwcr:
                    #set Functions for Fiber Model and NLTHA