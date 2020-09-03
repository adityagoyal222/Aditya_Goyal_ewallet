from classes.Login import Login
from interface.signup_int import SignupInterface
from interface.account_int import AccountInterface
from interface.service_int import ServiceInterface

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


class LoginInterface:
	"""Class to show Login Window."""
	def __init__(self):
		self.login = Login()

		self.window = Tk()
		self.window.title("Login to e-Wallet")
		self.window.geometry("400x400+0+0")
		self.window['background'] = 'white'
		self.show_img = ImageTk.PhotoImage(Image.open("show.png").resize((27, 27)))
		self.hide_img = ImageTk.PhotoImage(Image.open("hide.png").resize((27, 27)))
		self.show_state = False

		self.label_main = Label(self.window, text="Login", bg="white", fg="black", font=('Comic Sans MS', 20, 'bold'))
		self.label_main.place(x=160, y=5)

		self.delete_user_btn = Button(self.window, text="Delete User", width=10, bg="#F9F9F9", fg="red", font=('Comic Sans MS', 8), relief=FLAT, command=self.delete_user)
		self.delete_user_btn.place(x=280, y=15)

		self.label_username = Label(self.window, text="Username: ", bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_username.place(x=40, y=90)

		self.entry_username = Entry(self.window, width=20, borderwidth=0, bg="#F1F1F1", font=('Comic Sans MS', 11,))
		self.entry_username.place(x=150, y=90, height=30)

		self.label_password = Label(self.window, text="Password: ", bg="white", fg="black", font=('Comic Sans MS', 12,))
		self.label_password.place(x=40, y=140)

		self.entry_password = Entry(self.window, width=20, show="*", borderwidth=0, bg="#F1F1F1", font=('Comic Sans MS', 11,))
		self.entry_password.place(x=150, y=140, height=30)

		self.show_btn = Button(self.window, width=27, bg="white", image=self.show_img, relief=FLAT, command=self.show_password)
		self.show_btn.place(x=340, y=140, height=27)

		self.button_reset = Button(self.window, text="Reset", width=10, bg="#F9F9F9", fg="#2196F3", font=('Comic Sans MS', 8), relief=FLAT, command=self.reset)
		self.button_reset.place(x=50, y=220)

		self.button_login = Button(self.window, text="Login", width=10, bg="#2196F3", fg="white", font=('Comic Sans MS', 8), relief=FLAT, command=self.login_user)
		self.button_login.place(x=220, y=220)

		self.label_register = Label(self.window, text="Don't have an account?", fg="black", bg="white", font=('Comic Sans MS', 8))
		self.label_register.place(x=130, y=280)

		self.button_to_signup = Button(self.window, text="Register as User", width=15, bg="#F9F9F9", fg="#2196F3", font=('Comic Sans MS', 8), relief=FLAT, command=self.go_to_signup)
		self.button_to_signup.place(x=130, y=310)

		self.label_or = Label(self.window, text="or", fg="black", bg="white", font=('Comic Sans MS', 8))
		self.label_or.place(x=175, y=340)

		self.button_register_service = Button(self.window, text="Register as Service", width=15, bg="#F9F9F9", fg="#2196F3", font=('Comic Sans MS', 8), relief=FLAT, command=self.register_service)
		self.button_register_service.place(x=130, y=360)

		self.window.mainloop()

	def login_user(self):  # For Login Button
		username = self.entry_username.get()
		password = self.entry_password.get()
		if username != '' and password != '':  # Validation code
			if self.login.login_user(username, password):
				messagebox.showinfo("Login", "Logged in successfully!")
				self.window.destroy()
				AccountInterface(username)  # Opens main application window
				return True
		else:
			messagebox.showerror("Login", "Please fill out all the fields.")
			return False

	def delete_user(self):  # For Delete User Button
		username = self.entry_username.get()
		password = self.entry_password.get()
		if username != '' and password != '':  # Validation code
			if self.login.delete_user(username, password):
				messagebox.showinfo('Delete User', 'User Deleted successfully!')
				return True
		else:
			messagebox.showerror("Delete User", 'Please fill out all the fields.')

	def reset(self):  # For Reset Button
		self.entry_username.delete(0, END)
		self.entry_password.delete(0, END)

	def go_to_signup(self):  # For Register as User Button
		self.window.destroy()
		SignupInterface()  # Opens Signup window

	def register_service(self):  # For Register as Service Button
		self.window.destroy()
		ServiceInterface()  # Opens Register Window

	def show_password(self):  # For Show Password Button
		if not self.show_state:
			self.entry_password['show'] = ""
			self.show_btn['image'] = self.hide_img
		else:
			self.entry_password['show'] = "*"
			self.show_btn['image'] = self.show_img
		self.show_state = not self.show_state


if __name__ == "__main__":
	login = LoginInterface()
