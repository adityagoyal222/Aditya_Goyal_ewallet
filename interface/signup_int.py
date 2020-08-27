from classes.Signup import Signup

from tkinter import *
from tkinter import messagebox


class SignupInterface:
	def __init__(self):
		self.signup = Signup()

		self.window = Tk()
		self.window.title("Sign Up to e-Wallet")
		self.window.geometry("350x350+0+0")

		self.label_main = Label(self.window, text="SIGN UP")
		self.label_main.place(x=160, y=15)

		self.label_username = Label(self.window, text="Username: ")
		self.label_username.place(x=10, y=60)

		self.entry_username = Entry(self.window, width=25)
		self.entry_username.place(x=130, y=60)

		self.label_fullname = Label(self.window, text="Full Name: ")
		self.label_fullname.place(x=10, y=100)

		self.entry_fullname = Entry(self.window, width=25)
		self.entry_fullname.place(x=130, y=100)

		self.label_password = Label(self.window, text="Password: ")
		self.label_password.place(x=10, y=140)

		self.entry_password = Entry(self.window, width=25, show="*")
		self.entry_password.place(x=130, y=140)

		self.label_confirm_password = Label(self.window, text="Confirm Password: ")
		self.label_confirm_password.place(x=10, y=180)

		self.entry_confirm_password = Entry(self.window, width=25, show="*")
		self.entry_confirm_password.place(x=130, y=180)

		self.label_phone = Label(self.window, text="Phone No.")
		self.label_phone.place(x=10, y=220)

		self.entry_phone = Entry(self.window, width=25)
		self.entry_phone.place(x=130, y=220)

		self.label_email = Label(self.window, text="Email")
		self.label_email.place(x=10, y=260)

		self.entry_email = Entry(self.window, width=25)
		self.entry_email.place(x=130, y=260)

		self.button_to_login = Button(self.window, text="Back to Login", width=10, command=self.back_to_login)
		self.button_to_login.place(x=10, y=300)

		self.button_signup = Button(self.window, text="Sign Up", width=10, command=self.signup_user)
		self.button_signup.place(x=130, y=300)

		self.button_reset = Button(self.window, text="Reset", width=10, command=self.reset)
		self.button_reset.place(x=260, y=300)

		self.window.mainloop()

	def signup_user(self):
		username = self.entry_username.get()
		fullname = self.entry_fullname.get()
		password = self.entry_password.get()
		confirm_pass = self.entry_confirm_password.get()
		phone = self.entry_phone.get()
		email = self.entry_email.get()
		if username != '' and fullname != '' and password != '' and phone != '' and email != '':
			if confirm_pass == password:
				if self.signup.signup_user(username, fullname, password, phone, email):
					messagebox.showinfo("Register", "Signed up successfully!")
				else:
					messagebox.showerror("Register", "Sign up unsuccessful.")
			else:
				messagebox.showerror('Register', 'Confirm your password correctly')
		else:
			messagebox.showerror('Register', 'Please fill out all the fields.')

	def reset(self):
		self.entry_username.delete(0, END)
		self.entry_fullname.delete(0, END)
		self.entry_password.delete(0, END)
		self.entry_confirm_password.delete(0, END)
		self.entry_phone.delete(0, END)
		self.entry_email.delete(0, END)

	def back_to_login(self):
		self.window.destroy()
		from interface.login_int import LoginInterface
		LoginInterface()
