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
    data['processor_number'] = data['processor_number'].map({'i7': 7, 'i5': 5, 'i3': 3, 'amd': 2})
    data['number_of_cores'] = data['number_of_cores'].map({4: 4, 2: 2})
    data['ram_amount'] = data['ram_amount'].map({'16gb': 16,'16 gb': 16,'12gb': 12,'12 gb': 12,'8gb': 8, '8 gb': 8, '6gb': 6, '6 gb': 6, "4gb": 4, "4 gb": 4})
    data['storage_type'] = data['storage_type'].map({'ssd': 2, 'hdd': 1})
    data['storage_amount'] = data['storage_amount'].map({'2TB': 20, '1TB': 15, '750gb': 12,'750 gb': 12, '500gb': 10, '500 gb': 10,'256gb': 8, '256 gb': 8,'128gb': 5, '128 gb': 5})
    data['condition'] = data['condition'].map({'Novo': 6, 'Nekorišćen': 5, 'Polovan bez oštećenja': 4, 'Polovan sa vidljivim znacima korišćenja': 3, "Neispravno": 2, "Nekorišćen sa felerom": 1})

    return data

if __name__ == '__main__':
    print "Started.."

    fileName = "../data/laptops.csv"
    columns = ["processor_number", "number_of_cores", "ram_amount", "storage_type", "storage_amount", "condition"]

    data = load_data(fileName)
    print "Loaded: %d" % len(data)
    formated_data = format_data(data).dropna(subset=columns)
    print "Formated: %d" % len(formated_data)

    # Simple Linear Regression

    simpleLR = LinearRegression()
    
    for column in columns:

        pro_num_column = formated_data[[column]]

        simpleLR.fit(pro_num_column, formated_data["price"])

        predict = simpleLR.predict(pro_num_column)

        print "Simple Linear Regression RMSE" + " for attribute > " + str(column) + " : " + str(math.sqrt((mean_squared_error(formated_data["processor_number"], predict))))
 


    # plt.plot(formated_data["condition"], data["price"])
    # plt.show()

    # Multiple Linear Regression

    mlr = LinearRegression()

    X = formated_data.drop(['price', 'processor_brand', 'laptop_brand', 'ram_generation', 'screen_size'], axis=1)
  
    X_train, X_test, y_train, y_test = train_test_split(X, formated_data.price, test_size=0.10, random_state=5)     # Split the data in trainig and test sets

    mlr.fit(X_train, y_train)   # Fitting a linear model

    y_test_pred = mlr.predict(X_test)

    print X_test.to_string()
    print y_test_pred 

    print "Multiple Linear Regression RMSE: " + str(math.sqrt((mean_squared_error(y_test, y_test_pred))))
