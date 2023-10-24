#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task3


# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


# In[2]:


# Define the URL of the CSV file from Lab3
url = "https://raw.githubusercontent.com/atikagondal/Lab-2023-DAVE3625/main/Lab3/data/flight.csv"
# then read the CSV file from the spesified url using pandas
df = pd.read_csv(url)
#check if the dataframe we created contains the data from the CSV url
df


# In[3]:


#trying to find the colomns where we can change the type of it to DateTime
df.info()


# In[4]:


#converting spesified colomns to a dataTime and handling errors with 'coerce'
df['datetime_val'] = pd.to_datetime(df['datetime_val'],errors='coerce' )

df['dep_time'] = pd.to_datetime(df['dep_time'], errors='coerce')

df['arr_time'] = pd.to_datetime(df['arr_time'],errors='coerce')
df['sched_arr_time'] = pd.to_datetime(df['sched_arr_time'],errors='coerce' )
#check the data types of colomns and handle errors with 'coerce' 
df.info()


# In[5]:


# Iterate through every row in the df
for index, row in df.iterrows():
    #if the arr_time is earliar then dep_time
    if (row['arr_time']<row['dep_time']):
        # add one day to arr_time to account the potential time Zone change
        df.loc[index, 'arr_time'] = (row['arr_time'])+ datetime.timedelta(days=1)
   #if the sched_arr_time is earlier than dep_time
    if (row['sched_arr_time']<row['dep_time']):
        # add one day to sched_arr_time to adjust for scheduling discrepancies
        df.loc[index, 'sched_arr_time'] = (row['sched_arr_time'])+ datetime.timedelta(days=1)


# In[6]:


# we create a new colomn with name air_time which will store the calculated time differance in minumtes between arrival_time and departure_time 
df['air_time'] = df['arr_time'] - df['dep_time']

#  create a new colomn with name time_difference_sched which will store the Calculate time difference in minutes between 'sched_arr_time' and 'dep_time'
df['time_difference_sched'] = df['sched_arr_time'] - df['dep_time']


# In[7]:


# Display the first few rows of the df to inspect if new columns have been added successfully
df.head()


# In[8]:


#For every row in df
for index, row in df.iterrows():
    #if air_time is negative
    if (row['air_time'].days < 0):
        # Correct 'air_time' by adding 24 hours and subtracting the absolute value of negative days
        df.loc[index, 'air_time'] = datetime.timedelta(hours=24)-(row['air_time'] + datetime.timedelta(abs(row['air_time'].days)))
    


# In[9]:


df


# In[10]:


# Calculate the delay in arrival time and store it in a new column
df['Delay_arr_time'] = df['arr_time'] - df['sched_arr_time']

#calculate the delay as a percentage of the air_time and store it in a new column percent_delay

df['percent_delay'] = (100 * df['Delay_arr_time'])/df['air_time']
# print the calculated percent_delay 
print(df['percent_delay'])


# In[11]:


#create a box plot of the Percent_delay colomn
df['percent_delay'].plot.box()


# In[12]:


# generate a a discription for the percent_delay colomn  to provide summary statistics for it 
df["percent_delay"].describe()


# In[13]:


# find the row with the minnimum value in the "percent_delay" column
minrow= df['percent_delay'].argmin()

# get the corresponding row in df by using iloc
df.iloc[minrow]


# In[14]:


#finding outliers 

from pandas.api.types import is_numeric_dtype

#defining a function remove_outliers to remove outliers from the DF's nummeric colomns 
def remove_outlier(df):
    #difining lower and upper quantile values
    low = .05
    high = .95
    
      #quantlies is making a range of values which are excepted
    quant_df = df.quantile([low,high])
    
    #the function returns a df after removing all values that fall outside the defined range 
    if is_numeric_dtype(df):
        df = df[(df > quant_df.loc[low]) &(df < quant_df.loc[high])]
       
        return df


# In[15]:


# using the remove_outlier function on the colomn percent_delay
df["percent_delay"] = remove_outlier(df["percent_delay"])


# In[16]:


#repeting the plot to check if we did remove the outliers
#we can see clearly that the plot has changed and this is prove that the remove_outlier function worked
df["percent_delay"].plot.box()


# In[17]:


# repeting the description to double check if we did remove the outliers 
#we can see differance between before removing outliers and after and this is a prove that the function did work
df["percent_delay"].describe()


# In[ ]:





# In[ ]:




