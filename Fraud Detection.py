#!/usr/bin/env python
# coding: utf-8

# # Fraud Detection

# In[4]:


#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

#setting display  options and warnings
warnings.filterwarnings("ignore")
sns.set(color_codes=True)


# #### Load Dataset

# In[6]:


df = pd.read_csv("C:/Users/suyas/Downloads/CreditCardData.csv")
df.head()


# In[7]:


df.info()


# In[8]:


df_describe = df.describe(include='all')
df_describe


# #### Data Cleainng

# In[9]:


#Convert 'Amount' by removing currency symbol and converting to float
df['Amount'] = df['Amount'].replace('[£,]', '',regex=True).astype(float)


# In[10]:


#check for missing values and handle them
missing_values = df.isnull().sum()
missing_values


# In[11]:


# Filling missing values 
df['Amount'].fillna(df['Amount'].median(), inplace=True)
df['Merchant Group'].fillna(df['Merchant Group'].mode()[0], inplace=True)
df['Shipping Address'].fillna(df['Shipping Address'].mode()[0], inplace=True)
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)


# In[12]:


# Verify data after cleaning
data_cleaned_summary = df.describe(include='all')
data_cleaned_summary


# In[13]:



missing_values_after_cleaning = df.isnull().sum()
missing_values_after_cleaning


# In[14]:


# 1. Distribution of transaction amounts for fraudulent vs non-fraudulent transactions
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='Amount', hue='Fraud', bins=30, kde=True)
plt.title("Distribution of Transaction Amounts (Fraud vs Non-Fraud)")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.show()


# In[16]:


#2. Fraud distribution across types of cards
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Type of Card', hue='Fraud')
plt.title("Fraud Distribution by type of Card")
plt.xlabel("Type of card")
plt.ylabel("Count")
plt.show()


# In[17]:


#3. Fraud frequency based on entry mode
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Entry Mode', hue='Fraud')
plt.title("Fraud Distribution by Entry Mode")
plt.xlabel("Entry Mode")
plt.ylabel("Count")
plt.show()


# In[18]:


#4. Fraud Distribution by country of transaction
plt.figure(figsize=(7,5))
sns.countplot(data=df, x='Country of Transaction', hue='Fraud')
plt.title("Fraud Distribution by Country of Transaction")
plt.xlabel("Country of Transaction")
plt.ylabel("Count")
plt.show()


# In[ ]:




