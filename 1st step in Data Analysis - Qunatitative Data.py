# -*- coding: utf-8 -*-
"""
Tanmoy Das; PhD Researcher in Training at Dalhousie University
"""
# import libraryies
import pandas as pd
import matplotlib.pyplot as plt
data_01 = pd.read_csv("../Data/length of ship damages.csv")



# Plotting histogram
plt.hist(data_01['length of ship damage'])
# A hell lot of zeros



# Summary Statistics
data_01.describe()
# we have problem- Negative values




# Checking NAs
data_01.isnull()
#.sum()
# Remove NAs or Data Wrangling if there is NA

# Data pre-processing
# Data Processing 1: Remove zero values, maybe 
# Data Processing 2: Remove or make them positive
# Data Processing 3: Remove NAs or perform Data Wrangling