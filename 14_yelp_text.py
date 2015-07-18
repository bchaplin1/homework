# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 18:02:58 2015

@author: brian
"""

# TASK 1: read the data from yelp.csv into a DataFrame

import pandas as pd
yelp = pd.read_csv('yelp.csv')


# TASK 1 (ALTERNATIVE): construct the same DataFrame from yelp.json

# read the data from yelp.json into a list of rows
# each row is decoded into a dictionary using using json.loads()
import json
with open('yelp.json', 'rU') as f:
    data = [json.loads(row) for row in f]

# convert the list of dictionaries to a DataFrame
yelp = pd.DataFrame(data)[(yelp.stars ==5) | (yelp.stars==1 )  ]

# store feature matrix in "X"
feature_cols = ['text']
X = yelp[feature_cols]

# store response vector in "y"
y = yelp.stars


# ### Understanding the `train_test_split` function
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

type(X_train)

type(X_train[0,0])

X_train[1,0].lower()

X_train.shape


from sklearn.feature_extraction.text import CountVectorizer

# learn the 'vocabulary' of the training data 
vect = CountVectorizer() 

 
# learn vocabulary and create document-term matrix in a single step 
train_dtm = vect.fit_transform(X_train[:,0]) 

# transform testing data into a document-term matrix 
test_dtm = vect.transform(X_test[:,0]) 

# train a Naive Bayes model using train_dtm 
from sklearn.naive_bayes import MultinomialNB 
nb = MultinomialNB() 
nb.fit(train_dtm, y_train) 

# make predictions on test data using test_dtm 
y_pred_class = nb.predict(test_dtm) 

# compare predictions to true labels 
from sklearn import metrics 

# predict and calculate AUC 
y_pred_prob = nb.predict_proba(test_dtm)[:, 1] 
y_test2 = []
for x in y_test:
    if x == 5:
        y_test2.append(1)
    else:
        y_test2.append(0)

print metrics.roc_auc_score(y_test2, y_pred_prob) 

print metrics.accuracy_score(y_test, y_pred_class) 
confusion = metrics.confusion_matrix(y_test, y_pred_class)
print  confusion
sensitivity =float(confusion[1,1])/(confusion[1,0] + confusion[1,1])
print 'sensitivity is %f' % sensitivity
# sensitivity is 98.65% 

specificity =float(confusion[0,0])/(confusion[0,0] + confusion[0,1])
print 'specificity is %f' % specificity
# specificity is only 60% 
 
 # plot ROC curve
import matplotlib.pyplot as plt
fpr, tpr, thresholds = metrics.roc_curve(y_test2, y_pred_prob)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')
plt.plot(fpr, tpr)

# show false positives and false negatives
X_test[y_test < y_pred_class][:5,:]
# the false positives appear to be fooled by all the text, 
# or words never seen before like D-scust-ing. 
# Some seem to use a 1 if it's a different place but now under new management 

X_test[y_test > y_pred_class][:5,:]
# the false negatives from words like kinda disappointed, bot oh well, possibly Jesus Christ used more as a swear word that honoring the deity, 
# DMV review had Hate, dreading 
# because they were contrasting DMV with the place reviewed, 
# similarly with the Whitey vs. Meinike

y_pred_prob_sorted = y_pred_prob.copy()

y_pred_prob_sorted.sort()
idx = 1635 * .4
idx
y_pred_prob_sorted[idx]
# a false positive rate of as low as 40% can be achieved without sacrificing the 5 start ratings much as the TPR is still 99%
# the percentage cutoff at that point is 99.999756963708564%
y_pred_prob_sorted[1635 * .2]
# if you want to cut the false positive rate in half to 20%, then the 5 star rating will still be about 90%
# the percentage cutoff would be 99.189101964091309%
