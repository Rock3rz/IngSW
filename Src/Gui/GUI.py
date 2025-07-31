import tkinter as tk
import pandas as pd
from Src.Controllers.AccountController import AccountController


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

        self.mostra_frame("MainMenu")

    ##Funzione che carica nella gui il frame passato come parametro
    def mostra_frame(self, nome_frame):
        frame = self.frames[nome_frame]
        frame.tkraise()



#Questa classe conterrà il frame con i tasti di navigazione per il menu principale

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text = "Menu Principale").grid(row = 1, column = 1)

        tk.Button(self, text = "UserSection", command= lambda: controller.mostra_frame("UserSection")).grid(row = 2, column = 1)

        tk.Button(self, text = "VehicleSection", command= lambda: controller.mostra_frame("VehicleSection")).grid(row = 2, column = 2)

        tk.Button(self, text="ClientSection", command=lambda: controller.mostra_frame("ClientSection")).grid(row=2, column=3)

        tk.Button(self, text = "QuoteSection", command= lambda: controller.mostra_frame("QuoteSection")).grid(row = 2, column = 4)

        tk.Button(self, text="AppointmentSection", command=lambda: controller.mostra_frame("AppointmentSection")).grid(row=2, column=5)

        tk.Button(self, text="CreateUserSection", command=lambda: controller.mostra_frame("CreateUserSection")).grid(row=2, column=6)



#Classe di gestione Profilo Venditore
class UserSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="UserSection").grid(row=1, column=1)
        tk.Button(self, text = "Back", command= lambda: controller.mostra_frame("MainMenu")).grid(row=2, column=1)

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

        name = tk.Entry(self)
        name.grid(row = 1, column = 1)

        password = tk.Entry(self)
        password.grid(row = 2, column = 1)

        tk.Button(self, text="Submit", command=lambda:lc.save_infos(name.get(),password.get())).grid(row=3, column=1)

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

        isAdmin = tk.BooleanVar()
        isAdminButton = tk.Checkbutton(self, text = "isAdmin", variable = isAdmin)
        isAdminButton.grid(row=7, column=1)


        #Buttons
        confirm = tk.Button(self, text = "Crea", command = lambda:(lc.create_user(FirstName.get(),LastName.get(),Email.get(),Username.get(),Password.get(), isAdmin.get()), clearFields(self)))
        confirm.grid(row=8, column=2)

        #BackButton
        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=8, column=1)

        def clearFields(self):
            FirstName.delete(0, tk.END)
            LastName.delete(0, tk.END)
            Email.delete(0, tk.END)
            Username.delete(0, tk.END)
            Password.delete(0, tk.END)
            isAdmin.set(False)















