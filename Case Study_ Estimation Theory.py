#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
from scipy.stats import sem, t


data = pd.read_csv('100-Sales-Records.csv')


# In[5]:


data.head()


# In[9]:


mean_sales = data['Units Sold'].mean()
std_sales = data['Units Sold'].std()
print(f"Mean Sales: {mean_sales}, Standard Deviation: {std_sales}")


# In[10]:


confidence = 0.95
n = len(data['Units Sold'])
margin_error = sem(data['Units Sold']) * t.ppf((1 + confidence) / 2., n-1)
ci = (mean_sales - margin_error, mean_sales + margin_error)
print(f"95% Confidence Interval: {ci}")


# In[11]:


bootstrap_means = [data['Units Sold'].sample(frac=1, replace=True).mean() for _ in range(1000)]
bootstrap_ci = np.percentile(bootstrap_means, [2.5, 97.5])
print(f"Bootstrap Confidence Interval: {bootstrap_ci}")


# In[ ]:




