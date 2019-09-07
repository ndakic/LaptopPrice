import re
import csv

from bs4 import BeautifulSoup
from utils.chrome import get_webdriver

from model.laptop import Laptop


class LaptopUrl:

	def __init__(self, laptop_id, url):
		self.laptop_id = laptop_id
		self.url = url

	def __str__(self):
		return "{} {}".format(self.laptop_id, self.url)

	def get_laptop_id(self):
		return self.laptop_id

	@staticmethod
	def find_laptop_urls(processed_laptop_urls, project_base_url):

		collected_urls = list()

		print("Collectiong urls started..")

		driver = get_webdriver()

		pagination_limit = "1"

		driver.get(project_base_url + pagination_limit)
		bs_page_limit_page = BeautifulSoup(driver.page_source, 'html.parser')

		pagination_limit = bs_page_limit_page.find('div', attrs={'class': 'holder_pagination'}).find_all('a')[1].text

		print("Total pages: %d" % int(pagination_limit))

		limit = 0

		for page_number in range(1, int(pagination_limit)):

			if limit <= int(pagination_limit):

				driver.get(project_base_url + str(page_number))

				bs_page_urls = BeautifulSoup(driver.page_source, 'html.parser')

				laptops_container = bs_page_urls.find_all('div', attrs={'class': 'product'})

				for laptop_item in laptops_container:

					url = laptop_item.find('a', attrs={'class': 'item_link'})['href']

					get_id_regex = re.search(r'(/Laptopovi/)\d+.+', url)
					if get_id_regex:
						laptop_id = re.search(r'\d+.+', get_id_regex.group()).group().split("_")[0]

						if not Laptop.laptop_exist(laptop_id, processed_laptop_urls) and not Laptop.laptop_exist(laptop_id, collected_urls):
							collected_urls.append(LaptopUrl(laptop_id, url))

				limit += 1

		print("Total laptop urls found: %d" % len(collected_urls))

		return collected_urls

	@staticmethod
	def load_laptop_urls(file_name):

		laptop_urls = list()

		with open("data/" + file_name + '.csv', 'rt') as csv_file:
			loaded_data = list(csv.reader(csv_file, delimiter=","))[1:]  # skip header

			for row in loaded_data:
				laptop_urls.append(LaptopUrl(row[0], row[1]))

			print("%d Laptop urls loaded." % len(laptop_urls))

		csv_file.close()

		return laptop_urls
