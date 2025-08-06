import tkinter as tk
from Src.Controllers.AccountController import AccountController
import Src.GlobalVariables.GlobalVariables as gv


class UserSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.lc = AccountController()
        tk.Label(self, text="UserSection").grid(row=1, column=1)

        # EntryFields
        FirstNameLabel = tk.Label(self, text="First Name").grid(row=2, column=1)
        self.FirstName = (tk.Entry(self))
        self.FirstName.grid(row=2, column=2)

        LastNameLabel = tk.Label(self, text="Last Name").grid(row=3, column=1)
        self.LastName = tk.Entry(self)
        self.LastName.grid(row=3, column=2)


        self.EmailLabel = tk.Label(self, text="Email").grid(row=4, column=1)
        self.Email = tk.Entry(self)
        self.Email.grid(row=4, column=2)

        self.UsernameLabel = tk.Label(self, text="Username").grid(row=5, column=1)
        self.Username = tk.Entry(self)
        self.Username.grid(row=5, column=2)

        self.PasswordLabel = tk.Label(self, text="Password").grid(row=6, column=1)
        self.Password = tk.Entry(self)
        self.Password.grid(row=6, column=2)


        tk.Button(self, text = "Back", command= lambda: controller.mostra_frame("MainMenu")).grid(row=7, column=1)

        tk.Button(self, text = "Modifica", command = lambda: self.enable_field() ).grid(row = 7, column = 2)

        tk.Button(self, text = "Salva", command = lambda:self.edit_data()).grid(row = 8, column = 2)

    def load_data(self):
        print(gv.CurrentUser)
        if gv.CurrentUser:
            user = gv.CurrentUser
            self.enable_field()
            self.FirstName.delete(0, tk.END)
            self.FirstName.insert(0, user.firstName)
            self.FirstName.config(state = "readonly")

            self.LastName.delete(0, tk.END)
            self.LastName.insert(0, user.LastName)
            self.LastName.config(state="readonly")

            self.Email.delete(0, tk.END)
            self.Email.insert(0, user.email)
            self.Email.config(state="readonly")

            self.Username.delete(0, tk.END)
            self.Username.insert(0, user.username)
            self.Username.config(state="readonly")

            self.Password.delete(0, tk.END)
            self.Password.insert(0, user.Password)
            self.Password.config(state="readonly")

    def enable_field(self):
        self.FirstName.config(state="normal")
        self.LastName.config(state="normal")
        self.Email.config(state="normal")
        self.Username.config(state="normal")
        self.Password.config(state="normal")

    def edit_data(self):
        self.lc.edit_personal_info(self.FirstName.get(),self.LastName.get(),self.Email.get(),self.Username.get(),self.Password.get())
        self.load_data()