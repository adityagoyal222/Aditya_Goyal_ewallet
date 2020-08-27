from classes.connection import Connection


class Account:
	def __init__(self):
		self.db = Connection()

	def get_balance(self, username):
		qry = 'SELECT balance FROM normal_account WHERE username = %s;'
		values = (username,)
		balance_db = self.db.show_with_args(qry, values)
		return balance_db[0][0]

	def add_transaction(self, username, detail, amount):
		qry = 'SELECT account_id from normal_account WHERE username = %s'
		values = (username,)
		account_id = self.db.show_with_args(qry, values)
		qry2 = 'INSERT INTO transaction (account_id, detail, amount) VALUES (%s, %s, %s)'
		values2 = (account_id[0][0], detail, float(amount))
		self.db.iud(qry2, values2)
		return True

	def load_amount(self, username, bank, acc_no, amount):
		qry = 'UPDATE normal_account SET balance = balance + %s WHERE username = %s;'
		values = (amount, username)
		self.db.iud(qry, values)
		detail = f'Amount was loaded to wallet from {bank} Account No. {acc_no}.'
		self.add_transaction(username, detail, amount)
		return True

	def transfer_amount(self, username, receiver_username, amount):
		qry = 'UPDATE normal_account SET balance = balance - %s WHERE username = %s;'
		values = (amount, username)
		self.db.iud(qry, values)
		detail = f'Transferred money to {receiver_username} through e-wallet.'
		self.add_transaction(username, detail, amount)
		qry2 = 'UPDATE normal_account SET balance = balance + %s WHERE username = %s;'
		values2 = (amount, receiver_username)
		detail = f'Received money from {username} through e-wallet.'
		self.add_transaction(receiver_username, detail, amount)
		self.db.iud(qry2, values2)
		return True

	def pay_amount(self, username, servicename, amount):
		qry = 'UPDATE normal_account SET balance = balance - %s WHERE username = %s;'
		values = (float(amount), username)
		self.db.iud(qry, values)
		detail = f'Paid money to {servicename} for their service through e-wallet.'
		self.add_transaction(username, detail, float(amount))
		qry2 = 'UPDATE normal_account SET balance = balance + %s WHERE username = %s;'
		values2 = (float(amount) * 2 / 100, username)
		detail = f'Received cashback from {servicename} through e-wallet.'
		self.add_transaction(username, detail, float(amount) * 2 / 100)
		self.db.iud(qry2, values2)
		return True

	def show_transaction(self, username):
		qry = 'SELECT account_id from normal_account WHERE username = %s'
		values = (username,)
		account_id = self.db.show_with_args(qry, values)
		qry2 = 'SELECT transaction_id, detail, amount FROM transaction WHERE account_id = %s;'
		values2 = (account_id[0][0],)
		data = self.db.show_with_args(qry2, values2)
		return data