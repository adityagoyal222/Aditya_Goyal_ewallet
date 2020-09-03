from classes.connection import Connection


class Signup:
	"""Class to implement Signup feature."""
	def __init__(self):
		self.db = Connection()
		self.username = ''

	def signup_user(self, username, fullname, password, phone, email, balance=0.0):  # Registers the User in database
		self.username = username
		# Query to insert user information
		qry1 = "INSERT INTO normal_user VALUES (%s, %s, %s, %s, %s);"
		values1 = (self.username, fullname, password, phone, email)
		# Query to create e-wallet account
		qry2 = "INSERT INTO normal_account (username, balance) VALUES (%s, %s);"
		values2 = (self.username, balance)
		self.db.iud(qry1, values1)
		if self.db.iud(qry2, values2):
			return True
