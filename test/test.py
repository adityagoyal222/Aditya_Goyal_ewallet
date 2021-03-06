from classes.Login import *
from classes.Signup import *
from classes.Service import *
from classes.Account import *

import unittest


class UnitTesting(unittest.TestCase):
	"""Unit Testing class"""
	def test_login(self):
		login = Login()
		actual_result = login.login_user('tester', 'tester')
		self.assertTrue(actual_result)

	def test_service(self):
		service = Service()
		actual_result = type(service.get_service_name())
		expected_result = type([])
		self.assertEqual(actual_result, expected_result)

	def test_load_amount(self):
		account = Account()
		actual_result = account.load_amount('tester', 'Janata Bank', '1234', 30000)
		self.assertTrue(actual_result)

	def test_pay_amount(self):
		account = Account()
		actual_result = account.pay_amount('tester', 'Nepal Electricity Board', 500)
		self.assertTrue(actual_result)

	def test_show_transaction(self):
		account = Account()
		actual_result = type(account.show_transaction('tester'))
		expected_result = type([])
		self.assertEqual(actual_result, expected_result)
