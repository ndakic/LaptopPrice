#!/usr/bin/env python
# -*- coding: utf-8 -*

import pandas as pd
import math

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.model_selection import cross_val_score

import matplotlib.pyplot as plt
import psycopg2


def scatter_plot(data, feature, target):
	plt.figure(figsize=(16, 8))
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
	columns = ["id", "brand", "condition", "cores", "price", "processor_brand", "processor_model", "ram_amount", "ram_generation",
				"screen_size", "storage_amount", "storage_type", "url"]

	return pd.DataFrame(result, columns=columns)


def format_data(data):
	data['processor_model'] = data['processor_model'].map({'i7': 7, 'i5': 5, 'i3': 3})
	data['ram_generation'] = data['ram_generation'].map({'ddr4': 4, 'ddr3': 3, 'ddr2': 2})
	data['storage_type'] = data['storage_type'].map({'ssd': 2, 'hdd': 1})
	data['condition'] = data['condition'].map({'new': 1, 'used': 3, 'defective': 5})
	data['cores'] = data['cores'].astype('int64')

	return data


def transform_data(loaded_data):

	data_frame = pd.DataFrame()
	data_frame["condition"] = loaded_data["condition"]
	data_frame["cores"] = loaded_data["cores"]
	data_frame["ram_generation"] = loaded_data["ram_generation"]
	data_frame["processor_model"] = loaded_data["processor_model"]
	data_frame["storage_type"] = loaded_data["storage_type"]
	data_with_dummy_vars = pd.get_dummies(data=data_frame, drop_first=True)
	data_with_dummy_vars["ram_amount"] = loaded_data["ram_amount"]

	return data_with_dummy_vars


def transform_input(user_input):

	columns = ["condition_new", "condition_used", "cores_4", "ram_generation_ddr3", "ram_generation_ddr4",
				"processor_model_i5", "processor_model_i7", "storage_type_ssd", "ram_amount"]

	row = pd.DataFrame(data=[[0, 0, 0, 0, 0, 0, 0, 0, user_input["ram_amount"].iloc[0]]],
					   columns =columns)

	if user_input["condition"].iloc[0] == "new": row["condition_new"] = 1
	if user_input["condition"].iloc[0] == "used": row["condition_used"] = 1

	if user_input["cores"].iloc[0] == 4: row["cores_4"] = 1

	if user_input["ram_generation"].iloc[0] == "ddr3": row["ram_generation_ddr3"] = 1
	if user_input["ram_generation"].iloc[0] == "ddr4": row["ram_generation_ddr4"] = 1

	if user_input["processor_model"].iloc[0] == "i5": row["processor_model_i5"] = 1
	if user_input["processor_model"].iloc[0] == "i7": row["processor_model_i7"] = 1

	if user_input["storage_type"].iloc[0] == "ssd": row["storage_type_ssd"] = 1

	return row


# Multiple Linear Regression
def predict_price_mlr(data):

	loaded_data = load_data_from_db()
	data_with_dummies_var = transform_data(loaded_data)

	mlr = LinearRegression()

	# Split the data in training and test sets
	x_train, x_test, y_train, y_test = train_test_split(data_with_dummies_var, loaded_data.price, 
                                                        test_size=0.10, random_state=5)
	mlr.fit(x_train, y_train)  # Fitting a linear model

	print('Coefficients: \n', mlr.coef_, "Score: ", mlr.score(x_train, y_train))

	y_test_pred = mlr.predict(x_test)

	rmse = math.sqrt((mean_squared_error(y_test, y_test_pred)))

	result = mlr.predict(data.iloc[0].values.reshape(1, -1))

	return result, rmse


# K-Nearest Neighbors
def predict_price_knn(data):

	formated_data = format_data(load_data_from_db())

	# Drop columns
	x = formated_data.drop(['price', 'processor_brand', 'id', 'url', 'screen_size', 'brand', 'storage_amount'], axis=1)

	x_train, x_test, y_train, y_test = train_test_split(x, formated_data.price, test_size=0.10, random_state=5)

	num_list = list(range(1, 50))  # creating odd list of K for KNN

	neighbors = list(filter(lambda i: i % 2 != 0, num_list))  # subsetting just the odd ones

	cv_scores = []  # empty list that will hold cv scores

	# perform n-fold cross validation
	for k in neighbors: 
		knn = KNeighborsClassifier(n_neighbors=k)  # Finds the K-neighbors of a point.
		scores = cross_val_score(knn, x_train, y_train, cv=9)
		cv_scores.append(scores.mean())

	mse = [1 - cv for cv in cv_scores]  # changing to misclassification error

	optimal_k = mse.index(min(mse))  # determining best k
	print ("The optimal number of neighbors is %d" % optimal_k)

	neigh = KNeighborsRegressor(n_neighbors=optimal_k, weights='distance')
	neigh.fit(x_train, y_train)

	rmse = math.sqrt(mean_squared_error(y_test, neigh.predict(x_test)))
	result = neigh.predict(data.iloc[0].values.reshape(1, -1))
	
	return result, rmse
