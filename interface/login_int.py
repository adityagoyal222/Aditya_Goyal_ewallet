from classes.Login import Login
from interface.signup_int import SignupInterface
from interface.account_int import AccountInterface
from interface.service_int import ServiceInterface

from tkinter import *
from tkinter import messagebox


class LoginInterface:
	def __init__(self):
		self.login = Login()

		self.window = Tk()
		self.window.title("Login to e-Wallet")
		self.window.geometry("400x400+0+0")

		self.label_main = Label(self.window, text="Login")
		self.label_main.place(x=160, y=15)

		self.delete_user_btn = Button(self.window, text="Delete User", width=15, fg="red", command=self.delete_user)
		self.delete_user_btn.place(x=240, y=15)

		self.label_username = Label(self.window, text="Username: ")
		self.label_username.place(x=10, y=60)

		self.entry_username = Entry(self.window, width=25)
		self.entry_username.place(x=130, y=60)

		self.label_password = Label(self.window, text="Password: ")
		self.label_password.place(x=10, y=110)

		self.entry_password = Entry(self.window, width=25, show="*")
		self.entry_password.place(x=130, y=110)

		self.button_reset = Button(self.window, text="Reset", width=10, command=self.reset)
		self.button_reset.place(x=50, y=220)

		self.button_login = Button(self.window, text="Login", width=10, command=self.login_user)
		self.button_login.place(x=220, y=220)

		self.label_register = Label(self.window, text="Don't have an account?", fg="red")
		self.label_register.place(x=130, y=280)

		self.button_to_signup = Button(self.window, text="Register as User", width=15, fg="red", command=self.go_to_signup)
		self.button_to_signup.place(x=130, y=310)

		self.label_or = Label(self.window, text="or", fg="red")
		self.label_or.place(x=175, y=340)

		self.button_register_service = Button(self.window, text="Register as Service", width=15, fg="red", command=self.register_service)
		self.button_register_service.place(x=130, y=360)

		self.window.mainloop()

	def login_user(self):
		username = self.entry_username.get()
		password = self.entry_password.get()
		if username != '' and password != '':
			if self.login.login_user(username, password):
				messagebox.showinfo("Login", "Logged in successfully!")
				self.window.destroy()
				AccountInterface(username)
				return True
		return False


	def delete_user(self):
		username = self.entry_username.get()
		password = self.entry_password.get()
		if username != '' and password != '':
			if self.login.delete_user(username, password):
				messagebox.showinfo('Delete User', 'User Deleted successfully!')

	def reset(self):
		self.entry_username.delete(0, END)
		self.entry_password.delete(0, END)

	def go_to_signup(self):
		self.window.destroy()
		SignupInterface()

	def register_service(self):
		self.window.destroy()
		ServiceInterface()


login = LoginInterface()
