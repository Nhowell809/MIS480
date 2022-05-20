#!/usr/bin/env python
# coding: utf-8

# In[218]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('seaborn-whitegrid')

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split 
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, GRU, Bidirectional
from keras.optimizers import SGD
import math
from sklearn.metrics import mean_squared_error


# In[219]:


def return_rmse(test,predicted):
    rmse = math.sqrt(mean_squared_error(test, predicted))
    print("The root mean squared error is {}.".format(rmse))


# In[220]:


import os
import os.path
import glob


# In[221]:


file = "C:\\Users\\Nhowell.KUMAR\\Desktop\\Data"
trucknumberdir = os.listdir(file)


# In[222]:


trucklist = []

for file in trucknumberdir:
    trucknumber = file.split("_")[0]
    if trucknumber != "all":
        trucklist.append(trucknumber)
        
print(trucklist)


# In[235]:


trucklist = ['160', '174', '179', '184', '185', '186', '187', '190', '191', '192', '193', '194', '198', '200', '203', '204', 
             '205', '207', '209', '212', '213', '216', '217', '218', '221', '222', '223', '225', '227', '228', '229', '230',  
             '233', '234', '235', '236', '237', '240', '241', '242', '243', '244', '245', '246', '248', '249', '250', '251', 
             '252', '738', '739', '740', '741', '743', '745', '746']
df_ = {}

for i in trucklist:
    df_[i] = pd.read_csv("C:\\Users\\Nhowell.KUMAR\\Desktop\\Trucks.csv", index_col = "Week_Ending", 
                         parse_dates = ["Week_Ending"])
    
df_[i].head()    


# In[236]:


def split(dataframe, border, col):
    return dataframe.loc[:border,col], dataframe.loc[border:,col]

df_new = {}

for i in trucklist:
    df_new[i] = {}
    df_new[i]["Train"], df_new[i]["Test"] = split(df_[i], "2022-02-05", "Total_Miles")


# In[237]:


for i in trucklist:
    plt.figure(figsize=(15,5))
    plt.plot(df_new[i]["Train"])
    plt.plot(df_new[i]["Test"])
    plt.ylabel("Total_Miles")
    plt.xlabel("Week_Ending")
    plt.legend(["Training Set", "Test Set"])
    plt.title("Truck " + i + " Total Miles Driven")


# In[179]:





# In[181]:





# In[182]:





# In[ ]:


trucklist = ['160', '174', '179', '184', '185', '186', '187', '190', '191', '192', '193', '194', '198', '200', '203', '204', 
             '205', '207', '209', '212', '213', '216', '217', '218', '221', '222', '223', '225', '227', '228', '229', '230',  
             '233', '234', '235', '236', '237', '240', '241', '242', '243', '244', '245', '246', '248', '249', '250', '251', 
             '252', '738', '739', '740', '741', '743', '745', '746']

