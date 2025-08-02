import tkinter as tk
from tkinter import messagebox
import pandas as pd
from Src.Controllers.AccountController import AccountController
import Src.GlobalVariables.GlobalVariables as gv



class Gui:

    def __init__(self, root):
        self.root = root

        self.container = tk.Frame(root)
        self.container.grid(row = 0, column = 0, sticky="nsew")

        self.frames = {}

        #Ciclo che carica in memoria i vari frame
        for F in (
            MainMenu,
            UserSection,
            VehicleSection,
            ClientSection,
            QuoteSection,
            AppointmentSection,
            LoginFrame,
            CreateUserSection
            ):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")

        self.mostra_frame("LoginFrame")

    ##Funzione che carica nella gui il frame passato come parametro
    def mostra_frame(self, nome_frame):
        frame = self.frames[nome_frame]
        frame.tkraise()



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

        #funzione interna per la verifica e il caricamento delle funzioni da admin
        def isAdminCheckButton():
            if gv.isAdminUser:
                controller.mostra_frame("CreateUserSection")
            else:
                messagebox.showinfo("Accesso non consentito", "Non hai i permessi per accedere a questa sezione!")



#Classe di gestione Profilo Venditore
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
        if not gv.CurrentUser.empty:
            user = gv.CurrentUser.iloc[0]
            self.FirstName.delete(0, tk.END)
            self.FirstName.insert(0, user["Name"])
            self.FirstName.config(state = "readonly")

            self.LastName.delete(0, tk.END)
            self.LastName.insert(0, user["LastName"])
            self.LastName.config(state="readonly")

            self.Email.delete(0, tk.END)
            self.Email.insert(0, user["Email"])
            self.Email.config(state="readonly")

            self.Username.delete(0, tk.END)
            self.Username.insert(0, user["UserName"])
            self.Username.config(state="readonly")

            self.Password.delete(0, tk.END)
            self.Password.insert(0, user["Password"])
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


#Classe di gestione e visione veicoli
class VehicleSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="VehicleSection").grid(row=1, column=1)
        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=2, column=1)

#Classe di gestione Schede clienti
class ClientSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="ClientSection").grid(row=1, column=1)
        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=2, column=1)

#Classe di gestione preventivi
class QuoteSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="QuoteSection").grid(row=1, column=1)
        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=2, column=1)

#Classe di gestione appuntamenti
class AppointmentSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="AppointmentSection").grid(row=1, column=1)
        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=2, column=1)

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

class CreateUserSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        lc = AccountController()  # istanzia ogni volta che apro il frame
        #Labels
        tk.Label(self, text="Crea Utente").grid(row=1, column=1)

        #EntryFields
        FirstNameLabel = tk.Label(self, text = "First Name").grid(row=2, column=1)
        FirstName = (tk.Entry(self))
        FirstName.grid(row=2, column=2)

        LastNameLabel = tk.Label(self, text = "Last Name").grid(row=3, column=1)
        LastName = tk.Entry(self)
        LastName.grid(row=3, column=2)

        EmailLabel = tk.Label(self, text = "Email").grid(row=4, column=1)
        Email = tk.Entry(self)
        Email.grid(row=4, column=2)

        UsernameLabel = tk.Label(self, text = "Username").grid(row=5, column=1)
        Username = tk.Entry(self)
        Username.grid(row=5, column=2)

        PasswordLabel = tk.Label(self, text = "Password").grid(row=6, column=1)
        Password = tk.Entry(self)
        Password.grid(row=6, column=2)

        is_admin = tk.BooleanVar()
        is_admin_button = tk.Checkbutton(self, text = "is_admin", variable = is_admin)
        is_admin_button.grid(row=7, column=1)


        #Buttons
        confirm = tk.Button(self, text = "Crea", command = lambda:(lc.create_user(FirstName.get(),LastName.get(),Email.get(),Username.get(),Password.get(), is_admin.get()), clear_fields(self)))
        confirm.grid(row=8, column=2)

        #BackButton
        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=8, column=1)

        def clear_fields():
            FirstName.delete(0, tk.END)
            LastName.delete(0, tk.END)
            Email.delete(0, tk.END)
            Username.delete(0, tk.END)
            Password.delete(0, tk.END)
            is_admin.set(False)





















