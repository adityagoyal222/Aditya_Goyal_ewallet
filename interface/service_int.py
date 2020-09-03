from classes.Service import Service

from tkinter import *
from tkinter import messagebox


class ServiceInterface:
	"""Class to show Service Window"""
	def __init__(self):
		self.service = Service()

		self.window = Tk()
		self.window.geometry("350x350+0+0")
		self.window.title("Register as Business or Service")
		self.window['background'] = 'white'

		self.label_main = Label(self.window, text="REGISTER", bg="white", fg="black", font=('Comic Sans MS', 20, 'bold'))
		self.label_main.place(x=130, y=5)

		self.label_servicename = Label(self.window, text="Servicename: ", bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_servicename.place(x=10, y=60)

		self.entry_servicename = Entry(self.window, width=20, borderwidth=0, bg="#F1F1F1", font=('Comic Sans MS', 11,))
		self.entry_servicename.place(x=130, y=60, height=30)

		self.label_servicetype = Label(self.window, text="Service Type: ", bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_servicetype.place(x=10, y=100)

		self.entry_servicetype = Entry(self.window, width=20, borderwidth=0, bg="#F1F1F1", font=('Comic Sans MS', 11,))
		self.entry_servicetype.place(x=130, y=100, height=30)

		self.label_phone = Label(self.window, text="Phone No.", bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_phone.place(x=10, y=140)

		self.entry_phone = Entry(self.window, width=20, borderwidth=0, bg="#F1F1F1", font=('Comic Sans MS', 11,))
		self.entry_phone.place(x=130, y=140, height=30)

		self.label_email = Label(self.window, text="Email", bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_email.place(x=10, y=180)

		self.entry_email = Entry(self.window, width=20, borderwidth=0, bg="#F1F1F1", font=('Comic Sans MS', 11,))
		self.entry_email.place(x=130, y=180, height=30)

		self.button_to_login = Button(self.window, text="Back to Login", width=10, bg="#F9F9F9", fg="#2196F3", font=('Comic Sans MS', 8), relief=FLAT, command=self.back_to_login)
		self.button_to_login.place(x=10, y=250)

		self.button_register_service = Button(self.window, text="Register", width=10, bg="#2196F3", fg="white", font=('Comic Sans MS', 8), relief=FLAT, command=self.register_service)
		self.button_register_service.place(x=130, y=250)

		self.button_reset = Button(self.window, text="Reset", width=10, bg="#F9F9F9", fg="#2196F3", font=('Comic Sans MS', 8), relief=FLAT, command=self.reset)
		self.button_reset.place(x=260, y=250)

		self.window.mainloop()

	def back_to_login(self):  # For Login Button
		self.window.destroy()
		from interface.login_int import LoginInterface
		LoginInterface()  # Opens Login window

	def register_service(self):  # For Register Button
		servicename = self.entry_servicename.get()
		servicetype = self.entry_servicetype.get()
		phone = self.entry_phone.get()
		email = self.entry_email.get()
		if servicename != '' and servicetype != '' and phone != '' and phone != '' and email != '':  # Validation code
			if self.service.register_service(servicename, servicetype, phone, email):
				messagebox.showinfo("Register", "Registered successfully!")
			else:
				messagebox.showerror("Register", "Register unsuccessful.")
		else:
			messagebox.showerror('Register', 'Please fill out all the fields.')

	def reset(self):  # For Reset Button
		self.entry_servicename.delete(0, END)
		self.entry_servicetype.delete(0, END)
		self.entry_phone.delete(0, END)
		self.entry_email.delete(0, END)
