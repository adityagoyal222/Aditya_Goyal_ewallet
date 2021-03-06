from classes.connection import Connection


class Service:
	"""Class to implement Service/Business feature"""
	def __init__(self):
		self.db = Connection()
		self.service_name = ''

	def register_service(self, service_name, service_type, phone, email, balance=0.0):
		# Registers the service into the database
		self.service_name = service_name
		# Query to insert service into database
		qry = "INSERT INTO service_account VALUES (%s, %s, %s, %s, %s);"
		values = (self.service_name, service_type, phone, email, balance)
		self.db.iud(qry, values)
		return True

	def get_service_name(self):
		# Gathers the list of all services registered in the database
		qry = "SELECT servicename from service_account;"
		servicename = self.db.show(qry)
		return servicename
