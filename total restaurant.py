#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[23]:


data=pd.read_csv(r'E:/Data/food_delivery_datasets.csv')
print(data)


# In[ ]:





# In[26]:


#jumlah toko dengan banyaknya kali pesanan
x=data['resto_id']
print(x)


# In[43]:


#jumlah toko
y=[]
for i in x:
    if i not in y:
        y.append(i)
z=len(y)
print(z)
print(y)


# In[ ]:





# In[ ]:




