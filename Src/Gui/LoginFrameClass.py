import tkinter as tk
from Src.Controllers.AccountController import AccountController
import Src.GlobalVariables.GlobalVariables as gv


#Login
class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        lc = AccountController() #istanzia ogni volta che apro il frame

        tk.Label(self, text="Login").grid(row=1, column=1)
        name = tk.Entry(self)
        name.grid(row = 1, column = 2)

        tk.Label(self, text="Password").grid(row=2, column=1)
        password = tk.Entry(self)
        password.grid(row = 2, column = 2)


        (tk.Button(self, text="Submit", command=lambda:submit_logic()).grid(row=3, column=1))

        #Logica di submit per entrare
        def submit_logic():
            lc.login(name.get(), password.get())
            if gv.canEnter:
                controller.frames["UserSection"].load_data()
                controller.mostra_frame("MainMenu")
                name.delete(0, tk.END)
                password.delete(0, tk.END)