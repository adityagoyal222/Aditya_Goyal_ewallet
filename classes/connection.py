import mysql.connector
from tkinter import messagebox


class Connection:
	"""Class for database connection."""
	def __init__(self):
		self.connection = mysql.connector.connect(
			host="localhost",
			user="root",
			password="password",
			database="ewallet",
			port=3306,
		)
		self.cursor = self.connection.cursor()

	def iud(self, qry, values):  # Runs the insert/update/delete queries
		try:
			self.cursor.execute(qry, values)
			self.connection.commit()
			return True
		except Exception as e:
			messagebox.showerror('Error', e)

	def insert_with_id_return(self, qry, values):  # Runs the insert query and returns the id.
		try:
			self.cursor.execute(qry, values)
			self.cursor.commit(qry, values)
			return self.cursor.lastrowid
		except Exception as e:
			messagebox.showerror('Error', e)

	def show(self, qry):  # Runs the select queries.
		try:
			self.cursor.execute(qry)
			data = self.cursor.fetchall()
			return data
		except Exception as e:
			data = []
			messagebox.showerror('Error', e)
			return data

	def show_with_args(self, qry, values):  # Runs the select queries with specific fields.
		try:
			self.cursor.execute(qry, values)
			data = self.cursor.fetchall()
			return data
		except Exception as e:
			data = []
			messagebox.showerror('Error', e)
			return data
