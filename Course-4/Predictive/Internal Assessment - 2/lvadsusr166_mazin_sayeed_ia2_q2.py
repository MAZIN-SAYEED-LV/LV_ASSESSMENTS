# -*- coding: utf-8 -*-
"""lvadsusr166_mazin_sayeed_ia2_q2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tRa2FF6BEDu_BpC-sv27uGwIhN6yqLYD
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

customer_data = pd.read_csv('/content/Mall_Customers.csv')

customer_data.head()

customer_data.shape

customer_data.info()

customer_data.isnull().sum()

plt.hist(customer_data['Annual Income (k$)'])
plt.show()

customer_data['Annual Income (k$)'].fillna(customer_data['Annual Income (k$)'].mode()[0],inplace=True)

customer_data['Ratio']=customer_data['Annual Income (k$)']*1000/customer_data['Spending Score (1-100)']

customer_data.head()

X = customer_data.iloc[:,[3,4]].values

X=StandardScaler().fit_transform(X)

print(X)

wcss = []
for i in range(1,11):
  kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)

sns.set()
plt.plot(range(1,11), wcss)
plt.title('The Elbow Point Graph')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=0)
Y = kmeans.fit_predict(X)
print(Y)

# plotting all the clusters and their Centroids

plt.figure(figsize=(8,8))
plt.scatter(X[Y==0,0], X[Y==0,1], s=50, c='green', label='Low income, low spent score')
plt.scatter(X[Y==1,0], X[Y==1,1], s=50, c='red', label='Medium income, medium spent score')
plt.scatter(X[Y==2,0], X[Y==2,1], s=50, c='yellow', label='High income, low spent score')
plt.scatter(X[Y==3,0], X[Y==3,1], s=50, c='violet', label='low income, high spent score')
plt.scatter(X[Y==4,0], X[Y==4,1], s=50, c='blue', label='high income, high spent score')

# plot the centroids
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='cyan', label='Centroids')

plt.title('Customer Groups')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend(loc = "center right", fontsize="small")
plt.show()

print("""The visualization shows the clear representation of how the customers have been segmented based on this
information the company can take better decisions to how to make them more profitalbe""")

from sklearn.metrics import silhouette_score

print('silhouette score',silhouette_score(X,Y))

print('kmeans inertia',kmeans.inertia_)

