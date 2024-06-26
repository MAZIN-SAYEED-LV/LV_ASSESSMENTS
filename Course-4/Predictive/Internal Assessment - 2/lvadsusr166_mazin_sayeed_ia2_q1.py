# -*- coding: utf-8 -*-
"""LVADSUSR166_MAZIN_SAYEED_IA2_Q1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1beQBXARg_PzkLQ6_66EcSwRpcIfQYTPV
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report,f1_score
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE

df = pd.read_csv(r"/content/winequality-red.csv")

df.info()

df.describe()

df.head()

df.isnull().sum()

df.info()

df.hist(bins=20, figsize=(15, 10))
plt.show()

# A (i) Filling Missing Values
df.fillna(df.mean(), inplace = True)

df.isnull().sum()

# A (ii) Removing Outliers
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)
df = df[~outliers]

# B (i) Data Transformation for quality
def data_transformation(quality):
    if quality >= 3 and quality <= 6:
        return 0
    elif quality >= 7 and quality <= 8:
        return 1
    else:
        return None

df['quality'] = df['quality'].apply(data_transformation)

# C (i) All values are numeric (all columns are float64 except quality which is int64)

# Wine quality Distribution
print("Wine quality distribution:")
print(df['quality'].value_counts())

# Visualising it
plt.figure(figsize=(8, 6))
sns.countplot(x='quality', data=df, palette='viridis')
plt.title('Wine Quality Distribution')
plt.xlabel('Quality')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

df.duplicated().sum()

# D (i) All features from the dataset contribute to predicting the wine quality
# D (ii) Remove duplicates
df=df.drop_duplicates()

df.duplicated().sum()

X = df.drop(columns=['quality'])
y = df['quality']

# E (i) Splitting the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply SMOTE to handle class imbalance
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# F (i) Training a Random Forest classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train_resampled, y_train_resampled)

# Predict on the test set
y_pred = clf.predict(X_test)

# G (i) Evaluating the Random Forest Model using metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1score = f1_score(y_test, y_pred)

print("Accuracy:", round(accuracy * 100, 2), "%")
print("Precision:", round(precision * 100, 2), "%")
print("Recall:", round(recall * 100, 2), "%")
print("F1-score", round(f1score * 100, 2), "%")

print("RF Classifier Metrics:")
print(classification_report(y_test, y_pred))

conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, cmap="YlGnBu", fmt="d", cbar=False)
plt.title("Confusion Matrix for RF")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()