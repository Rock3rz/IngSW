import tkinter as tk



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
            LoginFrame
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

        tk.Label(self, text = "Menu Principale").grid(row = 1, column = 1)

        tk.Button(self, text = "UserSection", command= lambda: controller.mostra_frame("UserSection")).grid(row = 2, column = 1)

        tk.Button(self, text = "VehicleSection", command= lambda: controller.mostra_frame("VehicleSection")).grid(row = 2, column = 2)

        tk.Button(self, text="ClientSection", command=lambda: controller.mostra_frame("ClientSection")).grid(row=2, column=3)

        tk.Button(self, text = "QuoteSection", command= lambda: controller.mostra_frame("QuoteSection")).grid(row = 2, column = 4)

        tk.Button(self, text="AppointmentSection", command=lambda: controller.mostra_frame("AppointmentSection")).grid(row=2, column=5)

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
        name = tk.Entry(self).grid(row = 1, column = 1)
        password = tk.Entry(self).grid(row = 2, column = 1)














