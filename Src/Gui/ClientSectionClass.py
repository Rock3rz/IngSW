import tkinter as tk

from Src.Controllers.ClientController import ClientController


#Classe di gestione Schede clienti
class ClientSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.cc = ClientController()


        self.list_client = tk.Listbox(self)
        self.list_client.grid(row=0, column=0, rowspan = 10)


        tk.Button(self, text= "Crea Cliente", command = lambda: controller.mostra_frame("CreateClientSectionClass")).grid(row=1, column=5)
        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=2, column=1)

