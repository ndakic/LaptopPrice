#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import time
import csv
import random
import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path

from model.link import Link
from model.laptop import Laptop

root_path = sys.argv[1]

links = []
laptops = []

def get_chrome_options():

	user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

	chrome_options = Options()  
	chrome_options.add_argument('user-agent=%s' % user_agent)
	chrome_options.add_argument("--headless")
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('start-maximized')
	chrome_options.add_argument('disable-infobars')
	chrome_options.add_argument("--disable-extensions")
	chrome_options.add_argument('--dns-prefetch-disable')
	chrome_options.add_argument("--disable-dev-shm-usage")

	return chrome_options

def check_file_name(file_name):

	my_file = Path(root_path + "data/" + file_name + ".csv")

	if my_file.exists():
		file_name = file_name + str(random.randint(1, 1000) * 5)
		check_file_name(file_name)

	return file_name

def check_does_file_exist(filename):
	my_file = Path(root_path + "data/"+ filename + ".csv")

	if my_file.exists():
		return True
	else:
		return False

def save_data(file_name, purpose):

	with open(root_path + "data/" + file_name +'.csv', 'wt', 1) as myfile:
		wr = csv.writer(myfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
		if purpose == 'urls':
			wr.writerow(['laptop_id', 'laptop_url'])

			for i in links:
				wr.writerow([i.laptop_id, i.url])

		if purpose == 'laptops_info':
			wr.writerow(['laptop_brand', 'processor_brand', 'processor_number', 'number_of_cores', 'ram_generation', 'ram_amount', 'storage_type', 'storage_amount', 'screen_size', "price", "condition", "url", "laptop_id"])

			for i in laptops:
				wr.writerow([i.laptop_brand, i.processor_brand, i.processor_number, i.number_of_cores, i.ram_generation, i.ram_amount, i.storage_type, i.storage_amount, i.screen_size, i.price, i.condition, i.url, i.laptop_id])

			print "Total laptops saved: %d" % len(laptops)

	myfile.close()

def load_links(file_name):

	with open(root_path + "data/" +file_name + '.csv', 'rt') as csvfile:
		loaded_data = list(csv.reader(csvfile, delimiter=","))[1:] # skip header

		for link in loaded_data:
			links.append(Link(link[0], link[1]))

		print "%d links loaded." % len(links)

	csvfile.close()

def load_laptops(file_name):

	with open(root_path + "data/" + file_name + '.csv', 'rt') as csvfile:
		loaded_data = list(csv.reader(csvfile, delimiter=","))[1:] # skip header

		for laptop in loaded_data:
			laptops.append(Laptop(laptop[0], laptop[1], laptop[2], laptop[3], laptop[4], laptop[5], laptop[6], laptop[7], laptop[8], laptop[9], laptop[10], laptop[11], laptop[12]))

		print "%d laptops loaded." % len(laptops)

	csvfile.close()

def check_does_exist(laptop_id, purpose):

	status = False
	if purpose == "link":
		for link in links:
			if link.laptop_id == laptop_id:
				status = True

	if purpose == "laptop":
		for laptop in laptops:
			if laptop.laptop_id == laptop_id:
				status = True
		
	return status

def translate_condition(condition):
	if condition.lower() == "novo":
		return "new"
	if condition.lower() == "nekorišćen":
		return "new"
	if condition.lower() == "polovan bez oštećenja":
		return "used"

	return condition

def get_links(base_url):

	print "Collectiong urls started.."

	driver = webdriver.Chrome(executable_path=root_path + "scraper/chromedriver", chrome_options=get_chrome_options())
	driver.set_page_load_timeout(30)

	pagination_limit = "1"

	driver.get(base_url + pagination_limit)
	bs_page_limit_page = BeautifulSoup(driver.page_source, 'html.parser')

	pagination_limit = bs_page_limit_page.find('div', attrs={'class': 'holder_pagination'}).find_all('a')[1].text

	print "Total pages: %d" % int(pagination_limit)

	limit = 0

	for page_number in range(1, int(pagination_limit)):

		if limit <= int(pagination_limit):

			driver.get("https://www.kupindo.com/Racunari-i-oprema/Laptop-racunari-delovi-i-oprema/Laptopovi/artikli/1473/cena_DESC_strana_" 
				+ str(page_number))

			bs_page_urls = BeautifulSoup(driver.page_source, 'html.parser')

			laptops_container = bs_page_urls.find_all('div', attrs={'class': 'product'})

			for laptop_item in laptops_container:

				link = laptop_item.find('a', attrs={'class':'item_link'})['href']

				get_id_regex = re.search(r'(/Laptopovi/)\d+.+', link)
				if get_id_regex:
					laptop_id = re.search(r'\d+.+', get_id_regex.group()).group().split("_")[0]

					if check_does_exist(laptop_id, "link") == False:
						links.append(Link(laptop_id, link))

			limit += 1

	print "Total links found: %d" % len(links)

def get_details(description):
	processor_brand = ""
	processor_number = ""
	number_of_cores = 2
	ram_generation = ""
	ram_amount = ""
	storage_type = "hdd"
	storage_amount = ""

	description_lower = description.lower()

	# get processor brand, number and number_of_cores

	if "quad" in description_lower:
		number_of_cores = 4

	processor_number_regex = re.search(r'[i][357]', description_lower)
	if processor_number_regex:
		processor_number = processor_number_regex.group()
		processor_brand = "intel"

	# get ram_generation and ram_amount	

	ram_generation_regex = re.search(r'(memorija|ram)+.+(ddr)\d?', description_lower)
	if ram_generation_regex:
		ram_gen = re.search(r'(ddr)[234]', ram_generation_regex.group())
		if ram_gen:
			ram_generation = ram_gen.group()

	ram_regex = r'(memorija|ram)[^\S\n\t]*[:]?[^\S\n\t]*(ddr)?[234]?[^\S\n\t]*\d+[^\S\n\t]*(gb)'
	ram_amount_regex = re.search(ram_regex, description_lower)
	if ram_amount_regex:
		ram_r = re.search(r'\d+[^\S\n\t]*(gb)', ram_amount_regex.group())
		if ram_r:
			ram_amount = re.search(r'\d+', ram_r.group()).group()

		if int(ram_amount) > 32:
			ram_amount = "8"

	# get storage type and amount

	ssd_regex = re.search(r'(ssd)', description_lower)
	if ssd_regex:
		storage_type = "ssd"

	storage_amount_regex = re.search(r'(disk)[^\S\n\t]*[:]?[^\S\n\t].*\d+[^\S\n\t]*.*(gb)*', description_lower)
	if storage_amount_regex:
		storage_temp = re.search(r'\d+[ ]?(gb)*', storage_amount_regex.group())
		if storage_temp:
			storage_amount = re.search(r'\d+', storage_temp.group()).group()

	if storage_amount == "":
		storage_amount_regex = re.search(r'(hdd)[^\S\n\t]*[:]?[^\S\n\t].*\d+[^\S\n\t]*.*(gb)*', description_lower)
		if storage_amount_regex:
			storage_temp = re.search(r'\d+[ ]?(gb)*', storage_amount_regex.group())
			if storage_temp:
				storage_amount = re.search(r'\d+', storage_temp.group()).group()

	if storage_amount == "":
		storage_amount_regex = re.search(r'(ssd)[^\S\n\t]*[:]?[^\S\n\t].*\d+[^\S\n\t]*.*(gb)*', description_lower)
		if storage_amount_regex:
			storage_temp = re.search(r'\d+[ ]?(gb)*', storage_amount_regex.group())
			if storage_temp:
				storage_amount = re.search(r'\d+', storage_temp.group()).group()

	storage_amount_regex_terabite = re.search(r'\d[^\S\n\t]*(tb)', description_lower)
	if storage_amount_regex_terabite:
		storage_tb = re.search(r'\d', storage_amount_regex_terabite.group())
		if storage_tb:
			storage_amount = re.search(r'\d+', storage_tb.group()).group() 

	if storage_amount != "":
		if int(storage_amount) == 1:
				storage_amount = "1000"
				storage_type = "hdd"

		if int(storage_amount) == 2:
			storage_amount = "2000"
			storage_type = "hdd"

		if int(storage_amount) < 100 or int(storage_amount) > 2000:
			storage_amount = ""

	return processor_brand, processor_number, number_of_cores, ram_generation, ram_amount, storage_type, storage_amount

def get_laptop_info():

	print "Getting laptops info started.."

	driver = webdriver.Chrome(executable_path=root_path + "scraper/chromedriver", chrome_options=get_chrome_options())
	driver.set_page_load_timeout(30)

	count = 0

	for link in links:
		if check_does_exist(link.laptop_id, "laptop") == False:
			try:
				time.sleep(1)
				
				driver.get(link.url)
				laptop_page = BeautifulSoup(driver.page_source, 'html.parser')

				# get latop price
				price = ""
				price_search = re.search(r'\d+[.]\d+', laptop_page.find("span", attrs={"class": "input-group-addon"}).text)
				if price_search:
					print price
					price = int(price_search.group().replace(".", ""))

				# get laptop condition
				condition = ""
				condition_search = laptop_page.find("table", attrs={'class': 'table table-predmet table-predmet-info table-clear'}).find_all('tr')[0].find_all('td')
				
				if condition_search[0].text.lower() == "stanje:":
					condition = condition_search[1].text
				else:
					condition = laptop_page.find("table", attrs={'class': 'table table-predmet table-predmet-info table-clear'}).find_all('tr')[1].find_all('td')[1].text

				condition = translate_condition(condition)

				search_status = True
				description = laptop_page.find('div', attrs={'id': 'opis'}).find_all('p')

				try:
					screen_size = re.search(r'\d+[,.]*\d*', (description[0].find_all('strong')[0].text).strip()).group().replace(",", '.')
					laptop_brand = description[0].find_all('strong')[1].text
					processor_brand, processor_number, number_of_cores, ram_generation, ram_amount, storage_type, storage_amount = get_details(description[1].text)
				except Exception as e:
					print e
					search_status = False

				# insert human knowledge

				if price < 50000:
					number_of_cores = 2

				if ram_generation == "":
					if price < 50000:
						ram_generation = "ddr2"
					if price >= 50000 and price < 100000:
						ram_generation = "ddr3"
					if price > 100000:
						ram_generation = "ddr4"

				if ram_amount == "":
					if price < 50000:
						ram_amount = 4
					if price < 50000 and condition == "used":
						ram_amount = "8"
					if price >= 50000 and price < 100000:
						ram_amount = "8"
					if price >= 100000 and price < 150000 and condition == "used":
						ram_amount = "16"
					if price >= 100000 and price < 150000 and condition == "new":
						ram_amount = "8"
					if price >= 150000:
						ram_amount = "16"

				if search_status and processor_number != "" and price != "" and storage_amount != "" and ram_amount != "":
					laptops.append(Laptop(laptop_brand, processor_brand, processor_number, number_of_cores, ram_generation, ram_amount, storage_type, storage_amount, screen_size, price, condition, link.url, link.laptop_id))
				
				print count, link.display()
				count += 1

				# if count == 10:
				# 	break

			except Exception as e:
				print e

		else:
			print "Laptop already exist: %s" % link.laptop_id

if __name__ == "__main__":

	urls_filename = "urls"
	laptop_filename = "laptops"
	link_base_url = 'https://www.kupindo.com/Racunari-i-oprema/Laptop-racunari-delovi-i-oprema/Laptopovi/artikli/1473/cena_DESC_strana_'

	if check_does_file_exist('urls'):
		load_links(urls_filename)
		get_links(link_base_url)
		save_data(urls_filename, "urls")
	else:
		get_links(link_base_url)
		save_data(urls_filename, "urls")
	
	if check_does_file_exist('laptops'):
		load_laptops(laptop_filename)

	get_laptop_info()
	save_data(laptop_filename, "laptops_info")