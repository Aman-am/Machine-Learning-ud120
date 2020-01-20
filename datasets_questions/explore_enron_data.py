#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

len(enron_data)
len(enron_data.keys())

# For each person, how many features are available?
len(enron_data.values()[0])
enron_data[enron_data.keys()[0]]
len(enron_data['SKILLING JEFFREY K'])

# How many POIs are there in the E+F dataset
# Example 1:
count = 0
for i in range(len(enron_data)):
    a = enron_data.values()
    if a[i]['poi'] == True:
        count = count + 1        
print count

# Example 2:
count = 0
for user in enron_data:
    if enron_data[user]['poi'] == True:
        count+=1
print count

# How Many POIs Exist?
poi_names = open("../final_project/poi_names.txt", 'r')
fr = poi_names.readlines()
len(fr[2:])
poi_names.close()

# print(enron_data['SKILLING JEFFREY K'])
# if 'SKILLING JEFFREY K' in enron_data.keys():
#     print ("yes")
# else:
#     print ("No")

import pandas as pd 
import math
count = 0
for user in enron_data:
    if enron_data[user]['total_payments']:
    # if enron_data[user]["poi"]:
    # and enron_data[user]['total_payments'] =='NaN' :
        # print(enron_data[user]['salary'])
        count+=1
print count