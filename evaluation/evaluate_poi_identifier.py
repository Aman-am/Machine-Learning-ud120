#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.model_selection import train_test_split

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

features_train, features_test, labels_train, labels_test = train_test_split(features,
                labels,test_size=0.3,random_state=42)
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train,labels_train)

# acc = clf.score(features_test,labels_test)
# print(acc)
pred = clf.predict(features_test)
# print(sum(pred))

# print(len(features_test))

# print(pred)
# print(labels_test)
from sklearn.metrics import precision_score, recall_score
print(recall_score(labels_test,pred))
# precision & recall both are 0.0