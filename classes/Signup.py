from classes.connection import Connection


class Signup:
	def __init__(self):
		self.db = Connection()
		self.username = ''

	def signup_user(self, username, fullname, password, phone, email, balance=0.0):
		self.username = username
		qry1 = "INSERT INTO normal_user VALUES (%s, %s, %s, %s, %s);"
		values1 = (self.username, fullname, password, phone, email)
		qry2 = "INSERT INTO normal_account (username, balance) VALUES (%s, %s);"
		values2 = (self.username, balance)
		self.db.iud(qry1, values1)
		if self.db.iud(qry2, values2):
			return True
