from classes.Service import Service

from tkinter import *
from tkinter import messagebox


class ServiceInterface:
	def __init__(self):
		self.service = Service()

		self.window = Tk()
		self.window.geometry("350x350+0+0")
		self.window.title("Register as Business or Service")

		self.label_main = Label(self.window, text="REGISTER")
		self.label_main.place(x=160, y=15)

		self.label_servicename = Label(self.window, text="Servicename: ")
		self.label_servicename.place(x=10, y=60)

		self.entry_servicename = Entry(self.window, width=25)
		self.entry_servicename.place(x=130, y=60)

		self.label_servicetype = Label(self.window, text="Service Type: ")
		self.label_servicetype.place(x=10, y=100)

		self.entry_servicetype = Entry(self.window, width=25)
		self.entry_servicetype.place(x=130, y=100)

		self.label_phone = Label(self.window, text="Phone No.")
		self.label_phone.place(x=10, y=140)

		self.entry_phone = Entry(self.window, width=25)
		self.entry_phone.place(x=130, y=140)

		self.label_email = Label(self.window, text="Email")
		self.label_email.place(x=10, y=180)

		self.entry_email = Entry(self.window, width=25)
		self.entry_email.place(x=130, y=180)

		self.button_to_login = Button(self.window, text="Back to Login", width=10, command=self.back_to_login)
		self.button_to_login.place(x=10, y=250)

		self.button_register_service = Button(self.window, text="Register", width=10, command=self.register_service)
		self.button_register_service.place(x=130, y=250)

		self.button_reset = Button(self.window, text="Reset", width=10, command=self.reset)
		self.button_reset.place(x=260, y=250)

		self.window.mainloop()

	def back_to_login(self):
		self.window.destroy()
		from interface.login_int import LoginInterface
		LoginInterface()

	def register_service(self):
		servicename = self.entry_servicename.get()
		servicetype = self.entry_servicetype.get()
		phone = self.entry_phone.get()
		email = self.entry_email.get()
		if servicename != '' and servicetype != '' and phone != '' and phone != '' and email != '':
			if self.service.register_service(servicename, servicetype, phone, email):
				messagebox.showinfo("Register", "Registered successfully!")
			else:
				messagebox.showerror("Register", "Register unsuccessful.")
		else:
			messagebox.showerror('Register', 'Please fill out all the fields.')

	def reset(self):
		self.entry_servicename.delete(0, END)
		self.entry_servicetype.delete(0, END)
		self.entry_phone.delete(0, END)
		self.entry_email.delete(0, END)
