#!/usr/bin/env python
# coding: utf-8

# # 1. Import Required Libraries
# 

# In[184]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


# # 2. Load Dataset

# In[185]:


df= pd.read_csv("movies.csv")
df.head(5)


# # 3. Dataset Overview 

# In[186]:


df.shape


# In[187]:


df.columns


# In[188]:


df.isnull().sum()


# # 4. Drop Irrelevant Columns

# In[189]:


df.drop(columns = ["id", "imdb_id", "homepage","cast", "tagline", "overview","budget_adj" ], inplace=True)
df.head(5)


# # 5. Handle Missing Values

# In[190]:


df.isnull().sum()


# In[191]:


df.dropna(how = 'any', subset=['genres','director'], inplace = True)


# In[192]:


df['production_companies']=df['production_companies'].fillna(0)
df['keywords']=df['keywords'].fillna(0)


# In[193]:


df.isnull().sum()


# # 6. Round Popularity

# In[194]:


df['popularity']= df['popularity'].round(2)


# In[195]:


df


# # 7. Feature Engineering: Profit and ROI

# In[196]:


df.insert(3, 'profit', df.revenue-df.budget)


# In[197]:


df.insert(4, 'roi', df.profit/df.budget)


# In[198]:


df1= [['popularity', 'budget', 'revenue','profit','roi','vote_count', 'vote_average', 'release_year']]


# In[199]:


df.isnull().sum()


# In[200]:


non_finite_values=~np.isfinite(df['roi'])


# In[201]:


non_finite_values.sum()


# # 8. Handle Infinite ROI Values

# In[202]:


df['roi']= df['roi'].replace([np.inf, -np.inf], np.nan)


# # 9. Histograms of Numerical Columns

# In[203]:


df.hist(bins=20, figsize=(14,12))
plt.show()


# In[204]:


df.popularity.value_counts()


# In[205]:


df


# # 10.  ROI Trend Over Years

# In[206]:


df2=df.groupby('release_year')['roi'].mean()
df2.plot(kind='line')


# # 11. Popularity Trend Over Years 

# In[207]:


df3=df.groupby('release_year')['popularity'].sum()
df3.plot(kind='line', color='pink')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Popularity')


# In[208]:


df4=df.groupby('release_year')['popularity'].sum()
df3.plot(kind='line', color='pink')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Popularity')


# # 12. Rating Trend Over Years

# In[209]:


df4=df.groupby('release_year')['vote_average'].mean()
df4.plot(kind='line', color='pink')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Ratings')


# # 13. Popularity vs Rating Scatter Plot 

# In[210]:


df5= df.plot.scatter(x='popularity', y='vote_average', c = 'pink',figsize=(6,4))
df5.set_xlabel('Popularity', color = "DarkRed")
df5.set_xlabel("Vote Average", color = "DarkRed")
df5.set_xlabel('Popularity', color = "DarkRed")


# In[211]:


df.head(5)


# # 14. Genre Analysis

# In[212]:


df.genres.value_counts()


# In[213]:


split = ['genres']
for i in split:
    df[i]= df[i].apply(lambda x: x.split("|") )
df.head(3)


# In[214]:


df= df.explode('genres')
df


# In[215]:


# Sum of popularity by genre
df7= df.groupby('genres')["popularity"].sum().sort_values(ascending= True)
df7


# In[216]:


df7.plot.barh(x= 'genres', y= 'popularity', color= 'pink')


# In[217]:


df.head()


# In[218]:


df.dtypes


# # 15. Monthly Popularity Analysis

# In[219]:


df['release_date']= pd.to_datetime(df['release_date'])


# In[220]:


df['extracted_month']= df['release_date'].dt.month


# In[221]:


df8 = df.groupby('extracted_month')['popularity'].sum()


# In[222]:


df8


# In[223]:


df8.index


# In[224]:


df8.values


# In[225]:


# Convert to DataFrame
data = {
    'extracted_month': df8.index,
    'popularity': df8.values
}
df8=pd.DataFrame(data)


# In[226]:


df8


# In[227]:


# Map month numbers to names
index_to_month = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
}


# In[228]:


df8.extracted_month= df8.extracted_month.map(index_to_month)


# In[229]:


df8


# In[230]:


# Plot Monthly Popularity
df8.plot(kind= 'bar', x= "extracted_month", y="popularity", color = 'pink')


# # 16. Monthly Revenue Analysis

# In[231]:


df9= df.groupby('extracted_month')['revenue'].sum()
df9


# In[232]:


data = {
    'extracted_month': df9.index,
    'revenue': df9.values
}
df9=pd.DataFrame(data)


# In[233]:


index_to_month = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
}


# In[234]:


df9.extracted_month= df9.extracted_month.map(index_to_month)


# In[235]:


df9


# In[236]:


df9.plot(kind = 'bar', x= 'extracted_month' , y= 'revenue', color='Darkblue' )


# In[237]:


df.head()


# # 17. Top 5 Profitable Movies

# In[238]:


df10=df.groupby('original_title')['profit'].sum().sort_values(ascending= False).head(5)
df10


# In[239]:


df10.plot(kind='pie', autopct= '%1.1f%%', startangle= 90, colors= plt.cm.Paired.colors)
plt.title('Top 5 Movies by profit', color='red')


# # So the winner is Avatar movie

# In[ ]:




