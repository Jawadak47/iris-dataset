#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
iris = pd.read_csv('Iris.csv')


# In[3]:


print(iris.head())


# In[4]:


# Scatter plot of sepal length vs sepal width
plt.scatter(iris['SepalLengthCm'], iris['SepalWidthCm'])
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()


# In[5]:


# Scatter plot of petal length vs petal width, colored by species
colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'green', 'Iris-virginica': 'blue'}
plt.scatter(iris['PetalLengthCm'], iris['PetalWidthCm'], c=iris['Species'].map(colors))
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.show()


# In[6]:


# Box plot of sepal width by species
plt.boxplot([iris[iris['Species']=='Iris-setosa']['SepalWidthCm'],
             iris[iris['Species']=='Iris-versicolor']['SepalWidthCm'],
             iris[iris['Species']=='Iris-virginica']['SepalWidthCm']],
            labels=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
plt.ylabel('Sepal Width (cm)')
plt.show()


# In[ ]:




