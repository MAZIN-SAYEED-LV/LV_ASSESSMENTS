# -*- coding: utf-8 -*-
"""LVADSUSR166_MAZIN_SAYEED_IA1Q1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1l7Lqe_vXOXAKoROKc0_0M7Y_GlJK-A7r
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.metrics import classification_report, confusion_matrix, precision_score, recall_score, f1_score, accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,StandardScaler

df=pd.read_csv("/content/expenses.csv")

df.head()

df.shape

df.info()

df.describe()

df.duplicated().sum()

df.drop_duplicates(inplace=True)

df.duplicated().sum()

df.isnull().sum()

plt.hist(df['bmi'])
plt.show()

df['bmi'].fillna(df['bmi'].mean(),inplace=True)

df.isnull().sum()

for i in df.select_dtypes([int,float]):
  plt.hist(df[i])
  plt.title(f'Histogram of {i}')
  plt.ylabel("Frequency")
  plt.show()

for i in df.select_dtypes([object]):
  plt.bar(df[i].value_counts().index,df[i].value_counts().values)
  plt.xlabel(i)
  plt.ylabel('Frequency')
  plt.title(f'Bar chart of {i}')
  plt.show()

for i in df.select_dtypes([int,float]):
  plt.boxplot(df[i])
  plt.title(f'boxplot of {i}')
  plt.show()

numerical=df.select_dtypes([int,float])
q1=numerical.quantile(0.25)
q3=numerical.quantile(0.75)
iqr=q3-q1
lower=q1-1.5*iqr
upper=q3+1.5*iqr

outliers=df[df[numerical.columns]<lower]|df[df[numerical.columns]>upper]
df=df[~outliers.any(axis=1)]

df.shape

correl_matrix=df[numerical.columns].corr()

sns.heatmap(correl_matrix,annot=True,fmt=".2f")
plt.show()

columns_to_encode=['sex','smoker','region']
for column in columns_to_encode:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])

df

cormat=df.corr()

sns.heatmap(cormat,annot=True,fmt=".2f")
plt.show()

x=df.drop(['charges'],axis=1)
y=df['charges']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

scaler=StandardScaler()

x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)

model=LinearRegression()

model.fit(x_train,y_train)

predicted=model.predict(x_test)

rmse=np.sqrt(mean_squared_error(y_test,predicted))

r2score=r2_score(y_test,predicted)

print("RMSE",rmse)

print('r2 score',r2score)

