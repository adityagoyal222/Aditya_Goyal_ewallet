from classes.connection import Connection

from tkinter import messagebox


class Login:
	"""Class to implement Login feature."""
	def __init__(self):
		self.db = Connection()
		self.username = ''
		self.password = ''

	def login_user(self, username, password):  # Logs the user into the application
		self.username = username
		qry = 'SELECT password FROM normal_user WHERE username = %s;'
		values = (self.username,)
		passwd = self.db.show_with_args(qry, values)
		if not passwd:  # Checks if username exists
			messagebox.showerror('Login', 'Username does not exist.')
			return False
		else:
			if password == passwd[0][0]:  # Checks if the password matches
				self.password = password
				return True
			else:
				messagebox.showerror('Login', 'Please enter correct password')
				return False

	def delete_user(self, username, password):  # Method to delete user
		self.username = username
		qry = 'SELECT password FROM normal_user WHERE username = %s;'
		values = (self.username,)
		passwd = self.db.show_with_args(qry, values)
		if not passwd:  # Checks if username exists
			messagebox.showerror('Delete User', 'Username does not exist.')
		else:
			if password == passwd[0][0]:  # Checks if the password matches
				# Gets the account_id for the given username
				qry1 = 'SELECT account_id FROM normal_account WHERE username = %s;'
				values1 = (self.username,)
				account_id = self.db.show_with_args(qry1, values1)
				# Retrieves the transaction history.
				qry_optional = 'SELECT account_id FROM transaction WHERE account_id = %s;'
				values_optional = (account_id[0][0],)
				optional_out = self.db.show_with_args(qry_optional, values_optional)
				if optional_out:
					# If the user has any transaction history, query deletes it.
					qry2 = 'DELETE FROM transaction WHERE account_id = %s;'
					values2 = (account_id[0][0],)
					self.db.iud(qry2, values2)
				# Deletes the account.
				qry3 = 'DELETE FROM normal_account WHERE username = %s;'
				values3 = (self.username,)
				self.db.iud(qry3, values3)
				# Deletes the user information from the database
				qry4 = 'DELETE FROM normal_user WHERE username = %s;'
				values4 = (self.username,)
				if self.db.iud(qry4, values4):
					return True
			else:
				messagebox.showerror('Delete User', 'Please enter correct password')
				return False
