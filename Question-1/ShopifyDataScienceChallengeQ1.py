#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 
path = ".\RawData\DataScienceDataSet1.csv"
'''
A AOV value of $3145.13 is very high when considering the price of sneakers. The metric used may be the mean  and the issue 
that has arisen is that there are some outliers that are affecting the mean. Using Pandas, we will load in the Raw Data
in a data frame and then look at the Descriptive statistics using the describe() method.
'''
raw_df =pd.read_csv(path)
raw_df


# In[5]:


#Let's take a look at the Descriptive statistics  of this data set.
print("Descriptive statistics of Raw Data \n")
print(raw_df.describe())


# In[6]:


'''
The issue: When we look at orders data over a 30 day window, we naively calculate an average order value (AOV) of $3145.13. 
Reasoning: The mean is very succeptable to outliers, and with a very high Standard Deviation there is an indication that outliers are skewing the mean.

Solution: A better metric  for a quick glance could be to use the median value instead as it is less succeptible to being influenced by the outliers.
Using the median has the average AOV at $284.00 per order. This however is still not a perfect measure but it is better.
If we wish for a more accurate measure of the AOV, we should clean the data and remove any statistical outliers.
'''


# In[16]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(1, 2)
fig.suptitle('AOV Box Plot Comparison After Cleaning')    
axes[0].set_title('AOV: Before')
axes[1].set_title('AOV:After')

sns.boxplot(ax=axes[0], x=raw_df["order_amount"])


# In[9]:


'''
As you can see from the box plot, we some outliers that are causing issues with our analysis.
Following statistical convention , we will calculate the Interquartile Range (IQR) and anything outside q3 + 1.5 * IQR
or q1 - 1.5 *IQR will be discarded.
'''


# In[20]:


q1 = raw_df["order_amount"].quantile(0.25)
q3 = raw_df["order_amount"].quantile(0.75)
IQR = q3-q1
upperbound = q3 + (1.5 * IQR)
lowerbound = q1 - (1.5 * IQR)
df_no_outliers = raw_df[(raw_df["order_amount"] < upperbound) & (raw_df["order_amount"] > lowerbound)]


# In[21]:

print("\nDescriptive statistics of Cleaned Data \n")
print(df_no_outliers.describe())
#the boxplot once the initial outliers are removed
sns.boxplot(ax=axes[1],x=df_no_outliers["order_amount"])
plt.show()


# In[19]:


'''
Now that the Data is cleaned from the outliers, we can use the new Mean as the metric to evaluate  the AOV.

The AOV is: $293.72 per order.
'''
print(f"\nThe metric to calculate the AOV is the mean of the data after removing outliers:${round(df_no_outliers['order_amount'].mean(),2)}")
print(f"\nAlternatively if the data is to not be modified in any manner, then we will use the median of the original data set thus the AOV would be: ${round(raw_df['order_amount'].median(),2)}")

# In[25]:


# In[ ]:




