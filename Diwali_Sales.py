#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv('Diwali_Sales_Data.csv',encoding='unicode_escape')
df.shape


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[6]:


df.info()


# In[7]:


pd.isnull(df).sum()


# In[8]:


df.shape


# In[9]:


df.dropna(inplace=True)


# In[10]:


pd.isnull(df).sum()


# In[11]:


df['Amount']=df['Amount'].astype('int')


# In[12]:


df['Amount'].dtype


# In[13]:


df.describe()


# ## Exploratory Data Analysis

# ### Gender

# In[22]:


df.columns


# In[18]:


ax=sns.countplot(data=df,x='Gender')


# In[30]:


# Showing values 
ax=sns.countplot(data=df,x='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
    


# In[45]:


sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(data=sales_gen,x='Gender',y='Amount')


# ## Most of the buyer are female. Female purchasing power are greter than men

# ### Age

# In[48]:


df.columns


# In[52]:


ax=sns.countplot(data=df,x='Age Group',hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[63]:


# Total Amount vs Age group 
sales_age=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(data=sales_age,x='Age Group',y='Amount')


# ### From Above graph we can say most of the buyer are age group from 26 to 35 years Female. 

# ### State 

# In[75]:


sales_state=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.barplot(data=sales_state,x='State',y='Orders')
sns.set(rc={'figure.figsize':(27,10)})


# In[76]:


### Total Amount by State 
sales_state=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.barplot(data=sales_state,x='State',y='Amount')
sns.set(rc={'figure.figsize':(27,10)})


# ### From Above graph most of the orders and amount purchase by UP,Maharastra and Karnataka State 

# ### Marital_Status

# In[83]:


ax=sns.countplot(data=df,x='Marital_Status')
sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[88]:


sales_marital=df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(data=sales_marital,x='Marital_Status',y='Amount',hue='Gender')


# ### From above graph most of buyer are married women

# ### Occupation 

# In[91]:


ax=sns.countplot(data=df,x='Occupation')
sns.set(rc={'figure.figsize':(30,8)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[96]:


sales_occupation=df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(data=sales_occupation,x='Occupation',y='Amount')


# ### Above graph shows that most of the buyer are from IT and Healthcare sector 

# In[98]:


df.columns


# ### Product Category 

# In[105]:


ax=sns.countplot(data=df,x='Product_Category')
sns.set(rc={'figure.figsize':(30,10)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[107]:


sales_product_category=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.barplot(data=sales_product_category,x='Product_Category',y='Amount')


# ### Most of product sales in Food Category 

# ### TOP SELLING PRODUCT

# In[112]:


sales_product=df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.barplot(data=sales_product,x='Product_ID',y='Orders')


# # Conculsion:-

# ## According to the analyzed data it can be determined that Female individuals who are married and aged between 26 and 35 years and who work within the Information Technology, Healthcare, and Aviation sectors in the states of Uttar Pradesh, Maharashtra, and Karnataka, have a higher propensity to purchase products from the categories of Food, Clothing, and Electronics.

# ## Project Learnings:- 

# ### 1.Executed data cleaning and manipulation procedures.
# ### 2. Conducted exploratory data analysis (EDA) utilizing the pandas, matplotlib, and seaborn libraries.
# ### 3. Enhanced the customer experience by identifying prospective customers among diverse states, occupations, genders, and age groups.
# ### 4. Boosted sales by identifying the highest selling product categories and products, thereby facilitating inventory planning to meet demand.
# 
# 

# In[ ]:




