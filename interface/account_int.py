from classes.connection import Connection
from classes.Account import Account
from classes.Service import Service

from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox


class AccountInterface:
	def __init__(self, username):
		self.window = Tk()
		self.username = username
		self.account = Account()
		self.balance = self.account.get_balance(self.username)
		self.service = Service()

		# Define window geometry and add widgets
		self.window.geometry("500x500+0+0")
		self.window.title("E-Wallet")

		self.label_main = Label(self.window, text="E-Wallet")
		self.label_main.place(x=10, y=10)

		self.label_balance = Label(self.window, text="Balance (in Rs.):")
		self.label_balance.place(x=10, y=30)

		self.label_balance_amount = Label(self.window, text=self.balance)
		self.label_balance_amount.place(x=130, y=30)

		# Creates Notebook and adds Tabs
		self.notebook = ttk.Notebook(self.window)
		self.notebook.place(x=10, y=60, width=480, height=400)
		self.load_amount_tab = Frame(self.notebook)
		self.transfer_tab = Frame(self.notebook)
		self.pay_tab = Frame(self.notebook)
		self.transaction_tab = Frame(self.notebook)
		self.notebook.add(self.load_amount_tab, text='Load Money')
		self.notebook.add(self.transfer_tab, text='Transfer Money')
		self.notebook.add(self.pay_tab, text='Pay to Business/Service')
		self.notebook.add(self.transaction_tab, text='Transaction History')

		# Adding widgets to Load Money tab
		self.label_bank = Label(self.load_amount_tab, text="Bank: ")
		self.label_bank.place(x=10, y=30)

		self.entry_bank = Entry(self.load_amount_tab, width=25)
		self.entry_bank.place(x=130, y=30)

		self.label_acc_id = Label(self.load_amount_tab, text="Account ID.: ")
		self.label_acc_id.place(x=10, y=80)

		self.entry_acc_id = Entry(self.load_amount_tab, width=25)
		self.entry_acc_id.place(x=130, y=80)

		self.label_load_amount = Label(self.load_amount_tab, text="Amount (in Rs.): ")
		self.label_load_amount.place(x=10, y=130)

		self.entry_load_amount = Entry(self.load_amount_tab, width=15)
		self.entry_load_amount.place(x=130, y=130)

		self.button_load_amount = Button(self.load_amount_tab, text="Load", command=self.load_amount, width=10)
		self.button_load_amount.place(x=160, y=200)

		self.button_load_reset = Button(self.load_amount_tab, text="Reset", command=self.load_reset, width=10)
		self.button_load_reset.place(x=160, y=250)

		# Add widgets to Transfer tab
		self.label_receiver_username = Label(self.transfer_tab, text="Receiver Username:")
		self.label_receiver_username.place(x=10, y=30)

		self.entry_receiver_username = Entry(self.transfer_tab, width=25)
		self.entry_receiver_username.place(x=130, y=30)

		self.label_transfer_amount = Label(self.transfer_tab, text="Amount:")
		self.label_transfer_amount.place(x=10, y=80)

		self.entry_transfer_amount = Entry(self.transfer_tab, width=15)
		self.entry_transfer_amount.place(x=130, y=80)

		self.button_transfer_amount = Button(self.transfer_tab, text="Pay", command=self.transfer_amount, width=10)
		self.button_transfer_amount.place(x=160, y=200)

		self.button_transfer_reset = Button(self.transfer_tab, text="Reset", command=self.transfer_reset, width=10)
		self.button_transfer_reset.place(x=160, y=250)

		# Add widgets to Payment tab
		self.label_cashback = Label(self.pay_tab, fg="green", text="Receive 2% cashback on any payment for services through our e-wallet")
		self.label_cashback.place(x=10, y=30)

		self.label_service_name = Label(self.pay_tab, text="Business/Service:")
		self.label_service_name.place(x=10, y=100)

		self.combo_service_name = ttk.Combobox(self.pay_tab, width=25)
		self.combo_service_name['values'] = self.load_services()
		self.combo_service_name.place(x=130, y=100)

		self.label_payment_amount = Label(self.pay_tab, text="Amount:")
		self.label_payment_amount.place(x=10, y=150)

		self.entry_payment_amount = Entry(self.pay_tab, width=15)
		self.entry_payment_amount.place(x=130, y=150)

		self.button_pay_amount = Button(self.pay_tab, text="Pay", width=10, command=self.pay_amount)
		self.button_pay_amount.place(x=130, y=200)

		self.button_pay_reset = Button(self.pay_tab, text="Reset", width=10, command=self.pay_reset)
		self.button_pay_reset.place(x=130, y=250)

		# Add widgets to Transaction History tab
		self.label_search = Label(self.transaction_tab, text="Search:")
		self.label_search.place(x=10, y=10)

		self.entry_search = Entry(self.transaction_tab, width=25)
		self.entry_search.place(x=130, y=10)
		self.entry_search.bind('<KeyRelease>', self.search_event)

		self.show_all = Button(self.transaction_tab, text="Show All", width=10, command=self.show_transaction)
		self.show_all.place(x=150, y=60)

		self.transaction_tree = ttk.Treeview(self.transaction_tab, selectmode="browse", columns=('ID', 'Transaction Detail', 'Amount'), show='headings')
		self.transaction_tree.place(x=10, y=100, width=460, height=260)
		self.show_transaction()

		self.vscrollbar = ttk.Scrollbar(self.transaction_tab, orient="vertical", command=self.transaction_tree.yview)
		self.vscrollbar.pack(side="right", fill='x')

		self.transaction_tree.configure(yscrollcommand=self.vscrollbar.set)
		self.transaction_tree.heading('ID', text="ID")
		self.transaction_tree.column('ID', minwidth=0, width=5)
		self.transaction_tree.heading('Transaction Detail', text='Transaction Detail')
		self.transaction_tree.column('Transaction Detail', minwidth=0, width=350)
		self.transaction_tree.heading('Amount', text="Amount")
		self.transaction_tree.column('Amount', minwidth=0, width=25)

		self.window.mainloop()

	def load_amount(self):
		username = self.username
		bank = self.entry_bank.get()
		acc_id = self.entry_acc_id.get()
		load_amount = self.entry_load_amount.get()
		if username != '' and bank != '' and acc_id != '' and load_amount != '':
			if float(load_amount) > 0.0:
				if self.account.load_amount(username, bank, acc_id, float(load_amount)):
					self.balance = self.account.get_balance(username)
					self.label_balance_amount.config(text=self.balance)
					self.show_transaction()
					messagebox.showinfo('Load Amount', 'Amount Loaded successfully.')
				else:
					messagebox.showerror('Load Amount', 'Amount could not be loaded.')
			else:
				messagebox.showerror('Load Amount', 'Amount must be positive.')
		else:
			messagebox.showerror('Load Amount', 'Please fill out all the fields.')

	def load_reset(self):
		self.entry_load_amount.delete(0, END)
		self.entry_acc_id.delete(0, END)
		self.entry_bank.delete(0, END)

	def transfer_amount(self):
		username = self.username
		receiver_username = self.entry_receiver_username.get()
		transfer_amount = self.entry_transfer_amount.get()
		if username != '' and receiver_username != '' and transfer_amount != '':
			if float(transfer_amount) > 0.0:
				if self.account.transfer_amount(username, receiver_username, float(transfer_amount)):
					self.balance = self.account.get_balance(username)
					self.label_balance_amount.config(text=self.balance)
					self.show_transaction()
					messagebox.showinfo('Transfer Amount', 'Amount transferred successfully.')
				else:
					messagebox.showerror('Transfer Amount', 'Amount transfer was unsuccessful.')
			else:
				messagebox.showerror('Transfer Amount', 'Amount must be positive')
		else:
			messagebox.showerror('Transfer Amount', 'Please fill out all the fields.')

	def transfer_reset(self):
		self.entry_receiver_username.delete(0, END)
		self.entry_transfer_amount.delete(0, END)

	def load_services(self):
		service = []
		for i in self.service.get_service_name():
			for j in i:
				service.append(j)
		return service

	def pay_amount(self):
		username = self.username
		service_name = self.combo_service_name.get()
		payment_amount = self.entry_payment_amount.get()
		if username != '' and service_name != '' and payment_amount != '':
			if float(payment_amount) > 0:
				if self.account.pay_amount(username, service_name, float(payment_amount)):
					self.balance = self.account.get_balance(username)
					self.label_balance_amount.config(text=self.balance)
					self.show_transaction()
					messagebox.showinfo('Payment', 'Amount paid successfully.')
				else:
					messagebox.showerror('Payment', 'Amount payment was unsuccessful.')
			else:
				messagebox.showerror('Payment', 'Amount must be positive.')
		else:
			messagebox.showerror('Payment', 'Please fill out all the fields.')

	def pay_reset(self):
		self.entry_payment_amount.delete(0, END)

	def show_transaction(self):
		for i in self.transaction_tree.get_children():
			self.transaction_tree.delete(i)
		data = self.account.show_transaction(self.username)
		for i in data:
			self.transaction_tree.insert("", END, values=(i[0], i[1], i[2]))

	def quick_sort(self, array):
		less = []
		equal = []
		greater = []

		if len(array) > 1:
			pivot = array[0]
			for x in array:
				if x < pivot:
					less.append(x)
				elif x == pivot:
					equal.append(x)
				elif x > pivot:
					greater.append(x)
			return self.quick_sort(less) + equal + self.quick_sort(greater)

		else:
			return array

	def search_event(self, event):
		for i in self.transaction_tree.get_children():
			self.transaction_tree.delete(i)
		data = self.account.show_transaction(self.username)
		for i in data:
			list1 = i[1].split()
			sorted_list1 = self.quick_sort(list1)
			start = 0
			end = len(sorted_list1) - 1
			index = -1
			while start <= end:
				mid = (start + end) // 2
				if sorted_list1[mid] == self.entry_search.get():
					index = mid
					self.transaction_tree.insert("", END, values=(i[0], i[1], i[2]))
					break
				elif sorted_list1[mid] > self.entry_search.get():
					end = mid - 1
				else:
					start = mid + 1
