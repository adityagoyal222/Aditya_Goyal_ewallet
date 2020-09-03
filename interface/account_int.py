from classes.connection import Connection
from classes.Account import Account
from classes.Service import Service

from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox


class AccountInterface:
	"""Class to show Account Window"""
	def __init__(self, username):
		self.window = Tk()
		self.username = username
		self.account = Account()
		self.balance = self.account.get_balance(self.username)
		self.service = Service()

		# Define window geometry and add widgets
		self.window.geometry("500x500+0+0")
		self.window.title("E-Wallet")
		self.window['background'] = 'white'

		self.label_main = Label(self.window, text="E-Wallet", bg="white", fg="black", font=('Comic Sans MS', 20, 'bold'))
		self.label_main.place(x=220, y=5)

		self.label_balance = Label(self.window, text="Balance (in Rs.):", bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_balance.place(x=10, y=60)

		self.label_balance_amount = Label(self.window, text=self.balance, bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_balance_amount.place(x=130, y=60)

		# Creates Notebook and adds Tabs
		self.notebook = ttk.Notebook(self.window)
		self.notebook.place(x=10, y=100, width=480, height=400)
		self.load_amount_tab = Frame(self.notebook, background="white")
		self.transfer_tab = Frame(self.notebook, background="white")
		self.pay_tab = Frame(self.notebook, background="white")
		self.transaction_tab = Frame(self.notebook, background="white")
		self.notebook.add(self.load_amount_tab, text='Load Money')
		self.notebook.add(self.transfer_tab, text='Transfer Money')
		self.notebook.add(self.pay_tab, text='Pay to Business/Service')
		self.notebook.add(self.transaction_tab, text='Transaction History')

		# Adding widgets to Load Money tab
		self.label_bank = Label(self.load_amount_tab, text="Bank: ", bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_bank.place(x=10, y=30)

		self.entry_bank = Entry(self.load_amount_tab, width=20, borderwidth=0, bg="#F1F1F1", font=('Comic Sans MS', 11,))
		self.entry_bank.place(x=160, y=30, height=30)

		self.label_acc_id = Label(self.load_amount_tab, text="Account ID.: ", bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_acc_id.place(x=10, y=80)

		self.entry_acc_id = Entry(self.load_amount_tab, width=20, borderwidth=0, bg="#F1F1F1", font=('Comic Sans MS', 11,))
		self.entry_acc_id.place(x=160, y=80, height=30)

		self.label_load_amount = Label(self.load_amount_tab, text="Amount (in Rs.): ", bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_load_amount.place(x=10, y=130)

		self.entry_load_amount = Entry(self.load_amount_tab, width=20, borderwidth=0, bg="#F1F1F1", font=('Comic Sans MS', 11,))
		self.entry_load_amount.place(x=160, y=130, height=30)

		self.button_load_amount = Button(self.load_amount_tab, text="Load", bg="#2196F3", fg="white", font=('Comic Sans MS', 8), relief=FLAT, command=self.load_amount, width=10)
		self.button_load_amount.place(x=160, y=200)

		self.button_load_reset = Button(self.load_amount_tab, text="Reset", bg="#F9F9F9", fg="#2196F3", font=('Comic Sans MS', 8), relief=FLAT, command=self.load_reset, width=10)
		self.button_load_reset.place(x=160, y=250)

		# Add widgets to Transfer tab
		self.label_receiver_username = Label(self.transfer_tab, text="Receiver Username:", bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_receiver_username.place(x=10, y=30)

		self.entry_receiver_username = Entry(self.transfer_tab, width=20, borderwidth=0, bg="#F1F1F1", font=('Comic Sans MS', 11,))
		self.entry_receiver_username.place(x=160, y=30, height=30)

		self.label_transfer_amount = Label(self.transfer_tab, text="Amount:", bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_transfer_amount.place(x=10, y=80)

		self.entry_transfer_amount = Entry(self.transfer_tab, width=20, borderwidth=0, bg="#F1F1F1", font=('Comic Sans MS', 11,))
		self.entry_transfer_amount.place(x=160, y=80, height=30)

		self.button_transfer_amount = Button(self.transfer_tab, text="Transfer", bg="#2196F3", fg="white", font=('Comic Sans MS', 8), relief=FLAT, command=self.transfer_amount, width=10)
		self.button_transfer_amount.place(x=160, y=200)

		self.button_transfer_reset = Button(self.transfer_tab, text="Reset", bg="#F9F9F9", fg="#2196F3", font=('Comic Sans MS', 8), relief=FLAT, command=self.transfer_reset, width=10)
		self.button_transfer_reset.place(x=160, y=250)

		# Add widgets to Payment tab
		self.label_cashback = Label(self.pay_tab, text="Receive 2% cashback on any payment for services through our e-wallet", bg="white", fg="green", font=('Comic Sans MS', 9,))
		self.label_cashback.place(x=10, y=30)

		self.label_service_name = Label(self.pay_tab, text="Business/Service:", bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_service_name.place(x=10, y=100)

		self.combo_service_name = ttk.Combobox(self.pay_tab, width=25)
		self.combo_service_name['values'] = self.load_services()
		self.combo_service_name.place(x=160, y=100)

		self.label_payment_amount = Label(self.pay_tab, text="Amount:", bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_payment_amount.place(x=10, y=150)

		self.entry_payment_amount = Entry(self.pay_tab, width=20, borderwidth=0, bg="#F1F1F1", font=('Comic Sans MS', 11,))
		self.entry_payment_amount.place(x=160, y=150, height=30)

		self.button_pay_amount = Button(self.pay_tab, text="Pay", width=10, bg="#2196F3", fg="white", font=('Comic Sans MS', 8), relief=FLAT, command=self.pay_amount)
		self.button_pay_amount.place(x=130, y=200)

		self.button_pay_reset = Button(self.pay_tab, text="Reset", width=10, bg="#F9F9F9", fg="#2196F3", font=('Comic Sans MS', 8), relief=FLAT, command=self.pay_reset)
		self.button_pay_reset.place(x=130, y=250)

		# Add widgets to Transaction History tab
		self.label_search = Label(self.transaction_tab, text="Search:", bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_search.place(x=10, y=10)

		self.entry_search = Entry(self.transaction_tab, width=20, borderwidth=0, bg="#F1F1F1", font=('Comic Sans MS', 11,))
		self.entry_search.place(x=130, y=10, height=30)
		self.entry_search.bind('<KeyRelease>', self.search_event)

		self.show_all = Button(self.transaction_tab, text="Show All", width=10, bg="#2196F3", fg="white", font=('Comic Sans MS', 8), relief=FLAT, command=self.show_transaction)
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

	def load_amount(self):  # For Load Button
		username = self.username
		bank = self.entry_bank.get()
		acc_id = self.entry_acc_id.get()
		load_amount = self.entry_load_amount.get()
		if username != '' and bank != '' and acc_id != '' and load_amount != '':  # Validation code
			if float(load_amount) > 0.0:  # Checks if loaded amount is positive
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

	def load_reset(self):  # For Reset Button
		self.entry_load_amount.delete(0, END)
		self.entry_acc_id.delete(0, END)
		self.entry_bank.delete(0, END)

	def transfer_amount(self):  # For Transfer Button
		username = self.username
		receiver_username = self.entry_receiver_username.get()
		transfer_amount = self.entry_transfer_amount.get()
		if username != '' and receiver_username != '' and transfer_amount != '':  # Validation code
			if float(transfer_amount) > 0.0:  # Checks if transferred amount is positive.
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

	def transfer_reset(self):  # For Reset Button
		self.entry_receiver_username.delete(0, END)
		self.entry_transfer_amount.delete(0, END)

	def load_services(self):  # To load the list of services registered in the application.
		service = []
		for i in self.service.get_service_name():
			for j in i:
				service.append(j)
		return service

	def pay_amount(self):  # For Pay to Service Button
		username = self.username
		service_name = self.combo_service_name.get()
		payment_amount = self.entry_payment_amount.get()
		if username != '' and service_name != '' and payment_amount != '':  # Validation code
			if float(payment_amount) > 0:  # Checks if the paid amount is positive.
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

	def pay_reset(self):  # For Reset Button
		self.entry_payment_amount.delete(0, END)

	def show_transaction(self):  # To show corresponding transactions in the applications
		for i in self.transaction_tree.get_children():
			self.transaction_tree.delete(i)
		data = self.account.show_transaction(self.username)
		for i in data:
			self.transaction_tree.insert("", END, values=(i[0], i[1], i[2]))

	def quick_sort(self, array):  # Algorithm to sort the list of generated array for searching
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
			return self.quick_sort(less) + equal + self.quick_sort(greater)  # returns the sorted array

		else:
			return array

	def search_event(self, event):  # For the Search feature
		for i in self.transaction_tree.get_children():
			self.transaction_tree.delete(i)
		data = self.account.show_transaction(self.username)
		for i in data:  # Binary search
			list1 = i[1].split()
			sorted_list1 = self.quick_sort(list1)
			start = 0
			end = len(sorted_list1) - 1
			index = -1
			while start <= end:
				mid = (start + end) // 2
				if sorted_list1[mid] == self.entry_search.get():
					index = mid
					# shows the transactions that match the search
					self.transaction_tree.insert("", END, values=(i[0], i[1], i[2]))
					break
				elif sorted_list1[mid] > self.entry_search.get():
					end = mid - 1
				else:
					start = mid + 1
