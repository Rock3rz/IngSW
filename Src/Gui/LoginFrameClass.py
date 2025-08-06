import tkinter as tk
from Src.Controllers.AccountController import AccountController
import Src.GlobalVariables.GlobalVariables as gv


#Login
class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.lc = AccountController() #istanzia ogni volta che apro il frame

        tk.Label(self, text="Login").grid(row=1, column=1)
        self.name = tk.Entry(self)
        self.name.grid(row = 1, column = 2)

        tk.Label(self, text="Password").grid(row=2, column=1)
        self.password = tk.Entry(self)
        self.password.grid(row = 2, column = 2)


        ##tk.Button(self, text="Submit", command=lambda:submit_logic()).grid(row=3, column=1)
        self.submit = tk.Button(self, text = "Submit", command=lambda:submit_logic())
        self.submit.grid(row = 3, column = 2)

        tk.Button(self, text = "Pasword Dimenticata", command = lambda: lc.reset_password()).grid(row = 4, column=1)



        def submit_logic():
            self.lc.login(self.name.get(), self.password.get())
            self.name.delete(0, tk.END)
            self.password.delete(0, tk.END)
            #self.current_email = gv.CurrentUser.iloc[0]['Email']
            if gv.canEnter:
                controller.frames["UserSection"].load_data()
                controller.mostra_frame("MainMenu")
                self.name.delete(0, tk.END)
                self.password.delete(0, tk.END)

