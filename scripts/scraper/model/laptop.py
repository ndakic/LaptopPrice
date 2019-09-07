#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import re
import time

from utils.chrome import get_webdriver
from bs4 import BeautifulSoup

from model.enum import ProcessorBrand, ProcessorCores, ProcessorNumber, LaptopBrand, Condition, RamGeneration, StorageType


class Laptop:
	def __init__(self):
		self._laptop_brand = None
		self._processor_brand = None
		self._processor_number = None
		self._number_of_cores = None
		self._ram_generation = None
		self._ram_amount = None
		self._storage_type = None
		self._storage_amount = None
		self._screen_size = None
		self._price = None
		self._condition = None
		self._url = None
		self._laptop_id = None

	def __str__(self):
		return "id: {} laptop brand: {} processor number: {} condition: {} price: {}".format(self._laptop_id, self._laptop_brand, self._processor_number,
		                               self._condition, self._price)

		# setters
	def set_condition(self, condition):
		if condition.lower() == "novo":
			self._condition = Condition.NEW.value

		if condition.lower() == "nekorišćen":
			self._condition = Condition.NEW.value

		if condition.lower() == "polovan bez oštećenja":
			self._condition = Condition.USED.value

		if condition.lower() == "polovan sa vidljivim znacima korišćenja":
			self._condition = Condition.DEFECTIVE.value

		if condition.lower() == "neispravno":
			self._condition = Condition.DEFECTIVE.value

		# when conditions are loaded from file
		if condition == "new":
			self._condition = Condition.NEW.value

		if condition == "used":
			self._condition = Condition.USED.value

		if condition == "defective":
			self._condition = Condition.DEFECTIVE.value

	def set_laptop_brand(self, brand):

		if brand.lower() == "apple":
			self._laptop_brand = LaptopBrand.APPLE.value

		if brand.lower() == "hewlett packard" or brand.lower() == "hp omen" or brand.lower() == "hp":
			self._laptop_brand = LaptopBrand.HP.value

		if brand.lower() == "dell":
			self._laptop_brand = LaptopBrand.DELL.value

		if brand.lower() == "acer":
			self._laptop_brand = LaptopBrand.ACER.value

		if brand.lower() == "terra" or brand.lower() == "terra mobile":
			self._laptop_brand = LaptopBrand.TERRA.value

		if brand.lower() == "lenovo":
			self._laptop_brand = LaptopBrand.LENOVO.value

		if brand.lower() == "samsung":
			self._laptop_brand = LaptopBrand.SAMSUNG.value

		if brand.lower() == "sony":
			self._laptop_brand = LaptopBrand.SONY.value

		if brand.lower() == "asus":
			self._laptop_brand = LaptopBrand.ASUS.value

		if brand.lower() == "fujitsu":
			self._laptop_brand = LaptopBrand.FUJITSU.value

		if brand.lower() == "toshiba":
			self._laptop_brand = LaptopBrand.TOSHIBA.value

	def set_processor_brand(self, brand):
		if brand.lower() == "intel":
			self._processor_brand = ProcessorBrand.INTEL.value

	def set_processor_number(self, processor_number):
		if processor_number == "i7":
			self._processor_number = ProcessorNumber.I7.value
		if processor_number == "i5":
			self._processor_number = ProcessorNumber.I5.value
		if processor_number == "i3":
			self._processor_number = ProcessorNumber.I3.value

	def set_processor_cores(self, cores):
		if int(cores) == 4:
			self._number_of_cores = ProcessorCores.FOUR.value
		if int(cores) == 2:
			self._number_of_cores = ProcessorCores.TWO.value

	def set_ram_generation(self, ram_generation):
		if ram_generation == "ddr4":
			self._ram_generation = RamGeneration.DDR4.value
		if ram_generation == "ddr3":
			self._ram_generation = RamGeneration.DDR3.value
		if ram_generation == "ddr2":
			self._ram_generation = RamGeneration.DDR2.value

	def set_storage_type(self, storage_type):
		if storage_type == "ssd":
			self._storage_type = StorageType.SSD.value
		if storage_type == "hdd":
			self._storage_type = StorageType.HDD.value

	def set_price(self, price):
		self._price = price

	def set_screen_size(self, screen_size):
		self._screen_size = screen_size

	def set_storage_amount(self, storage_amount):
		self._storage_amount = storage_amount

	def set_ram_amount(self, ram_amount):
		self._ram_amount = ram_amount

	def set_laptop_ulr(self, url):
		self._url = url

	def set_laptop_id(self, laptop_id):
		self._laptop_id = laptop_id

	# getters
	def get_condition(self):
		return self._condition

	def get_laptop_brand(self):
		return self._laptop_brand

	def get_processor_brand(self):
		return self._processor_brand

	def get_processor_number(self):
		return self._processor_number

	def get_processor_cores(self):
		return self._number_of_cores

	def get_ram_generation(self):
		return self._ram_generation

	def get_storage_type(self):
		return self._storage_type

	def get_price(self):
		return self._price

	def get_screen_size(self):
		return self._screen_size

	def get_storage_amount(self):
		return self._storage_amount

	def get_ram_amount(self):
		return self._ram_amount

	def get_laptop_ulr(self):
		return self._url

	def get_laptop_id(self):
		return self._laptop_id

	@staticmethod
	def laptop_exist(laptop_id, collection):
		for laptop in collection:
			if laptop.get_laptop_id() == laptop_id:
				return True

		return False

	@staticmethod
	def load_laptops(file_name):

		laptops = list()

		with open("data/" + file_name + '.csv', 'rt') as csv_file:
			loaded_data = list(csv.reader(csv_file, delimiter=","))[1:]  # skip header
			for data in loaded_data:
				laptop = Laptop()
				laptop.set_laptop_brand(data[0])
				laptop.set_processor_brand(data[1])
				laptop.set_processor_number(data[2])
				laptop.set_processor_cores(data[3])
				laptop.set_ram_generation(data[4])
				laptop.set_ram_amount(data[5])
				laptop.set_storage_type(data[6])
				laptop.set_storage_amount(data[7])
				laptop.set_screen_size(data[8])
				laptop.set_price(data[9])
				laptop.set_condition(data[10])
				laptop.set_laptop_ulr(data[11])
				laptop.set_laptop_id(data[12])
				laptops.append(laptop)

			print("%d laptops loaded." % len(laptops))

		csv_file.close()

		return laptops

	@staticmethod
	def insert_human_knowledge(
			number_of_cores, ram_generation, ram_amount, storage_amount, processor_number, storage_type, condition, price):

		# check number of cores
		if not number_of_cores:
			if processor_number == 'i5' and price < 80000:
				number_of_cores = 2
			if processor_number == 'i5' and price >= 80000 and condition == 'used':
				number_of_cores = 4
			if processor_number == "i7":
				number_of_cores = 4
			if processor_number == "i3":
				number_of_cores = 2

		# check ram generation
		if not ram_generation:
			if price < 50000:
				ram_generation = "ddr2"
			if price >= 50000 < 100000:
				ram_generation = "ddr3"
			if price > 100000:
				ram_generation = "ddr4"

		# check ram amount
		if not ram_amount:
			if price < 50000 and condition == "new":
				ram_amount = 4
			if price < 50000 and condition == "used":
				ram_amount = 8
			if price >= 50000 < 100000:
				ram_amount = 8
			if price >= 100000 < 150000 and condition == "used":
				ram_amount = 16
			if price >= 100000 < 150000 and condition == "new":
				ram_amount = 8
			if price >= 150000:
				ram_amount = 16

		# check storage amount
		if not storage_amount:
			if price < 50000:
				storage_amount = 250
			if price >= 50000:
				storage_amount = 500

		# check condition
		if processor_number == 'i5' and condition == 'used' and ram_amount == 8 and storage_type == 'ssd' and price < 25000:
			condition = 'defective'
		if processor_number == 'i5' and condition == 'used' and ram_amount == 8 and storage_type == 'hdd' and price < 20000:
			condition = 'defective'
		if processor_number == 'i7' and condition == 'used' and ram_amount <= 8 and price < 25000:
			condition = 'defective'

		# set typical if spec is empty
		if not number_of_cores:
			number_of_cores = 2
		if not storage_type:
			storage_type = 'hdd'

		return number_of_cores, ram_generation, ram_amount, storage_amount, processor_number, storage_type, condition

	@staticmethod
	def get_laptop_details(description):

		processor_brand, processor_number, number_of_cores, ram_generation, ram_amount, storage_type, storage_amount = None, None, None, None, None, None, None

		description_lower = description.lower()

		# get processor brand, number and number_of_cores
		if "quad" in description_lower:
			number_of_cores = 4
		else:
			number_of_cores = 2

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

			if ram_amount and int(ram_amount) > 32:
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

		if not storage_amount:
			storage_amount_regex = re.search(r'(hdd)[^\S\n\t]*[:]?[^\S\n\t].*\d+[^\S\n\t]*.*(gb)*', description_lower)
			if storage_amount_regex:
				storage_temp = re.search(r'\d+[ ]?(gb)*', storage_amount_regex.group())
				if storage_temp:
					storage_amount = re.search(r'\d+', storage_temp.group()).group()

		if not storage_amount:
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

		if storage_amount:
			if int(storage_amount) == 1:
				storage_amount = "1000"
				storage_type = "hdd"

			if int(storage_amount) == 2:
				storage_amount = "2000"
				storage_type = "hdd"

			if int(storage_amount) < 100 or int(storage_amount) > 2000:
				storage_amount = None

		return processor_brand, processor_number, number_of_cores, ram_generation, ram_amount, storage_type, storage_amount

	@staticmethod
	def find_laptops(laptop_urls, collected_laptops):

		laptops = list()

		print("Getting laptops info started..")

		driver = get_webdriver()

		count = 0

		for laptop_url in laptop_urls:
			laptop = Laptop()
			laptop.set_laptop_id(laptop_url.laptop_id)
			laptop.set_laptop_ulr(laptop_url.url)
			if not Laptop.laptop_exist(laptop.get_laptop_id(), collected_laptops) and not Laptop.laptop_exist(laptop.get_laptop_id(), laptops):
				try:
					time.sleep(1)
					driver.get(laptop_url.url)

					laptop_page = BeautifulSoup(driver.page_source, 'html.parser')

					# get laptop price
					price_search = re.search(r'\d+[.]\d+', laptop_page.find("span", attrs={"class": "input-group-addon"}).text)
					if price_search:
						laptop.set_price(int(price_search.group().replace(".", "")))

					# get laptop condition
					condition_search = laptop_page.find("table", attrs={
						'class': 'table table-predmet table-predmet-info table-clear'}).find_all('tr')[0].find_all('td')

					if condition_search[0].text.lower() == "stanje:":
						laptop.set_condition(condition_search[1].text)
					else:
						laptop.set_condition(laptop_page.find("table",
							attrs={'class': 'table table-predmet table-predmet-info table-clear'}).find_all('tr')[1].find_all('td')[1].text)
					search_status = True
					description = laptop_page.find('div', attrs={'id': 'opis'}).find_all('p')
					try:
						laptop.set_screen_size(re.search(r'\d+[,.]*\d*', description[0].find_all('strong')[0].text.strip()).group().replace(",", '.'))
						laptop.set_laptop_brand(description[0].find_all('strong')[1].text)
					except:
						pass

					try:
						processor_brand, processor_number, number_of_cores, ram_generation, \
						ram_amount, storage_type, storage_amount = Laptop.get_laptop_details(description[1].text)
						laptop.set_processor_brand(processor_brand)
						laptop.set_processor_number(processor_number)
						laptop.set_processor_cores(number_of_cores)
						laptop.set_ram_generation(ram_generation)
						laptop.set_ram_amount(ram_amount)
						laptop.set_storage_type(storage_type)
						laptop.set_storage_amount(storage_amount)
					except IndexError as e:
						# print("Index error: ", e)
						search_status = False

					# insert human knowledge if spec is empty
					number_of_cores, ram_generation, ram_amount, storage_amount, processor_number, storage_type, condition = \
						Laptop.insert_human_knowledge(
													laptop.get_processor_cores(),
													laptop.get_ram_generation(),
													laptop.get_ram_amount(),
													laptop.get_storage_amount(),
													laptop.get_processor_number(),
													laptop.get_storage_type(),
													laptop.get_condition(),
													laptop.get_price())

					laptop.set_processor_cores(number_of_cores)
					laptop.set_ram_generation(ram_generation)
					laptop.set_ram_amount(ram_amount)
					laptop.set_storage_amount(storage_amount)
					laptop.set_processor_number(processor_number)
					laptop.set_storage_type(storage_type)
					laptop.set_condition(condition)
					if search_status and laptop.get_processor_number() and laptop.get_price() and laptop.get_laptop_brand():
						laptops.append(laptop)
					else:
						print(laptop.get_processor_number(), laptop.get_price(), laptop.get_laptop_brand(), search_status)

					print(count, laptop_url)
					count += 1

				except Exception as e:
					print("Exception:", e)

			else:
				print("Laptop already exist: {}".format(laptop_url.laptop_id))

		return laptops
