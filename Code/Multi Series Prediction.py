#!/usr/bin/env python
# coding: utf-8

# In[43]:


# Import of various libraries: pandas, numpy, matplotlib, warnings, scikit-learn (sklearn), lightgbm, datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')
from sklearn.metrics import mean_squared_log_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from lightgbm import LGBMRegressor
from datetime import date, timedelta


# In[44]:


# import of 55 data frames. df = dataframe, numeric value following df = truck number.

df160 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\160_Truck.csv")
df174 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\174_Truck.csv")
df179 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\179_Truck.csv")
df184 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\184_Truck.csv")
df185 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\185_Truck.csv")
df186 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\186_Truck.csv")
df187 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\187_Truck.csv")
df190 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\190_Truck.csv")
df191 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\191_Truck.csv")
df192 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\192_Truck.csv")
df193 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\193_Truck.csv")
df195 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\195_Truck.csv")
df198 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\198_Truck.csv")
df200 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\200_Truck.csv")
df203 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\203_Truck.csv")
df204 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\204_Truck.csv")
df205 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\205_Truck.csv")
df207 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\207_Truck.csv")
df209 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\209_Truck.csv")
df212 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\212_Truck.csv")
df213 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\213_Truck.csv")
df216 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\216_Truck.csv")
df217 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\217_Truck.csv")
df218 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\218_Truck.csv")
df221 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\221_Truck.csv")
df222 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\222_Truck.csv")
df223 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\223_Truck.csv")
df225 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\225_Truck.csv")
df227 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\227_Truck.csv")
df228 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\228_Truck.csv")
df229 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\229_Truck.csv")
df230 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\230_Truck.csv")
df233 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\233_Truck.csv")
df234 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\234_Truck.csv")
df235 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\235_Truck.csv")
df236 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\236_Truck.csv")
df237 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\237_Truck.csv")
df240 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\240_Truck.csv")
df241 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\241_Truck.csv")
df242 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\242_Truck.csv")
df243 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\243_Truck.csv")
df244 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\244_Truck.csv")
df245 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\245_Truck.csv")
df246 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\246_Truck.csv")
df248 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\248_Truck.csv")
df249 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\249_Truck.csv")
df250 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\250_Truck.csv")
df251 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\251_Truck.csv")
df252 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\252_Truck.csv")
df738 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\738_Truck.csv")
df739 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\739_Truck.csv")
df740 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\740_Truck.csv")
df741 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\741_Truck.csv")
df743 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\743_Truck.csv")
df746 = pd.read_csv("C:\\Users\\Nrhow\\OneDrive\\Desktop\\Data\\Data\\746_Truck.csv")


# In[45]:


# I really need to learn how to do loops with dataframes...
# print the missing values for each dataset -- I knew what weeks I collected 
# data for and included those weeks in the creation of the CSV documents. 
# So, I should only have missing values for Ending_Mileage. 

print("Truck Data Frame 160 Missing Values: " , (df160.isnull().sum()))
print("Truck Data Frame 174 Missing Values: " , (df174.isnull().sum()))
print("Truck Data Frame 179 Missing Values: " , (df179.isnull().sum()))
print("Truck Data Frame 184 Missing Values: " , (df184.isnull().sum()))
print("Truck Data Frame 185 Missing Values: " , (df185.isnull().sum()))
print("Truck Data Frame 186 Missing Values: " , (df186.isnull().sum()))
print("Truck Data Frame 187 Missing Values: " , (df187.isnull().sum()))
print("Truck Data Frame 190 Missing Values: " , (df190.isnull().sum()))
print("Truck Data Frame 191 Missing Values: " , (df191.isnull().sum()))
print("Truck Data Frame 192 Missing Values: " , (df192.isnull().sum()))
print("Truck Data Frame 193 Missing Values: " , (df193.isnull().sum()))
print("Truck Data Frame 195 Missing Values: " , (df195.isnull().sum()))
print("Truck Data Frame 198 Missing Values: " , (df198.isnull().sum()))
print("Truck Data Frame 200 Missing Values: " , (df200.isnull().sum()))
print("Truck Data Frame 203 Missing Values: " , (df203.isnull().sum()))
print("Truck Data Frame 204 Missing Values: " , (df204.isnull().sum()))
print("Truck Data Frame 205 Missing Values: " , (df205.isnull().sum()))
print("Truck Data Frame 207 Missing Values: " , (df207.isnull().sum()))
print("Truck Data Frame 209 Missing Values: " , (df209.isnull().sum()))
print("Truck Data Frame 212 Missing Values: " , (df212.isnull().sum()))
print("Truck Data Frame 213 Missing Values: " , (df213.isnull().sum()))
print("Truck Data Frame 216 Missing Values: " , (df216.isnull().sum()))
print("Truck Data Frame 217 Missing Values: " , (df217.isnull().sum()))
print("Truck Data Frame 218 Missing Values: " , (df218.isnull().sum()))
print("Truck Data Frame 221 Missing Values: " , (df221.isnull().sum()))
print("Truck Data Frame 222 Missing Values: " , (df222.isnull().sum()))
print("Truck Data Frame 223 Missing Values: " , (df223.isnull().sum()))
print("Truck Data Frame 225 Missing Values: " , (df225.isnull().sum()))
print("Truck Data Frame 227 Missing Values: " , (df227.isnull().sum()))
print("Truck Data Frame 228 Missing Values: " , (df228.isnull().sum()))
print("Truck Data Frame 229 Missing Values: " , (df229.isnull().sum()))
print("Truck Data Frame 230 Missing Values: " , (df230.isnull().sum()))
print("Truck Data Frame 233 Missing Values: " , (df233.isnull().sum()))
print("Truck Data Frame 234 Missing Values: " , (df234.isnull().sum()))
print("Truck Data Frame 235 Missing Values: " , (df235.isnull().sum()))
print("Truck Data Frame 236 Missing Values: " , (df236.isnull().sum()))
print("Truck Data Frame 237 Missing Values: " , (df237.isnull().sum()))
print("Truck Data Frame 240 Missing Values: " , (df240.isnull().sum()))
print("Truck Data Frame 241 Missing Values: " , (df241.isnull().sum()))
print("Truck Data Frame 242 Missing Values: " , (df242.isnull().sum()))
print("Truck Data Frame 243 Missing Values: " , (df243.isnull().sum()))
print("Truck Data Frame 244 Missing Values: " , (df244.isnull().sum()))
print("Truck Data Frame 245 Missing Values: " , (df245.isnull().sum()))
print("Truck Data Frame 246 Missing Values: " , (df246.isnull().sum()))
print("Truck Data Frame 248 Missing Values: " , (df248.isnull().sum()))
print("Truck Data Frame 249 Missing Values: " , (df249.isnull().sum()))
print("Truck Data Frame 250 Missing Values: " , (df250.isnull().sum()))
print("Truck Data Frame 251 Missing Values: " , (df251.isnull().sum()))
print("Truck Data Frame 252 Missing Values: " , (df252.isnull().sum()))
print("Truck Data Frame 738 Missing Values: " , (df738.isnull().sum()))
print("Truck Data Frame 739 Missing Values: " , (df739.isnull().sum())) 
print("Truck Data Frame 740 Missing Values: " , (df740.isnull().sum()))
print("Truck Data Frame 741 Missing Values: " , (df741.isnull().sum()))
print("Truck Data Frame 743 Missing Values: " , (df743.isnull().sum()))
print("Truck Data Frame 746 Missing Values: " , (df746.isnull().sum()))


# In[46]:


# convert Week_ending from dtype int64 to datetime64[ns]

df160["Week_Ending"] = df160["Week_Ending"].astype('datetime64[ns]')

df174["Week_Ending"] = df174["Week_Ending"].astype('datetime64[ns]')

df179["Week_Ending"] = df179["Week_Ending"].astype('datetime64[ns]')

df184["Week_Ending"] = df184["Week_Ending"].astype('datetime64[ns]')

df185["Week_Ending"] = df185["Week_Ending"].astype('datetime64[ns]')

df186["Week_Ending"] = df186["Week_Ending"].astype('datetime64[ns]')

df187["Week_Ending"] = df187["Week_Ending"].astype('datetime64[ns]')

df190["Week_Ending"] = df190["Week_Ending"].astype('datetime64[ns]')

df191["Week_Ending"] = df191["Week_Ending"].astype('datetime64[ns]')

df192["Week_Ending"] = df192["Week_Ending"].astype('datetime64[ns]')

df193["Week_Ending"] = df193["Week_Ending"].astype('datetime64[ns]')

df195["Week_Ending"] = df195["Week_Ending"].astype('datetime64[ns]')

df198["Week_Ending"] = df198["Week_Ending"].astype('datetime64[ns]')

df200["Week_Ending"] = df200["Week_Ending"].astype('datetime64[ns]')

df203["Week_Ending"] = df203["Week_Ending"].astype('datetime64[ns]')

df204["Week_Ending"] = df204["Week_Ending"].astype('datetime64[ns]')

df205["Week_Ending"] = df205["Week_Ending"].astype('datetime64[ns]')

df207["Week_Ending"] = df207["Week_Ending"].astype('datetime64[ns]')

df209["Week_Ending"] = df209["Week_Ending"].astype('datetime64[ns]')

df212["Week_Ending"] = df212["Week_Ending"].astype('datetime64[ns]')

df213["Week_Ending"] = df213["Week_Ending"].astype('datetime64[ns]')

df216["Week_Ending"] = df216["Week_Ending"].astype('datetime64[ns]')

df217["Week_Ending"] = df217["Week_Ending"].astype('datetime64[ns]')

df218["Week_Ending"] = df218["Week_Ending"].astype('datetime64[ns]')

df221["Week_Ending"] = df221["Week_Ending"].astype('datetime64[ns]')

df222["Week_Ending"] = df222["Week_Ending"].astype('datetime64[ns]')

df223["Week_Ending"] = df223["Week_Ending"].astype('datetime64[ns]')

df225["Week_Ending"] = df225["Week_Ending"].astype('datetime64[ns]')

df227["Week_Ending"] = df227["Week_Ending"].astype('datetime64[ns]')

df228["Week_Ending"] = df228["Week_Ending"].astype('datetime64[ns]')

df229["Week_Ending"] = df229["Week_Ending"].astype('datetime64[ns]')

df230["Week_Ending"] = df230["Week_Ending"].astype('datetime64[ns]')

df233["Week_Ending"] = df233["Week_Ending"].astype('datetime64[ns]')

df234["Week_Ending"] = df234["Week_Ending"].astype('datetime64[ns]')

df235["Week_Ending"] = df235["Week_Ending"].astype('datetime64[ns]')

df236["Week_Ending"] = df236["Week_Ending"].astype('datetime64[ns]')

df237["Week_Ending"] = df237["Week_Ending"].astype('datetime64[ns]')

df240["Week_Ending"] = df240["Week_Ending"].astype('datetime64[ns]')

df241["Week_Ending"] = df241["Week_Ending"].astype('datetime64[ns]')

df242["Week_Ending"] = df242["Week_Ending"].astype('datetime64[ns]')

df243["Week_Ending"] = df243["Week_Ending"].astype('datetime64[ns]')

df244["Week_Ending"] = df244["Week_Ending"].astype('datetime64[ns]')

df245["Week_Ending"] = df245["Week_Ending"].astype('datetime64[ns]')

df246["Week_Ending"] = df246["Week_Ending"].astype('datetime64[ns]')

df248["Week_Ending"] = df248["Week_Ending"].astype('datetime64[ns]')

df249["Week_Ending"] = df249["Week_Ending"].astype('datetime64[ns]')

df250["Week_Ending"] = df250["Week_Ending"].astype('datetime64[ns]')

df251["Week_Ending"] = df251["Week_Ending"].astype('datetime64[ns]')

df252["Week_Ending"] = df252["Week_Ending"].astype('datetime64[ns]')

df738["Week_Ending"] = df738["Week_Ending"].astype('datetime64[ns]')

df739["Week_Ending"] = df739["Week_Ending"].astype('datetime64[ns]')

df740["Week_Ending"] = df740["Week_Ending"].astype('datetime64[ns]')

df741["Week_Ending"] = df741["Week_Ending"].astype('datetime64[ns]')

df743["Week_Ending"] = df743["Week_Ending"].astype('datetime64[ns]')

df746["Week_Ending"] = df746["Week_Ending"].astype('datetime64[ns]')


# In[47]:


# I need to fill in the missing data from the Ending_mileage sections. 
# For all the datasets I have a starting mileage and and ending mileage
# those points are not necessarily the first and last week of the data
# Initially, I used a linear regression for each dataset to predict the
# missing values, but for some reason the numbers weren't progressing
# linearly. So, I switched to linear interpolation, because it simply 
# takes the two points (start, end) and connect those points with a 
# straight line. It can then identify an estimation between the points
# to fill in the missing mileage. Since this continues in a true linear
# progression, the mileage may not be precise but should be accurate. In
# an ideal solution the prediction would be both accurate and precise. 

new_df160 = df160["Ending_Mileage"].interpolate(method = 'linear')
new_df174 = df174["Ending_Mileage"].interpolate(method = 'linear')
new_df179 = df179["Ending_Mileage"].interpolate(method = 'linear')
new_df184 = df184["Ending_Mileage"].interpolate(method = 'linear')
new_df185 = df185["Ending_Mileage"].interpolate(method = 'linear')
new_df186 = df186["Ending_Mileage"].interpolate(method = 'linear')
new_df187 = df187["Ending_Mileage"].interpolate(method = 'linear')
new_df190 = df190["Ending_Mileage"].interpolate(method = 'linear')
new_df191 = df191["Ending_Mileage"].interpolate(method = 'linear')
new_df192 = df192["Ending_Mileage"].interpolate(method = 'linear')
new_df193 = df193["Ending_Mileage"].interpolate(method = 'linear')
new_df195 = df195["Ending_Mileage"].interpolate(method = 'linear')
new_df198 = df198["Ending_Mileage"].interpolate(method = 'linear')
new_df200 = df200["Ending_Mileage"].interpolate(method = 'linear')
new_df203 = df203["Ending_Mileage"].interpolate(method = 'linear')
new_df204 = df204["Ending_Mileage"].interpolate(method = 'linear')
new_df205 = df205["Ending_Mileage"].interpolate(method = 'linear')
new_df207 = df207["Ending_Mileage"].interpolate(method = 'linear')
new_df209 = df209["Ending_Mileage"].interpolate(method = 'linear')
new_df212 = df212["Ending_Mileage"].interpolate(method = 'linear')
new_df213 = df213["Ending_Mileage"].interpolate(method = 'linear')
new_df216 = df216["Ending_Mileage"].interpolate(method = 'linear')
new_df217 = df217["Ending_Mileage"].interpolate(method = 'linear')
new_df218 = df218["Ending_Mileage"].interpolate(method = 'linear')
new_df221 = df221["Ending_Mileage"].interpolate(method = 'linear')
new_df222 = df222["Ending_Mileage"].interpolate(method = 'linear')
new_df223 = df223["Ending_Mileage"].interpolate(method = 'linear')
new_df225 = df225["Ending_Mileage"].interpolate(method = 'linear')
new_df227 = df227["Ending_Mileage"].interpolate(method = 'linear')
new_df228 = df228["Ending_Mileage"].interpolate(method = 'linear')
new_df229 = df229["Ending_Mileage"].interpolate(method = 'linear')
new_df230 = df230["Ending_Mileage"].interpolate(method = 'linear')
new_df233 = df233["Ending_Mileage"].interpolate(method = 'linear')
new_df234 = df234["Ending_Mileage"].interpolate(method = 'linear')
new_df235 = df235["Ending_Mileage"].interpolate(method = 'linear')
new_df236 = df236["Ending_Mileage"].interpolate(method = 'linear')
new_df237 = df237["Ending_Mileage"].interpolate(method = 'linear')
new_df240 = df240["Ending_Mileage"].interpolate(method = 'linear')
new_df241 = df241["Ending_Mileage"].interpolate(method = 'linear')
new_df242 = df242["Ending_Mileage"].interpolate(method = 'linear')
new_df243 = df243["Ending_Mileage"].interpolate(method = 'linear')
new_df244 = df244["Ending_Mileage"].interpolate(method = 'linear')
new_df245 = df245["Ending_Mileage"].interpolate(method = 'linear')
new_df246 = df246["Ending_Mileage"].interpolate(method = 'linear')
new_df248 = df248["Ending_Mileage"].interpolate(method = 'linear')
new_df249 = df249["Ending_Mileage"].interpolate(method = 'linear')
new_df250 = df250["Ending_Mileage"].interpolate(method = 'linear')
new_df251 = df251["Ending_Mileage"].interpolate(method = 'linear')
new_df252 = df252["Ending_Mileage"].interpolate(method = 'linear')
new_df738 = df738["Ending_Mileage"].interpolate(method = 'linear')
new_df739 = df739["Ending_Mileage"].interpolate(method = 'linear')
new_df740 = df740["Ending_Mileage"].interpolate(method = 'linear')
new_df741 = df741["Ending_Mileage"].interpolate(method = 'linear')
new_df743 = df743["Ending_Mileage"].interpolate(method = 'linear')
new_df746 = df746["Ending_Mileage"].interpolate(method = 'linear')


# In[48]:


# the following series of code is for combining the initial dataframes with the interpolated dataframes. 
# first create a blank list for the dataframe. Then using a for in loop we are trying to say
# for data [i] in our interpolated dataframe iterate through the list and 
# add the interpolated data to the list. 
#Print the list. Printing the list was more for me to check where I was. 
# Next, we are over-writing the new_dfxxx to turn our list into a dataframe. 
# I named this new column Pred_Ending_Mileage short for Predicted. 
# Then we overwrite our initial dataframe, dfxxx and concatenate the 
# initial dataframe and the dataframe with the predicted ending mileage. 
# I used reindexing using the initial index of the dataframe. 

list_df160 = []
for i in new_df160:
    list_df160.append(i)
print(list_df160)
new_df160 = pd.DataFrame(list_df160, columns = ['Pred_Ending_Mileage'])
df160 = pd.concat([df160, new_df160], axis =1).reindex(df160.index)
                                                       
list_df174 = []
for i in new_df174:
    list_df174.append(i)
print(list_df174)
new_df174 = pd.DataFrame(list_df174, columns = ['Pred_Ending_Mileage'])
df174 = pd.concat([df174, new_df174], axis =1).reindex(df174.index)
                                                       
list_df179 = []
for i in new_df179:
    list_df179.append(i)
print(list_df179)
new_df179 = pd.DataFrame(list_df179, columns = ['Pred_Ending_Mileage'])
df179 = pd.concat([df179, new_df179], axis =1).reindex(df179.index)
                                                       
list_df184 = []
for i in new_df184:
    list_df184.append(i)
print(list_df184)
new_df184 = pd.DataFrame(list_df184, columns = ['Pred_Ending_Mileage'])
df184 = pd.concat([df184, new_df184], axis =1).reindex(df184.index)
                                                       
list_df185 = []
for i in new_df185:
    list_df185.append(i)
print(list_df185)
new_df185 = pd.DataFrame(list_df185, columns = ['Pred_Ending_Mileage'])
df185 = pd.concat([df185, new_df185], axis =1).reindex(df185.index)
                                                       
list_df186 = []
for i in new_df186:
    list_df186.append(i)
print(list_df186)
new_df186 = pd.DataFrame(list_df186, columns = ['Pred_Ending_Mileage'])
df186 = pd.concat([df186, new_df186], axis =1).reindex(df186.index)
                                                       
list_df187 = []
for i in new_df187:
    list_df187.append(i)
print(list_df187)
new_df187 = pd.DataFrame(list_df187, columns = ['Pred_Ending_Mileage'])
df187 = pd.concat([df187, new_df187], axis =1).reindex(df187.index)
                                                       
list_df190 = []
for i in new_df190:
    list_df190.append(i)
print(list_df190)
new_df190 = pd.DataFrame(list_df190, columns = ['Pred_Ending_Mileage'])
df190 = pd.concat([df190, new_df190], axis =1).reindex(df190.index)
                                                       
list_df191 = []
for i in new_df191:
    list_df191.append(i)
print(list_df191)
new_df191 = pd.DataFrame(list_df191, columns = ['Pred_Ending_Mileage'])
df191 = pd.concat([df191, new_df191], axis =1).reindex(df191.index)
                                                       
list_df192 = []
for i in new_df192:
    list_df192.append(i)
print(list_df192)
new_df192 = pd.DataFrame(list_df192, columns = ['Pred_Ending_Mileage'])
df192 = pd.concat([df192, new_df192], axis =1).reindex(df192.index)
                                                                             
list_df193 = []
for i in new_df193:
    list_df193.append(i)
print(list_df193)
new_df193 = pd.DataFrame(list_df193, columns = ['Pred_Ending_Mileage'])
df193 = pd.concat([df193, new_df193], axis =1).reindex(df193.index)
                                                                             
list_df195 = []
for i in new_df195:
    list_df195.append(i)
print(list_df195)
new_df195 = pd.DataFrame(list_df195, columns = ['Pred_Ending_Mileage'])
df195 = pd.concat([df195, new_df195], axis =1).reindex(df195.index)
                                                                            
list_df198 = []
for i in new_df198:
    list_df198.append(i)
print(list_df198)
new_df198 = pd.DataFrame(list_df198, columns = ['Pred_Ending_Mileage'])
df198 = pd.concat([df198, new_df198], axis =1).reindex(df198.index)
                                                                             
list_df200 = []
for i in new_df200:
    list_df200.append(i)
print(list_df200)
new_df200 = pd.DataFrame(list_df200, columns = ['Pred_Ending_Mileage'])
df200 = pd.concat([df200, new_df200], axis =1).reindex(df200.index)
                                                                             
list_df203 = []
for i in new_df203:
    list_df203.append(i)
print(list_df203)
new_df203 = pd.DataFrame(list_df203, columns = ['Pred_Ending_Mileage'])
df203 = pd.concat([df203, new_df203], axis =1).reindex(df203.index)
                                                                             
list_df204 = []
for i in new_df204:
    list_df204.append(i)
print(list_df204)
new_df204 = pd.DataFrame(list_df204, columns = ['Pred_Ending_Mileage'])
df204 = pd.concat([df204, new_df204], axis =1).reindex(df204.index)
                                                                             
list_df205 = []
for i in new_df205:
    list_df205.append(i)
print(list_df205)
new_df205 = pd.DataFrame(list_df205, columns = ['Pred_Ending_Mileage'])
df205 = pd.concat([df205, new_df205], axis =1).reindex(df205.index)
                                                                             
list_df207 = []
for i in new_df207:
    list_df207.append(i)
print(list_df207)
new_df207 = pd.DataFrame(list_df207, columns = ['Pred_Ending_Mileage'])
df207 = pd.concat([df207, new_df207], axis =1).reindex(df207.index)
                                                                             
list_df209 = []
for i in new_df209:
    list_df209.append(i)
print(list_df209)
new_df209 = pd.DataFrame(list_df209, columns = ['Pred_Ending_Mileage'])
df209 = pd.concat([df209, new_df209], axis =1).reindex(df209.index)
                                                                             
list_df212 = []
for i in new_df212:
    list_df212.append(i)
print(list_df212)
new_df212 = pd.DataFrame(list_df212, columns = ['Pred_Ending_Mileage'])
df212 = pd.concat([df212, new_df212], axis =1).reindex(df212.index)
                                                                             
list_df213 = []
for i in new_df213:
    list_df213.append(i)
print(list_df213)
new_df213 = pd.DataFrame(list_df213, columns = ['Pred_Ending_Mileage'])
df213 = pd.concat([df213, new_df213], axis =1).reindex(df213.index)
                                                                             
list_df216 = []
for i in new_df216:
    list_df216.append(i)
print(list_df216)
new_df216 = pd.DataFrame(list_df216, columns = ['Pred_Ending_Mileage'])
df216 = pd.concat([df216, new_df216], axis =1).reindex(df216.index)
                                                                            
list_df217 = []
for i in new_df217:
    list_df217.append(i)
print(list_df217)
new_df217 = pd.DataFrame(list_df217, columns = ['Pred_Ending_Mileage'])
df217 = pd.concat([df217, new_df217], axis =1).reindex(df217.index)
                                                                             
list_df218 = []
for i in new_df218:
    list_df218.append(i)
print(list_df218)
new_df218 = pd.DataFrame(list_df218, columns = ['Pred_Ending_Mileage'])
df218 = pd.concat([df218, new_df218], axis =1).reindex(df218.index)
                                                                             
list_df221 = []
for i in new_df221:
    list_df221.append(i)
print(list_df221)
new_df221 = pd.DataFrame(list_df221, columns = ['Pred_Ending_Mileage'])
df221 = pd.concat([df221, new_df221], axis =1).reindex(df221.index)
                                                                             
list_df222 = []
for i in new_df222:
    list_df222.append(i)
print(list_df222)
new_df222 = pd.DataFrame(list_df222, columns = ['Pred_Ending_Mileage'])
df222 = pd.concat([df222, new_df222], axis =1).reindex(df222.index)
                                                                             
list_df223 = []
for i in new_df223:
    list_df223.append(i)
print(list_df223)
new_df223 = pd.DataFrame(list_df223, columns = ['Pred_Ending_Mileage'])
df223 = pd.concat([df223, new_df223], axis =1).reindex(df223.index)
                                                                            
list_df225 = []
for i in new_df225:
    list_df225.append(i)
print(list_df225)
new_df225 = pd.DataFrame(list_df225, columns = ['Pred_Ending_Mileage'])
df225 = pd.concat([df225, new_df225], axis =1).reindex(df225.index)
                                                                             
list_df227 = []
for i in new_df227:
    list_df227.append(i)
print(list_df227)
new_df227 = pd.DataFrame(list_df227, columns = ['Pred_Ending_Mileage'])
df227 = pd.concat([df227, new_df227], axis =1).reindex(df227.index)
                                                                             
list_df228 = []
for i in new_df228:
    list_df228.append(i)
print(list_df228)
new_df228 = pd.DataFrame(list_df228, columns = ['Pred_Ending_Mileage'])
df228 = pd.concat([df228, new_df228], axis =1).reindex(df228.index)
                                                                             
list_df229 = []
for i in new_df229:
    list_df229.append(i)
print(list_df229)
new_df229 = pd.DataFrame(list_df229, columns = ['Pred_Ending_Mileage'])
df229 = pd.concat([df229, new_df229], axis =1).reindex(df229.index)
                      
list_df230 = []
for i in new_df230:
    list_df230.append(i)
print(list_df230)
new_df230 = pd.DataFrame(list_df230, columns = ['Pred_Ending_Mileage'])
df230 = pd.concat([df230, new_df230], axis =1).reindex(df230.index)
                                                                             
list_df233 = []
for i in new_df233:
    list_df233.append(i)
print(list_df233)
new_df233 = pd.DataFrame(list_df233, columns = ['Pred_Ending_Mileage'])
df233 = pd.concat([df233, new_df233], axis =1).reindex(df233.index)
                      
list_df234 = []
for i in new_df234:
    list_df234.append(i)
print(list_df234)
new_df234 = pd.DataFrame(list_df234, columns = ['Pred_Ending_Mileage'])
df234 = pd.concat([df234, new_df234], axis =1).reindex(df234.index)
                                                                             
list_df235 = []
for i in new_df235:
    list_df235.append(i)
print(list_df235)
new_df235 = pd.DataFrame(list_df235, columns = ['Pred_Ending_Mileage'])
df235 = pd.concat([df235, new_df235], axis =1).reindex(df235.index)
                                                                             
list_df236 = []
for i in new_df236:
    list_df236.append(i)
print(list_df236)
new_df236 = pd.DataFrame(list_df236, columns = ['Pred_Ending_Mileage'])
df236 = pd.concat([df236, new_df236], axis =1).reindex(df236.index)
                                                                             
list_df237 = []
for i in new_df237:
    list_df237.append(i)
print(list_df237)
new_df237 = pd.DataFrame(list_df237, columns = ['Pred_Ending_Mileage'])
df237 = pd.concat([df237, new_df237], axis =1).reindex(df237.index)
                                                                             
list_df240 = []
for i in new_df240:
    list_df240.append(i)
print(list_df240)
new_df240 = pd.DataFrame(list_df240, columns = ['Pred_Ending_Mileage'])
df240 = pd.concat([df240, new_df240], axis =1).reindex(df240.index)
                                                                             
list_df241 = []
for i in new_df241:
    list_df241.append(i)
print(list_df241)
new_df241 = pd.DataFrame(list_df241, columns = ['Pred_Ending_Mileage'])
df241 = pd.concat([df241, new_df241], axis =1).reindex(df241.index)
                                                                             
list_df242 = []
for i in new_df242:
    list_df242.append(i)
print(list_df242)
new_df242 = pd.DataFrame(list_df242, columns = ['Pred_Ending_Mileage'])
df242 = pd.concat([df242, new_df242], axis =1).reindex(df242.index)
                                                                             
list_df243 = []
for i in new_df243:
    list_df243.append(i)
print(list_df243)
new_df243 = pd.DataFrame(list_df243, columns = ['Pred_Ending_Mileage'])
df243 = pd.concat([df243, new_df243], axis =1).reindex(df243.index)
                                                                             
list_df244 = []
for i in new_df244:
    list_df244.append(i)
print(list_df244)
new_df244 = pd.DataFrame(list_df244, columns = ['Pred_Ending_Mileage'])
df244 = pd.concat([df244, new_df244], axis =1).reindex(df244.index)
                                                                             
list_df245 = []
for i in new_df245:
    list_df245.append(i)
print(list_df245)
new_df245 = pd.DataFrame(list_df245, columns = ['Pred_Ending_Mileage'])
df245 = pd.concat([df245, new_df245], axis =1).reindex(df245.index)
                                                                             
list_df246 = []
for i in new_df246:
    list_df246.append(i)
print(list_df246)
new_df246 = pd.DataFrame(list_df246, columns = ['Pred_Ending_Mileage'])
df246 = pd.concat([df246, new_df246], axis =1).reindex(df246.index)
                                                                             
list_df248 = []
for i in new_df248:
    list_df248.append(i)
print(list_df248)
new_df248 = pd.DataFrame(list_df248, columns = ['Pred_Ending_Mileage'])
df248 = pd.concat([df248, new_df248], axis =1).reindex(df248.index)
                                                                             
list_df249 = []
for i in new_df249:
    list_df249.append(i)
print(list_df249)
new_df249 = pd.DataFrame(list_df249, columns = ['Pred_Ending_Mileage'])
df249 = pd.concat([df249, new_df249], axis =1).reindex(df249.index)
                                                                             
list_df250 = []
for i in new_df250:
    list_df250.append(i)
print(list_df250)
new_df250 = pd.DataFrame(list_df250, columns = ['Pred_Ending_Mileage'])
df250 = pd.concat([df250, new_df250], axis =1).reindex(df250.index)
                                                                             
list_df251 = []
for i in new_df251:
    list_df251.append(i)
print(list_df251)
new_df251 = pd.DataFrame(list_df251, columns = ['Pred_Ending_Mileage'])
df251 = pd.concat([df251, new_df251], axis =1).reindex(df251.index)
                                                                             
list_df252 = []
for i in new_df252:
    list_df252.append(i)
print(list_df252)
new_df252 = pd.DataFrame(list_df252, columns = ['Pred_Ending_Mileage'])
df252 = pd.concat([df252, new_df252], axis =1).reindex(df252.index)
                                                                             
list_df738 = []
for i in new_df738:
    list_df738.append(i)
print(list_df738)
new_df738 = pd.DataFrame(list_df738, columns = ['Pred_Ending_Mileage'])
df738 = pd.concat([df738, new_df738], axis =1).reindex(df738.index)
                                                                             
list_df739 = []
for i in new_df739:
    list_df739.append(i)
print(list_df739)
new_df739 = pd.DataFrame(list_df739, columns = ['Pred_Ending_Mileage'])
df739 = pd.concat([df739, new_df739], axis =1).reindex(df739.index)
                                                                             
list_df740 = []
for i in new_df740:
    list_df740.append(i)
print(list_df740)
new_df740 = pd.DataFrame(list_df740, columns = ['Pred_Ending_Mileage'])
df740 = pd.concat([df740, new_df740], axis =1).reindex(df740.index)
                                                                             
list_df741 = []
for i in new_df741:
    list_df741.append(i)
print(list_df741)
new_df741 = pd.DataFrame(list_df741, columns = ['Pred_Ending_Mileage'])
df741 = pd.concat([df741, new_df741], axis =1).reindex(df741.index)
                      
list_df743 = []
for i in new_df743:
    list_df743.append(i)
print(list_df743)
new_df743 = pd.DataFrame(list_df743, columns = ['Pred_Ending_Mileage'])
df743 = pd.concat([df743, new_df743], axis =1).reindex(df743.index)
                  
list_df746 = []
for i in new_df746:
    list_df746.append(i)
print(list_df746)
new_df746 = pd.DataFrame(list_df746, columns = ['Pred_Ending_Mileage'])
df746 = pd.concat([df746, new_df746], axis =1).reindex(df746.index)


# In[49]:


bigdf = pd.concat([df160, df174, df179, df184, df185, df186, df187, df190, df191, df192, df193, 
                   df195, df198, df200, df203, df204, df205, df207, df209, df212, df213, df216, df217, 
                   df218, df221, df222, df223, df225, df227, df228, df229, df230, df233, df234, df235, 
                   df236, df237, df240, df241, df242, df243, df244, df245, df246, df248, df249, df250, 
                   df251, df252, df738, df739 , df740, df741, df743, df746], axis = 0)

bigdf.head()
bigdf.to_csv("bigdf.csv")


# In[50]:


# Clean up, Clean up, everyone do you share...
# say goodbye to Ending Mileage. Pred Ending Mileage can replace
# Ending Mileage now. 

bigdf = bigdf.drop(columns = "Ending_Mileage")
bigdf


# In[51]:


# Now to get into the nitty gritty. 
# The goal is to essentially use time series forcasting to determine
# when each truck will hit 200,000 miles to aid in identification
# of fleet turn-over. 
# Time series forcasting often uses previous week [variable], and previous 
# week difference in [variable]. To do this, I copied the bigdf to create
# bigdf2. Creative, I am. The two features we just talked about need to be
# added in. So we call bigdf2 and insert a new column called 
# Miles_Driven_Last_Week. To fill this column in we group our data
# by the vehicle by looking at the Pred Ending Miles column, and then shift 
# that row down the respective period (1 week). So Miles driver in week 3
# are shifted to week 4. 
# Then I added the columns for last weeks difference in miles driven by grouping by
# Vehicle, and using the diff() command to calculate the difference between
# columns for Miles Driven last week and miles driven for the current week. 
# dropna is used to drop any blank value points. 
# I popped out the column Week_Ending for the next series of code.

bigdf2 = bigdf.copy()
bigdf2["Miles_Driven_Last_Week"] = bigdf2.groupby(["Vehicle"])["Pred_Ending_Mileage"].shift()
bigdf2["Last_Week_Diff_Miles"] = bigdf2.groupby(["Vehicle"])["Miles_Driven_Last_Week"].diff()
bigdf2 = bigdf2.dropna()
Week_Ending = bigdf2.pop("Week_Ending")
bigdf2


# In[52]:


# Models are prone to error. So, I am going to use Root Mean Square Error
# to calculate the error. This error metric is the square for ALL error present.
# The below will calculate the percentage of error from our model(s) and
# output target. (ytrue vs ypred)

def rmsle(ytrue, ypred):
    return np.sqrt(mean_squared_log_error(ytrue, ypred))


# In[53]:


train, test = train_test_split(bigdf2, test_size = .30, random_state = 25)


# In[54]:


mean_error = []
for index in range(17,30):
    train = train[train["Week_Index"] < index]
    val = test[test["Week_Index"] == index]
    
    
    p = val["Miles_Driven_Last_Week"].values
    
    error = rmsle(val["Pred_Ending_Mileage"].values, p)
    print("Week %d - Error %.5f" % (index, error))
    mean_error.append(error)

print("Mean Error = %.5f" % np.mean(mean_error))


# In[55]:



mean_error = []
for index in range(17,30):
    train = train[train["Week_Index"] < index]
    val = test[test["Week_Index"] == index]
    
    xtr, xts = train.drop(['Pred_Ending_Mileage'], axis = 1), val.drop(["Pred_Ending_Mileage"], axis = 1)
    
    ytr, yts = train["Pred_Ending_Mileage"].values, val["Pred_Ending_Mileage"].values
    
    mdl1 = RandomForestRegressor(n_estimators = 1000,  n_jobs = -1, 
                               random_state = 0)
    mdl1.fit(xtr, ytr)
    
    p = val["Miles_Driven_Last_Week"].values
    
    error = rmsle(val["Pred_Ending_Mileage"].values, p)
    print("Week %d - Error %.5f" % (index, error))
    mean_error.append(error)

print("Mean Error = %.5f" % np.mean(mean_error))


# In[56]:


bigdf3 = bigdf.copy()
bigdf3["Miles_Driven_Last_Week"] = bigdf3.groupby(["Vehicle"])["Pred_Ending_Mileage"].shift()
bigdf3["Last_Week_Diff_Miles"] = bigdf3.groupby(["Vehicle"])["Miles_Driven_Last_Week"].diff()
bigdf3["Last-1_Week_Miles"] = bigdf3.groupby(["Vehicle"])["Pred_Ending_Mileage"].shift(2)
bigdf3["Last-1_Week_Diff_Miles"] = bigdf3.groupby(["Vehicle"])["Last-1_Week_Miles"].diff()
bigdf3 = bigdf3.dropna()
Week_Ending = bigdf3.pop("Week_Ending")
bigdf3.head()


# In[57]:


train, test = train_test_split(bigdf3, test_size = .30, random_state = 25)


# In[58]:


mean_error = []
for index in range(17,30):
    train = train[train["Week_Index"] < index]
    val = test[test["Week_Index"] == index]
    
    xtr, xts = train.drop(['Pred_Ending_Mileage'], axis = 1), val.drop(["Pred_Ending_Mileage"], axis = 1)
    
    ytr, yts = train["Pred_Ending_Mileage"].values, val["Pred_Ending_Mileage"].values
    
    mdl2 = RandomForestRegressor(n_estimators = 1000,  n_jobs = -1, 
                               random_state = 0)
    mdl2.fit(xtr, ytr)
    
    p = mdl2.predict(xts)
    
    error = rmsle(yts, p)
    
    print('Week %d - Error %.5f' % (index, error))
    mean_error.append(error)

print("Mean Error = %.5f" % np.mean(mean_error))


# In[59]:


bigdf4 = bigdf.copy()
bigdf4["Miles_Driven_Last_Week"] = bigdf4.groupby(["Vehicle"])["Pred_Ending_Mileage"].shift()
bigdf4["Last_Week_Diff_Miles"] = bigdf4.groupby(["Vehicle"])["Miles_Driven_Last_Week"].diff()
bigdf4["Last-1_Week_Miles"] = bigdf4.groupby(["Vehicle"])["Pred_Ending_Mileage"].shift(2)
bigdf4["Last-1_Week_Diff_Miles"] = bigdf4.groupby(["Vehicle"])["Last-1_Week_Miles"].diff()
bigdf4["Last-2_Week_Miles"] = bigdf4.groupby(["Vehicle"])["Pred_Ending_Mileage"].shift(3)
bigdf4["Last-2_Week_Diff_Miles"] = bigdf4.groupby(["Vehicle"])["Last-2_Week_Miles"].diff()
bigdf4 = bigdf4.dropna()
Week_Ending = bigdf4.pop("Week_Ending")
bigdf4.head()


# In[60]:


train, test = train_test_split(bigdf4, test_size = .30, random_state = 25)


# In[61]:


mean_error = []
for index in range(17,30):
    train = train[train["Week_Index"] < index]
    val = test[test["Week_Index"] == index]
    
    xtr, xts = train.drop(['Pred_Ending_Mileage'], axis = 1), val.drop(["Pred_Ending_Mileage"], axis = 1)
    
    ytr, yts = train["Pred_Ending_Mileage"].values, val["Pred_Ending_Mileage"].values
    
    mdl3 = RandomForestRegressor(n_estimators = 1000,  n_jobs = -1, 
                               random_state = 0)
    mdl3.fit(xtr, ytr)
    
    p = mdl3.predict(xts)
    
    error = rmsle(yts, p)
    
    print('Week %d - Error %.5f' % (index, error))
    mean_error.append(error)

print("Mean Error = %.5f" % np.mean(mean_error))


# In[62]:


mean_error = []
for index in range(17,30):
    train = train[train["Week_Index"] < index]
    val = test[test["Week_Index"] == index]
    
    xtr, xts = train.drop(['Pred_Ending_Mileage'], axis = 1), val.drop(["Pred_Ending_Mileage"], axis = 1)
    
    ytr, yts = train["Pred_Ending_Mileage"].values, val["Pred_Ending_Mileage"].values
    
    mdl4 = RandomForestRegressor(n_estimators = 1000,  n_jobs = -1, 
                               random_state = 0)
    mdl4.fit(xtr, np.log1p(ytr))
    
    p = np.expm1(mdl4.predict(xts))
    
    error = rmsle(yts,p)
    print("Week %d - Error %.5f" % (index, error))
    mean_error.append(error)

print("Mean Error = %.5f" % np.mean(mean_error))


# In[63]:


mean_error = []
for index in range(17,30):
    train = train[train["Week_Index"] < index]
    val = test[test["Week_Index"] == index]
    
    xtr, xts = train.drop(['Pred_Ending_Mileage'], axis = 1), val.drop(["Pred_Ending_Mileage"], axis = 1)
    
    ytr, yts = train["Pred_Ending_Mileage"].values, val["Pred_Ending_Mileage"].values
    
    mdl5 = LGBMRegressor(n_estimators = 1000,  learning_rate = 0.01)
    
    mdl5.fit(xtr, np.log1p(ytr))
    
    p = np.expm1(mdl5.predict(xts))
    
    error = rmsle(yts,p)
    print("Week %d - Error %.5f" % (index, error))
    mean_error.append(error)

print("Mean Error = %.5f" % np.mean(mean_error))


# In[64]:


mean_error = []
for index in range(17,30):
    train = train[train["Week_Index"] < index]
    val = test[test["Week_Index"] == index]
    
    xtr, xts = train.drop(['Pred_Ending_Mileage'], axis = 1), val.drop(["Pred_Ending_Mileage"], axis = 1)
    
    ytr, yts = train["Pred_Ending_Mileage"].values, val["Pred_Ending_Mileage"].values
    
    mdl3 = RandomForestRegressor(n_estimators = 1000,  n_jobs = -1, 
                               random_state = 0)
    mdl3.fit(xtr, ytr)
    
    p = mdl3.predict(xts)
    
    error = rmsle(yts, p)
    
    print('Week %d - Error %.5f' % (index, error))
    mean_error.append(error)

print("Mean Error = %.5f" % np.mean(mean_error))


# In[65]:


val.loc[:, 'Prediction'] = np.round(p)

val.plot.scatter(x = "Prediction", y = "Pred_Ending_Mileage", figsize = (15,10), 
                title = "Prediction vs. Miles")


# In[67]:


df160_pred = df160.copy()
df160_pred["Miles_Driven_Last_Week"] = df160_pred.groupby(["Vehicle"])["Pred_Ending_Mileage"].shift()
df160_pred["Last_Week_Diff_Miles"] = df160_pred.groupby(["Vehicle"])["Miles_Driven_Last_Week"].diff()
df160_pred["Last-1_Week_Miles"] = df160_pred.groupby(["Vehicle"])["Pred_Ending_Mileage"].shift(2)
df160_pred["Last-1_Week_Diff_Miles"] = df160_pred.groupby(["Vehicle"])["Last-1_Week_Miles"].diff()
df160_pred["Last-2_Week_Miles"] = df160_pred.groupby(["Vehicle"])["Pred_Ending_Mileage"].shift(3)
df160_pred["Last-2_Week_Diff_Miles"] = df160_pred.groupby(["Vehicle"])["Last-2_Week_Miles"].diff()
df160_pred = df160_pred.dropna()
df160_pred.pop("Vehicle")
df160_pred


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[21]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




