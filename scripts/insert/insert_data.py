import sys
reload(sys)
sys.setdefaultencoding('utf8')

import psycopg2
import csv
import datetime

from model.laptop import Laptop

root_path = sys.argv[1]

laptops = []


def load_laptops(file_name):

	with open(root_path + "data/" + file_name + '.csv', 'rt') as csvfile:
		loaded_data = list(csv.reader(csvfile, delimiter=","))[1:] # skip header

		for laptop in loaded_data:
			laptops.append(Laptop(laptop[0], laptop[1], laptop[2], laptop[3], laptop[4], laptop[5], laptop[6], laptop[7], laptop[8], laptop[9], laptop[10], laptop[11], laptop[12]))

		print "%d laptops loaded." % len(laptops)

	csvfile.close()


if __name__ == "__main__":

	load_laptops('laptops')
	try:
		conn = psycopg2.connect("host=server-api-db.c1yne3bmdpup.us-east-2.rds.amazonaws.com dbname=server_db user=ndakic password=postgres")
	except:
		print "I am unable to connect to the database"

	seq_con = conn.cursor()
	laptop_con = conn.cursor()
	scraper_con = conn.cursor()


	today = datetime.date.today()
	seq_con.execute("SELECT last_value FROM scraper_seq")
	next_value = seq_con.fetchall()[0][0]
	print next_value
	try:
		for laptop in laptops:

			check_laptop = "select l.brand from laptop l where id = %d" % long(laptop.laptop_id)
			laptop_con.execute(check_laptop)

			if len(laptop_con.fetchall()) == 0:
				values = '\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\'' % (laptop.laptop_id, laptop.laptop_brand, laptop.number_of_cores, laptop.price, laptop.processor_brand, laptop.processor_number, laptop.ram_amount, laptop.ram_generation, laptop.screen_size, laptop.storage_amount, laptop.storage_type, laptop.condition, laptop.url)
				insert_query = "INSERT INTO laptop (id, brand, cores, price, processor_brand, processor_model, ram_amount, ram_generation, screen_size, storage_amount, storage_type, condition, url) VALUES (%s)" % values
				print "Insert laptop:", insert_query
				laptop_con.execute(insert_query)
			else:
				print "Laptop %d already exist in DB." % long(laptop.laptop_id) 
		
		scraper_values = "\'%d\', \'%s\', \'%s\', \'%s\', \'%s\'" % (next_value, "kupindo", str(today), str(len(laptops)), "success")
		scraper_insert = "INSERT INTO scraper (id, source, date, total, status) values (%s)" % scraper_values
		print scraper_insert
		scraper_con.execute(scraper_insert)
	except Exception as e:
		print e
		scraper_values = "\'%d\', \'%s\', \'%s\', \'%s\', \'%s\'" % (next_value, "kupindo", str(today), str(len(laptops)), "error")
		scraper_con.execute("INSERT INTO scraper (id, source, date, total, status) values (%s)" % scraper_values)

  
	set_seq = "SELECT setval('scraper_seq', %d, true)" % (long(next_value) + 1)
	seq_con.execute(set_seq)

	conn.commit()

	conn.close()
