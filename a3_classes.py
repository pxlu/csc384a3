class ItemProfile(object):

	def __init__(self, name="", price=-1, seasonal="",category="",rec_age=-1,brand="",is_entertainment=False, is_indoor=False):

		self.name = name
		self.price = price
		self.seasonal = seasonal
		self.category = category
		self.rec_age = rec_age
		# "HIDDEN" fields
		self.brand = brand
		self.is_entertainment = is_entertainment
		self.is_indoor = is_indoor

	def __str__(self):

		return "{} is an item in the {} category, with a price of {}, recommended age of {}, and seasonal type of {}.".format(self.name, self.category, self.price, self.rec_age, self.seasonal)

	def _detailed_info(self):

		return "============================================= \
        \nName: {}\
        \nPrice: {}\
        \nSeasonal: {}\
        \nCategory: {}\
        \nRecommended Age: {}\
        \nIs Entertainment? : {}\
        \nIs Indoor? : {}\
        \n=============================================".format(self.name, self.price, self.seasonal, self.category, self.rec_age, self.is_entertainment, self.is_indoor)