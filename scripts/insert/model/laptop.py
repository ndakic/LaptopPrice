class Laptop:
	def __init__(self, laptop_brand, processor_brand, processor_number, number_of_cores, ram_generation, ram_amount, storage_type, storage_amount, screen_size, price, condition, url, laptop_id):
		self.laptop_brand = laptop_brand
		self.processor_brand = processor_brand
		self.processor_number = processor_number
		self.number_of_cores = number_of_cores
		self.ram_generation = ram_generation
		self.ram_amount = ram_amount
		self.storage_type = storage_type
		self.storage_amount = storage_amount
		self.screen_size = screen_size
		self.price = price
		self.condition = condition
		self.url = url
		self.laptop_id = laptop_id

	def display(self):
		return "laptop_id", self.laptop_id
