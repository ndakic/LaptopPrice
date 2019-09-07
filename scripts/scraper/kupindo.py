#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from utils import file
from model.url import LaptopUrl
from model.laptop import Laptop

laptop_urls = []
laptops = []
urls_filename = "urls"
laptop_filename = "laptops"
kupindo_url = "https://www.kupindo.com/Racunari-i-oprema/Laptop-racunari-delovi-i-oprema/" \
			"Laptopovi/artikli/1473/cena_DESC_strana_"


if __name__ == "__main__":

	if file.check_does_file_exist(urls_filename):
		laptop_urls = LaptopUrl.load_laptop_urls(urls_filename)
		laptop_urls.extend(LaptopUrl.find_laptop_urls(laptop_urls, kupindo_url))
		file.save_data(urls_filename, "urls", laptop_urls)
	else:
		laptop_urls = LaptopUrl.find_laptop_urls(laptop_urls, kupindo_url)
		file.save_data(urls_filename, "urls", laptop_urls)
	
	if file.check_does_file_exist(laptop_filename):
		laptops = Laptop.load_laptops(laptop_filename)

	laptops.extend(Laptop.find_laptops(laptop_urls[:100], laptops))
	file.save_data(laptop_filename, "laptops", laptops)
