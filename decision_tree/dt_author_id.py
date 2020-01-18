#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import tree


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

clf = tree.DecisionTreeClassifier(min_samples_split=40)
t0 = time()
clf = clf.fit(features_train,labels_train)
print ("training time:", round(time()-t0, 3), "s")

acc = clf.score(features_test,labels_test)
# accuracy is 0.9766
print(acc)
# print(len(features_train[0]))
# Number of features : 3785
# reduced to 379 after changing percentile in preprocess from 10 to 1
# accuracy changed to 0.967 after changing percentile