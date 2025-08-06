import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv
from Src.Controllers.ClientController import ClientController
from Src.Class.Client import Client


#Classe di gestione Schede clienti
class ClientSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.cc = ClientController()


        self.list_client = tk.Listbox(self)
        self.list_client.grid(row=0, column=0, rowspan = 10)
        self.fill_listbox()

        tk.Button(self, text= "Crea Cliente", command = lambda: controller.mostra_frame("CreateClientSectionClass")).grid(row=1, column=5)
        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=2, column=1)

    def fill_listbox(self):
        self.list_client.delete(0, tk.END)

        for client in gv.client_list:
            self.list_client.insert(tk.END, f"{client.ID} {client.FirstName} {client.LastName}")