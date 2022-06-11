#!/usr/bin/env python
# coding: utf-8

# In[26]:



# import libraries for use 

import prophet
from prophet import Prophet
import pandas as pd
from matplotlib import pyplot
from pandas import to_datetime
from prophet.plot import plot_plotly, plot_components_plotly
import plotly.graph_objs as go
import plotly.express as px


# In[27]:


# import CSV data file

df = pd.read_csv("C:\\Users\\Nhowell.KUMAR\\Desktop\\Trucks v1.csv")

# Show first five of table

df.head(5)


# In[28]:


# Data types

df.dtypes

df.Week_Ending = df.Week_Ending.astype(str)
df.Vehicle = df.Vehicle.astype(str)
df.Beginning_Mileage = df.Beginning_Mileage.astype(int)
df.Ending_Mileage = df. Ending_Mileage.astype(int)
df.Total_Miles = df.Total_Miles.astype(int)
df.Office = df.Office.astype(str)
df.Year = df.Year.astype(str)
df.Make = df.Make.astype(str)
df.Model = df.Model.astype(str)


# In[29]:


# Total rows and columns -- 1550 rows, 9 columns

df.shape


# In[30]:


# How many duplicate rows -- 0,9

dupliacte_rows_df = df[df.duplicated()]
print("The number of duplicate rows: ", dupliacte_rows_df.shape)


# In[31]:


# Total number of rows in data set 

df.count()


# In[32]:


# Find the nulls

print(df.isnull().sum())


# In[33]:


# Descriptive data of the Total_Miles Column across all offices

df.describe()[['Total_Miles']]


# In[34]:




fig = px.histogram(df, x='Total_Miles', title = "Count of Total Miles Driven per Week")
fig.show()


# In[35]:


fig2 = px.box(df, y='Total_Miles', title = "Box Plot for Total Miles Driven per Week")
fig2.show()


# In[36]:


fig3 = px.scatter(df, x='Vehicle', y='Total_Miles', color = 'Office',
                  labels={
                      'Vehicle': "Vehicle Number",
                      'Total_Miles': "Total Miles per Week",
                      'Office': "Office",
                  }, title = "Scatter Plot of Total Miles Driven by Each Truck, Per Week",)
fig3.show()


# In[37]:


DN = df[df["Office"].str.contains('DN')]
PK = df[df["Office"].str.contains('PK')]
FC = df[df["Office"].str.contains('FC')]
CS = df[df["Office"].str.contains('CS')]
GS = df[df["Office"].str.contains('GS')]
SC = df[df["Office"].str.contains('SC')]


# In[39]:


DN1 = px.histogram(DN, x='Total_Miles', title = "Count of Total Miles Driven of Denver Trucks per Week")
DN1.show()


# In[40]:


PK1 = px.histogram(PK, x='Total_Miles', title = "Count of Total Miles Driven of Parker Trucks per Week")
PK1.show()


# In[41]:


FC1 = px.histogram(FC, x='Total_Miles', 
                   title = "Count of Total Miles Driven of Fort Collins Trucks per Week")
FC1.show()


# In[42]:


CS1 = px.histogram(CS, x='Total_Miles', 
                   title = "Count of Total Miles Driven of Colorado Springs Trucks per Week")
CS1.show()


# In[43]:


GS1 = px.histogram(GS, x='Total_Miles',
                   title = "Count of Total Miles Driven of Glenwood Springs Trucks per Week")
GS1.show()


# In[44]:


SC1 = px.histogram(SC, x='Total_Miles', 
                   title = "Count of Total Miles Driven of Summit County Trucks per Week")
SC1.show()


# In[45]:


DN2 = px.box(DN, y='Total_Miles', title = "Box Plot for Total Miles Driven per Week for Denver")
DN2.show()


# In[46]:


PK2 = px.box(PK, y='Total_Miles', title = "Box Plot for Total Miles Driven per Week for Parker")
PK2.show()


# In[47]:


FC2 = px.box(FC, y='Total_Miles', title = "Box Plot for Total Miles Driven per Week for Fort Collins")
FC2.show()


# In[48]:


fig2 = px.box(CS, y='Total_Miles', title = "Box Plot for Total Miles Driven per Week for Colorado Springs")
fig2.show()


# In[49]:


GS2 = px.box(GS, y='Total_Miles', title = "Box Plot for Total Miles Driven per Week for Glenwood Springs")
GS2.show()


# In[50]:


SC2 = px.box(SC, y='Total_Miles', title = "Box Plot for Total Miles Driven per Week for Summit County")
SC2.show()


# In[52]:


DN3 = px.scatter(x=DN['Vehicle'], y=DN['Total_Miles'],
                  labels={
                      'Vehicle': "Vehicle Number",
                      'Total_Miles': "Total Miles per Week",
                  }, title = "Scatter Plot of Total Miles Driven by Denver Trucks, Per Week")
DN3.show()


# In[53]:


PK3 = px.scatter(x=PK['Vehicle'], y=PK['Total_Miles'],
                  labels={
                      'Vehicle': "Vehicle Number",
                      'Total_Miles': "Total Miles per Week",
                  }, title = "Scatter Plot of Total Miles Driven by Parker Trucks, Per Week") 
PK3.show()


# In[54]:


FC3 = px.scatter(x=FC['Vehicle'], y=FC['Total_Miles'],
                  labels={
                      'Vehicle': "Vehicle Number",
                      'Total_Miles': "Total Miles per Week",
                  }, title = "Scatter Plot of Total Miles Driven by Fort Collins Trucks, Per Week")
FC3.show()


# In[55]:


CS3 = px.scatter(x=CS['Vehicle'], y=CS['Total_Miles'],
                  labels={
                      'Vehicle': "Vehicle Number",
                      'Total_Miles': "Total Miles per Week",
                  }, title = "Scatter Plot of Total Miles Driven by Colorado Springs Trucks, Per Week") 
CS3.show()


# In[56]:


GS3 = px.scatter(x=GS['Vehicle'], y=GS['Total_Miles'],
                  labels={
                      'Vehicle': "Vehicle Number",
                      'Total_Miles': "Total Miles per Week",
                  }, title = "Scatter Plot of Total Miles Driven by Glenwood Springs Trucks, Per Week")
GS3.show()


# In[57]:


SC3 = px.scatter(x=SC['Vehicle'], y=SC['Total_Miles'],
                  labels={
                      'Vehicle': "Vehicle Number",
                      'Total_Miles': "Total Miles per Week",
                  }, title = "Scatter Plot of Total Miles Driven by Summit County Trucks, Per Week")
SC3.show()


# In[58]:


# upload data
df = pd.read_csv("C:\\Users\\Nhowell.KUMAR\\Desktop\\187_Truck.csv")

# convert date to index, for clear plotting. 
df["Week_Ending"] = df["Week_Ending"].astype('datetime64[ns]')

# linear interpolation for missing values
df1 = df["Ending_Mileage"].interpolate(method = 'linear')


# In[59]:


# Adding the linear interpolation values back into the dataframe. 
list_df = []
for i in df1:
    list_df.append(i)
print(list_df)
df1 = pd.DataFrame(list_df, columns = ['Pred_Ending_Mileage'])
df = pd.concat([df, df1], axis =1).reindex(df.index)
df = df.drop("Ending_Mileage", axis = 1)


# In[60]:


df.to_csv('Interpolate_187.csv', index = False)


# In[61]:


# reupload of data. Not necessary, you can reset the index or skip the last plot. 
# We just need the date column to be the dates and not the index. 

df = pd.read_csv("C:\\Users\\Nhowell.KUMAR\\Desktop\\Interpolate_187.csv")

# print shape of data (rows, columns)
print(df.shape)

# print first five rows of data
print(df.head())


# In[62]:


# calling the dataframe I want to plot
df1.plot()

# showing the plot for the data frame
pyplot.show()


# In[63]:




# Prophet uses default column calls/names. ds is your date column, y is in this case mileage
df.columns = ["ds", "y"]

# convert the date column to date time format
df["ds"] = to_datetime(df["ds"])

# call the model we will be using Prophet
model = Prophet()

# fit the model to our data or data frame
model.fit(df)

#  future is our variable for extrapolating the model out to predict future values. The periods
# can be adjusted to predict further and further into the future. I have manipulated it to reflect 
# approx. when the truck will hit 200,000 miles. 

future = model.make_future_dataframe(periods = 1000)

# print the last 5 rows of the future data

print(future.tail())

# forecast is the forecasted data for our predictive model. 

forecast = model.predict(future)

# ds=date, yhat=future predicted value, yhat_lower= the lower range predicted value, 
# yhat_upper = upper range of predicted value. 

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()


# In[64]:


# create plot of forecasted values. Non-interactive. 

fig1 = model.plot(forecast)


# In[65]:


# create plot of forecasted values. Interactive.

plot_plotly(model, forecast)


# In[66]:


# upload data
df = pd.read_csv("C:\\Users\\Nhowell.KUMAR\\Desktop\\191_Truck.csv")

# convert date to index, for clear plotting. 
df["Week_Ending"] = df["Week_Ending"].astype('datetime64[ns]')

# linear interpolation for missing values
df1 = df["Ending_Mileage"].interpolate(method = 'linear')


# In[67]:


# Adding the linear interpolation values back into the dataframe. 
list_df = []
for i in df1:
    list_df.append(i)
print(list_df)
df1 = pd.DataFrame(list_df, columns = ['Pred_Ending_Mileage'])
df = pd.concat([df, df1], axis =1).reindex(df.index)
df = df.drop("Ending_Mileage", axis = 1)


# In[68]:


df.to_csv('Interpolate_191.csv', index = False)


# In[69]:


# reupload of data. Not necessary, you can reset the index or skip the last plot. 
# We just need the date column to be the dates and not the index. 

df = pd.read_csv("C:\\Users\\Nhowell.KUMAR\\Desktop\\Interpolate_191.csv")

# print shape of data (rows, columns)
print(df.shape)

# print first five rows of data
print(df.head())


# In[70]:


# calling the dataframe I want to plot
df.plot()

# showing the plot for the data frame
pyplot.show()


# In[71]:




# Prophet uses default column calls/names. ds is your date column, y is in this case mileage
df.columns = ["ds", "y"]

# convert the date column to date time format
df["ds"] = to_datetime(df["ds"])

# call the model we will be using Prophet
model = Prophet()

# fit the model to our data or data frame
model.fit(df)

#  future is our variable for extrapolating the model out to predict future values. The periods
# can be adjusted to predict further and further into the future. I have manipulated it to reflect 
# approx. when the truck will hit 200,000 miles. 

future = model.make_future_dataframe(periods = 2000)

# print the last 5 rows of the future data

print(future.tail())

# forecast is the forecasted data for our predictive model. 

forecast = model.predict(future)

# ds=date, yhat=future predicted value, yhat_lower= the lower range predicted value, 
# yhat_upper = upper range of predicted value. 

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()


# In[72]:


# create plot of forecasted values. Non-interactive. 

fig1 = model.plot(forecast)


# In[73]:


# create plot of forecasted values. Interactive.

plot_plotly(model, forecast)


# In[74]:


# upload data
df = pd.read_csv("C:\\Users\\Nhowell.KUMAR\\Desktop\\222_Truck.csv")

# convert date to index, for clear plotting. 
df["Week_Ending"] = df["Week_Ending"].astype('datetime64[ns]')

# linear interpolation for missing values
df1 = df["Ending_Mileage"].interpolate(method = 'linear')


# In[75]:


# Adding the linear interpolation values back into the dataframe. 
list_df = []
for i in df1:
    list_df.append(i)
print(list_df)
df1 = pd.DataFrame(list_df, columns = ['Pred_Ending_Mileage'])
df = pd.concat([df, df1], axis =1).reindex(df.index)
df = df.drop("Ending_Mileage", axis = 1)


# In[76]:


df.to_csv('Interpolate_222.csv', index = False)


# In[77]:


# reupload of data. Not necessary, you can reset the index or skip the last plot. 
# We just need the date column to be the dates and not the index. 

df = pd.read_csv("C:\\Users\\Nhowell.KUMAR\\Desktop\\Interpolate_222.csv")

# print shape of data (rows, columns)
print(df.shape)

# print first five rows of data
print(df.head())


# In[78]:


# calling the dataframe I want to plot
df.plot()

# showing the plot for the data frame
pyplot.show()


# In[79]:




# Prophet uses default column calls/names. ds is your date column, y is in this case mileage
df.columns = ["ds", "y"]

# convert the date column to date time format
df["ds"] = to_datetime(df["ds"])

# call the model we will be using Prophet
model = Prophet()

# fit the model to our data or data frame
model.fit(df)

#  future is our variable for extrapolating the model out to predict future values. The periods
# can be adjusted to predict further and further into the future. I have manipulated it to reflect 
# approx. when the truck will hit 200,000 miles. 

future = model.make_future_dataframe(periods = 1500)

# print the last 5 rows of the future data

print(future.tail())

# forecast is the forecasted data for our predictive model. 

forecast = model.predict(future)

# ds=date, yhat=future predicted value, yhat_lower= the lower range predicted value, 
# yhat_upper = upper range of predicted value. 

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()


# In[80]:


# create plot of forecasted values. Non-interactive. 

fig1 = model.plot(forecast)


# In[81]:


# create plot of forecasted values. Interactive.

plot_plotly(model, forecast)


# In[82]:


# upload data
df = pd.read_csv("C:\\Users\\Nhowell.KUMAR\\Desktop\\241_Truck.csv")

# convert date to index, for clear plotting. 
df["Week_Ending"] = df["Week_Ending"].astype('datetime64[ns]')

# linear interpolation for missing values
df1 = df["Ending_Mileage"].interpolate(method = 'linear')


# In[83]:


# Adding the linear interpolation values back into the dataframe. 
list_df = []
for i in df1:
    list_df.append(i)
print(list_df)
df1 = pd.DataFrame(list_df, columns = ['Pred_Ending_Mileage'])
df = pd.concat([df, df1], axis =1).reindex(df.index)
df = df.drop("Ending_Mileage", axis = 1)


# In[84]:


df.to_csv('Interpolate_241.csv', index = False)


# In[85]:


# reupload of data. Not necessary, you can reset the index or skip the last plot. 
# We just need the date column to be the dates and not the index. 

df = pd.read_csv("C:\\Users\\Nhowell.KUMAR\\Desktop\\Interpolate_241.csv")

# print shape of data (rows, columns)
print(df.shape)

# print first five rows of data
print(df.head())


# In[86]:


# calling the dataframe I want to plot
df.plot()

# showing the plot for the data frame
pyplot.show()


# In[87]:




# Prophet uses default column calls/names. ds is your date column, y is in this case mileage
df.columns = ["ds", "y"]

# convert the date column to date time format
df["ds"] = to_datetime(df["ds"])

# call the model we will be using Prophet
model = Prophet()

# fit the model to our data or data frame
model.fit(df)

#  future is our variable for extrapolating the model out to predict future values. The periods
# can be adjusted to predict further and further into the future. I have manipulated it to reflect 
# approx. when the truck will hit 200,000 miles. 

future = model.make_future_dataframe(periods = 1000)

# print the last 5 rows of the future data

print(future.tail())

# forecast is the forecasted data for our predictive model. 

forecast = model.predict(future)

# ds=date, yhat=future predicted value, yhat_lower= the lower range predicted value, 
# yhat_upper = upper range of predicted value. 

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()


# In[88]:


# create plot of forecasted values. Non-interactive. 

fig1 = model.plot(forecast)


# In[89]:


# create plot of forecasted values. Interactive.

plot_plotly(model, forecast)

