#!/usr/bin/env python
# -*- coding: utf-8 -*

import pandas as pd
import numpy as np
import math
import os

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import psycopg2

def load_data_from_db():

	try:
		conn = psycopg2.connect("host=server-api-db.c1yne3bmdpup.us-east-2.rds.amazonaws.com dbname=server_db user=ndakic password=postgres")
		print ("Connected to DB.")
	except:
		print ("I am unable to connect to the database")

	laptop_con = conn.cursor()

	laptop_con.execute("SELECT * FROM laptop")
	result = laptop_con.fetchall()
	# current order of loaded columns
	columns = ["id", "brand", "condition", "cores", "price", "processor_brand", "processor_model", "ram_amount", "ram_generation", 
			   "screen_size", "storage_amount", "storage_type", "url"]

	return pd.DataFrame(result, columns=columns)

def format_data(data):
	data['processor_model'] = data['processor_model'].map({'i7': 7, 'i5': 5, 'i3': 3})
	data['ram_generation'] = data['ram_generation'].map({'ddr4': 4, 'ddr3': 3, 'ddr2': 2})
	data['storage_type'] = data['storage_type'].map({'ssd': 3, 'hdd': 1})
	data['condition'] = data['condition'].map({'new': 6, 'used': 5, 'defective': 4})

	return data

# Multiple Linear Regression
def predict_price_mlr(data):

	formated_data = format_data(load_data_from_db())

	mlr = LinearRegression()

	X = formated_data.drop(['price', 'processor_brand', 'brand', 'id', 'url'], axis=1)
	
	# NOTE: current columns order after drop: condition, cores, processor_model, ram_amount, ram_generation, screen_size, storage_amount, storage_type
  
	X_train, X_test, y_train, y_test = train_test_split(X, formated_data.price, test_size=0.10, random_state=5)  # Split the data in training and test sets

	mlr.fit(X_train, y_train) # Fitting a linear model

	y_test_pred = mlr.predict(X_test)

	rmse = math.sqrt((mean_squared_error(y_test, y_test_pred)))

	values = [data['condition'], data['cores'], data['processor_model'], data['ram_amount'], data['ram_generation'], 
			  data['screen_size'], data['storage_amount'],  data['storage_type']]
	data_frame_object = pd.DataFrame(data=[values], columns=['condition', 'cores', 'processor_model','ram_amount', 'ram_generation', 
															'screen_size', 'storage_amount', 'storage_type'])
	result = mlr.predict(data_frame_object.values.reshape(1, -1))

	return result, rmse