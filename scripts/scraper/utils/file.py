import csv
import random

from pathlib import Path
from config import settings


def check_file_name(file_name):

	my_file = Path(settings.scripts_root_path + "data/" + file_name + ".csv")

	if my_file.exists():
		file_name = file_name + str(random.randint(1, 1000) * 5)
		check_file_name(file_name)

	return file_name


def check_does_file_exist(file_name):
	my_file = Path(settings.scripts_root_path + "data/" + file_name + ".csv")

	if my_file.exists():
		return True
	else:
		return False


def save_data(file_name, purpose, collection):

	with open("data/" + file_name + '.csv', 'wt', 1) as my_file:
		writer = csv.writer(my_file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
		if purpose == 'urls':
			writer.writerow(['laptop_id', 'laptop_url'])

			for i in collection:
				writer.writerow([i.laptop_id, i.url])

		if purpose == 'laptops':
			writer.writerow([
				'laptop_brand', 'processor_brand', 'processor_number', 'number_of_cores', 'ram_generation',
				'ram_amount', 'storage_type', 'storage_amount', 'screen_size', "price", "condition",
				"url", "laptop_id"])

			for i in collection:
				writer.writerow([
					i.get_laptop_brand(), i.get_processor_brand(), i.get_processor_number(), i.get_processor_cores(),
					i.get_ram_generation(), i.get_ram_amount(), i.get_storage_type(), i.get_storage_amount(),
					i.get_screen_size(), i.get_price(), i.get_condition(), i.get_laptop_ulr(), i.get_laptop_id()])

			print("Total laptops saved: %d" % len(collection))

	my_file.close()
