# -*- coding: utf-8 -*-
"""LogisticRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ImSRP2deP3IE1k9O9f2bnyDTlNXF1H92
"""

import numpy as np
import pandas as pd
import os

train_df = pd.read_csv('train.csv')

test_df = pd.read_csv('test.csv')

print('The number of samples into the train data is {}.'.format(train_df.shape[0]))

print('The number of samples into the test data is {}.'.format(test_df.shape[0]))

print(train_df.isnull().any())

train_df['Age'].fillna(train_df['Age'].mean(skipna=True), inplace=True)
test_df['Age'].fillna(test_df['Age'].mean(skipna=True), inplace=True)

print(train_df.head())

train_df_label = train_df['Survived']

train_df.drop(['Survived', 'Cabin', 'Embarked', 'Fare', 'Ticket', 'PassengerId', 'Name'], axis=1, inplace = True)

from sklearn.preprocessing import LabelEncoder

enc = LabelEncoder()
enc.fit(train_df['Sex'])
train_df['Sex'] = enc.transform(train_df['Sex'])

t_enc = LabelEncoder()
t_enc.fit(test_df['Sex'])
test_df['Sex'] = t_enc.transform(test_df['Sex'])

# 1 - male, 0 - female

from sklearn.linear_model import LogisticRegression

selected_features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']
test_df = test_df[selected_features]

model = LogisticRegression()
model.fit(train_df, train_df_label)

pred_label = model.predict(test_df)

test_label = pd.read_csv('gender_submission.csv')

test_label.drop(['PassengerId'], axis=1, inplace=True)

from sklearn.metrics import accuracy_score, confusion_matrix, precision_score

print("Accuracy is %.4f" % accuracy_score(pred_label, test_label))

print("Confusion matrix: ")
mat = confusion_matrix(test_label, pred_label)
print(mat)

print("%.4f" % precision_score(test_label, pred_label))

