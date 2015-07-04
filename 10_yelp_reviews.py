# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 17:15:06 2015

@author: brian
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import statsmodels.formula.api as smf

# visualization
import seaborn as sns
import matplotlib.pyplot as plt


# read data into a DataFrame
data = pd.read_csv('yelp.csv')

# create X and y
feature_cols = ['cool','useful','funny']
X = data[feature_cols]
y = data.stars

# instantiate and fit
linreg = LinearRegression()
linreg.fit(X, y)

# print the coefficients
print linreg.intercept_
print linreg.coef_

# pair the feature names with the coefficients
zip(feature_cols, linreg.coef_)

# cool is very collinear with useful and funny
# which may explain the negative coefficient for useful and funny
# perhaps using just cool is good enough

# define a function that accepts X and y and computes testing RMSE
def train_test_rmse(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    linreg = LinearRegression()
    linreg.fit(X_train, y_train)
    y_pred = linreg.predict(X_test)
    return np.sqrt(metrics.mean_squared_error(y_test, y_pred))

feature_cols = ['cool','useful','funny'] # RMSE 1.18429
X = data[feature_cols]
train_test_rmse(X, y)

feature_cols = ['cool'] # just using cool it's not that much worse, 1.21055
X = data[feature_cols]
train_test_rmse(X, y)
zip(feature_cols, linreg.coef_)

feature_cols = ['cool','useful']  # 1.196
X = data[feature_cols]
train_test_rmse(X, y)
zip(feature_cols, linreg.coef_)

feature_cols = ['cool','funny']  # 1.194
X = data[feature_cols]
train_test_rmse(X, y)

feature_cols = ['useful']  # 1.212
X = data[feature_cols]
train_test_rmse(X, y)

feature_cols = ['funny']  # 1.210
X = data[feature_cols]
train_test_rmse(X, y)

# let's explore the data

data.head()

data.columns

# include a "regression line"
sns.pairplot(data, x_vars=['cool','useful','funny'], y_vars='stars', size=6, aspect=0.7, kind='reg')

data.describe()

sns.pairplot(data)
# we have a lot of collinearity and hugh right tail,
# why so many zero ratings, does this mean missing or NA and should we discard or treat as non-predictive and missing?
sns.boxplot(x=data.cool) 
sns.boxplot(x=data.funny)
sns.boxplot(x=data.useful)

# let's look at correlations
# compute correlation matrix
data.corr()

# display correlation matrix in Seaborn using a heatmap
sns.heatmap(data.corr())

data[(data.cool == 0) & (data.funny == 0) & (data.useful == 0) ]
# so 36% of the set has no ratings at all,

# wonder what the average star rating is?
data[(data.cool == 0) & (data.funny == 0) & (data.useful == 0) ].stars.mean()
# it's 3.86 which is higher than the mean of 3.77 and RMSE is 1.17 using all 3 attrs
# so 0 really means missing
data[(data.cool == 0) & (data.funny == 0) & (data.useful == 0) ].head()


len(data[(data.cool != 0) & (data.funny != 0) & (data.useful != 0) ])


len(data[(data.cool != 0) | (data.funny != 0) | (data.useful != 0) ])
# 6388 or 64% have at least one of the attrs populated


# let's just build a model first for when at least one attributes exist
# what's the mean?
data[(data.cool != 0) | (data.funny != 0) | (data.useful != 0) ].stars.mean()
# 3.73 which is a little under the average of 3.77


feature_cols = ['cool','useful','funny']
X = data[(data.cool != 0) | (data.funny != 0) | (data.useful != 0) ][feature_cols]
y = data[(data.cool != 0) | (data.funny != 0) | (data.useful != 0) ].stars
train_test_rmse(X, y)  # 1.213 so that didn't really work much


# 2334 or 23% have all 3 attrs populated
data[(data.cool != 0) & (data.funny != 0) & (data.useful != 0) ].stars.mean()
# 3.74 is the mean
feature_cols = ['cool','useful','funny']
X = data[(data.cool != 0) & (data.funny != 0) & (data.useful != 0) ][feature_cols]
y = data[(data.cool != 0) & (data.funny != 0) & (data.useful != 0) ].stars
train_test_rmse(X, y)  # RMSE of 1.1356 so when all 3 are there we get a better prediction 



numbers = list()
avgStars = data.stars.mean()
for i in range(len(data)):
    numbers.append(avgStars)


# what's the null model RMSE if I just predict the average of 3.77
np.sqrt(metrics.mean_squared_error(data.stars, numbers))
# hmmm it's 1.214 so we have a ways to go

