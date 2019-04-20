class Link:
	def __init__(self, laptop_id, url):
		self.laptop_id = laptop_id
		self.url = url

	def display(self):
		return "id:", self.laptop_id, "url", self.url
