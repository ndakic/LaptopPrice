#!/usr/bin/env python
# -*- coding: utf-8 -*

import pandas as pd
import numpy as np
import math

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt


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

    fileName = "../data/laptops.csv"
    columns = ["processor_number", "number_of_cores", "ram_amount", "storage_type", "storage_amount", "condition", 'screen_size']

    pd_data = load_data(fileName)
    formated_data = format_data(pd_data) # .dropna(subset=columns) Drop the rows where at least one element is missing.

    print "Loaded: %d" % len(pd_data)
    print "Formated: %d" % len(formated_data)

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

        print "Simple Linear Regression RMSE" + " for attribute > " + str(column) + " : " + str(math.sqrt((mean_squared_error(formated_data["processor_number"], predict))))
 
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

    # print X_test.to_string()
    # print y_test_pred 

    print "Multiple Linear Regression RMSE: " + str(math.sqrt((mean_squared_error(y_test, y_test_pred))))

    grades = [data['processor_number'],data['number_of_cores'], data['ram_amount'], data['storage_type'], data['ram_generation'], 
    data['storage_amount'], data['condition'], data['screen_size']]
    data_frame_object = pd.DataFrame(data=[grades], columns=['processor_number', 'number_of_cores', 'ram_amount', 'storage_type', 'ram_generation', 
        'storage_amount', 'condition', 'screen_size'])

    result = mlr.predict(data_frame_object)
    
    return result


if __name__ == '__main__':

    test = {}
    test['processor_number'] = 7
    test['number_of_cores'] = 4
    test['ram_amount'] = 16
    test['storage_type'] = 3
    test['ram_generation'] = 4
    test['storage_amount'] = 100
    test['condition'] = 6
    test['screen_size'] = 13

    print predict_price_mlr(test)
