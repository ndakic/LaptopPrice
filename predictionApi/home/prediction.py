#!/usr/bin/env python
# -*- coding: utf-8 -*

import pandas as pd
import numpy as np
import math

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt


laptopFileName = '/home/daka/Desktop/LaptopPrice/scripts/data/laptops.csv'


def load_data(fileName):
    return pd.read_csv(fileName)

def format_data(data):
    data['processor_number'] = data['processor_number'].map({'i7': 7, 'i5': 5, 'i3': 3})
    data['number_of_cores'] = data['number_of_cores']
    data['ram_amount'] = data['ram_amount']
    data['storage_type'] = data['storage_type'].map({'ssd': 3, 'hdd': 1})
    data['ram_generation'] = data['ram_generation'].map({'ddr4': 4, 'ddr3': 3, 'ddr2': 2})
    data['storage_amount'] = data['storage_amount']
    data['condition'] = data['condition'].map({'new': 6, 'used': 5, 'defective': 4})
    data['screen_size'] = data['screen_size']
    data['price'] = data['price']

    return data

def get_data():

    columns = ["processor_number", "number_of_cores", "ram_amount", "storage_type", "storage_amount", "condition", 'screen_size']

    pd_data = load_data(laptopFileName)
    formated_data = format_data(pd_data) # .dropna(subset=columns) Drop the rows where at least one element is missing.

    #print "Loaded: %d" % len(pd_data)
    #print "Formated: %d" % len(formated_data)

    return pd_data, formated_data

# Simple Linear Regression
def predict_price_slr(data):    

    pd_data, formated_data = get_data()

    columns = ["processor_number", "number_of_cores", "ram_amount", "storage_type", "storage_amount", "condition", 'screen_size', 'ram_generation']

    simpleLR = LinearRegression()
    
    for column in columns:

        pro_num_column = formated_data[[column]]

        simpleLR.fit(pro_num_column, formated_data.price)

        predict = simpleLR.predict(pro_num_column)

        #print "Simple Linear Regression RMSE" + " for attribute > " + str(column) + " : " + str(math.sqrt((mean_squared_error(formated_data["processor_number"], predict))))
 
    # plt.plot(formated_data["condition"], pd_data["price"])
    # plt.show()

# Multiple Linear Regression
def predict_price_mlr(data):

    pd_data, formated_data = get_data()

    mlr = LinearRegression()

    X = formated_data.drop(['price', 'processor_brand', 'laptop_brand', 'laptop_id', 'url'], axis=1)
  
    X_train, X_test, y_train, y_test = train_test_split(X, formated_data.price, test_size=0.10, random_state=5)     # Split the data in training and test sets

    mlr.fit(X_train, y_train)   # Fitting a linear model

    y_test_pred = mlr.predict(X_test)

    #print "Multiple Linear Regression RMSE: " + str(math.sqrt((mean_squared_error(y_test, y_test_pred))))

    grades = [data['processorModel'],data['processorCores'], data['ramGeneration'], data['ramAmount'], data['storageType'], data['storageAmount'], data['screenSize'], data['condition']]
    data_frame_object = pd.DataFrame(data=[grades], columns=['processorModel', 'processorCores', 'ramGeneration', 'ramAmount', 'storageType', 'storageAmount', 'screenSize', 'condition' ])

    result = mlr.predict(data_frame_object.values.reshape(1, -1))
    
    return result


def create_dict(data):

    specs = {}

    specs['processorCores'] = data['processorCores']
    specs['ramAmount'] = data['ramAmount']
    specs['storageAmount'] = data['storageAmount']
    specs['screenSize'] = data['screenSize']

    if data['processorModel'] == 'i7':
        specs['processorModel'] = 7

    if data['processorModel'] == 'i5':
        specs['processorModel'] = 5

    if data['processorModel'] == 'i3':
        specs['processorModel'] = 3

    if data['storageType'] == 'ssd':
        specs['storageType'] = 3

    if data['storageType'] == 'hdd':
        specs['storageType'] = 1

    if data['ramGeneration'] == 'ddr4':
        specs['ramGeneration'] = 4

    if data['ramGeneration'] == 'ddr3':
        specs['ramGeneration'] = 3

    if data['ramGeneration'] == 'ddr2':
        specs['ramGeneration'] = 2

    if data['condition'] == 'new':
        specs['condition'] = 6

    if data['condition'] == 'used':
        specs['condition'] = 5

    if data['condition'] == 'defective':
        specs['condition'] = 4

    return specs