#!/usr/bin/env python
# -*- coding: utf-8 -*

import pandas as pd
import numpy as np
import math
import os

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.model_selection import cross_val_score

from  matplotlib import pyplot 

import matplotlib.pyplot as plt
import psycopg2


def scatter_plot(data, feature, target):
	plt.figure(figsize=(16,8))
	plt.scatter(
		data[feature],
		data[target],
		c='black')
	plt.show()

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
	data['storage_type'] = data['storage_type'].map({'ssd': 2, 'hdd': 1})
	data['condition'] = data['condition'].map({'new': 1, 'used': 2})
	data['cores'] = data['cores'].astype('int64')

	return data

# Multiple Linear Regression
def predict_price_mlr(data):

	formated_data = format_data(load_data_from_db())

	mlr = LinearRegression()

	X = formated_data.drop(['price', 'processor_brand', 'brand', 'id', 'url', 'screen_size', 'storage_amount'], axis=1)

	# scatter_plot(formated_data, "ram_generation", "price")

	# NOTE: current columns order after drop: condition, cores, processor_model, ram_amount, ram_generation, screen_size, storage_amount, storage_type

	X_train, X_test, y_train, y_test = train_test_split(X, formated_data.price, test_size=0.10, random_state=5)  # Split the data in training and test sets

	mlr.fit(X_train, y_train) # Fitting a linear model

	# print('Coefficients: \n', mlr.coef_, "Score: ", mlr.score(X_train, y_train))

	y_test_pred = mlr.predict(X_test)

	rmse = math.sqrt((mean_squared_error(y_test, y_test_pred)))

	result = mlr.predict(data.iloc[0].values.reshape(1, -1))

	return result, rmse

# K Nearest Neighbors
def predict_price_knn(data):

	formated_data = format_data(load_data_from_db())

	# Drop columns
	X = formated_data.drop(['price', 'processor_brand', 'brand', 'id', 'url', 'screen_size', 'storage_amount'], axis=1)

	X_train, X_test, y_train, y_test = train_test_split(X, formated_data.price, test_size=0.10, random_state=5)

	# creating odd list of K for KNN
	# num_list = list(range(1,50))

	# subsetting just the odd ones
	# neighbors = list(filter(lambda x: x % 2 != 0, num_list))

	# empty list that will hold cv scores
	# cv_scores = []

	# perform 10-fold cross validation
	# for k in neighbors: 
	# 	knn = KNeighborsClassifier(n_neighbors=k) # Finds the K-neighbors of a point.
	# 	scores = cross_val_score(knn, X_train, y_train, cv=5)
	# 	cv_scores.append(scores.mean())

	# changing to misclassification error
	# MSE = [1 - x for x in cv_scores]

	# determining best k
	# optimal_k = MSE.index(min(MSE))
	# print ("The optimal number of neighbors is %d" % optimal_k)

	neigh = KNeighborsRegressor(n_neighbors=8, weights='distance')
	neigh.fit(X_train, y_train)

	rmse = math.sqrt(mean_squared_error(y_test, neigh.predict(X_test)))

	result = neigh.predict(data.iloc[0].values.reshape(1, -1))
	
	return result, rmse