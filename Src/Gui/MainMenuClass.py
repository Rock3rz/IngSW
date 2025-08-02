import tkinter as tk
from tkinter import messagebox
import Src.GlobalVariables.GlobalVariables as gv
from Src.Controllers.AccountController import AccountController


#Questa classe conterrà il frame con i tasti di navigazione per il menu principale
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.lc = AccountController()

        tk.Label(self, text = "Menu Principale").grid(row = 1, column = 1)

        tk.Button(self, text = "UserSection", command= lambda: controller.mostra_frame("UserSection")).grid(row = 2, column = 1)

        tk.Button(self, text = "VehicleSection", command= lambda: controller.mostra_frame("VehicleSection")).grid(row = 2, column = 2)

        tk.Button(self, text="ClientSection", command=lambda: controller.mostra_frame("ClientSection")).grid(row=2, column=3)

        tk.Button(self, text = "QuoteSection", command= lambda: controller.mostra_frame("QuoteSection")).grid(row = 2, column = 4)

        tk.Button(self, text="AppointmentSection", command=lambda: controller.mostra_frame("AppointmentSection")).grid(row=2, column=5)

        tk.Button(self, text="CreateUserSection", command=lambda: isAdminCheckButton()).grid(row=2, column=6)

        tk.Button(self, text="LogOut", command=lambda: (controller.mostra_frame("LoginFrame"),self.lc.LogOut())).grid(row=3, column=7)

        # funzione interna per la verifica e il caricamento delle funzioni da admin
        def isAdminCheckButton():
            if gv.isAdminUser:
                controller.mostra_frame("CreateUserSection")
            else:
                messagebox.showinfo("Accesso non consentito", "Non hai i permessi per accedere a questa sezione!")