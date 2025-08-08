import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv
from Src.Controllers.ClientController import ClientController
from Src.Class.Client import Client
from tkinter import messagebox

#Classe di gestione Schede clienti
class ClientSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.cc = ClientController()

        self.controller = controller

        #indice cliente selezionato NELLA LISTBOX
        self.selected_client = None

        #Lista di supporto
        self.support_list = []

        #istanzio la tabella
        self.list_client = tk.Listbox(self)
        self.list_client.grid(row=0, column=0, rowspan = 10)

        #Campi di ricerca
        tk.Label(self, text = "Ricerca cliente").grid(row = 0, column = 6,columnspan = 2)

        tk.Label(self, text="Nome").grid(row = 1, column = 6)
        self.first_nameSrc = tk.Entry(self)
        self.first_nameSrc.grid(row=1, column=7)

        tk.Label(self, text = "Cognome").grid(row = 2, column = 6)
        self.last_nameSrc = tk.Entry(self)
        self.last_nameSrc.grid(row=2, column=7)

        tk.Label(self, text="Email").grid(row= 3, column = 6)
        self.emailSrc = tk.Entry(self)
        self.emailSrc.grid(row=3, column=7)

        tk.Label(self, text="Telefono").grid(row = 4, column = 6)
        self.phone_numberSrc = tk.Entry(self)
        self.phone_numberSrc.grid(row=4, column=7)

        self.buttonSrc = tk.Button(self, text = "Cerca", command = lambda:self.call_search())
        self.buttonSrc.grid(row = 5, column = 7)

        #Riempio la listbox con TUTTI gli utenti
        self.fill_listbox()

        #Tasti Selezione
        tk.Button(self, text= "Crea Cliente", command = lambda: controller.mostra_frame("CreateClientSectionClass")).grid(row=1, column=5)
        tk.Button(self, text= "Visualizza Cliente", command= lambda: self.open_view_conditional()).grid(row=2, column=5)
        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=2, column=1)

        self.list_client.bind("<<ListboxSelect>>", self.on_select)

    def fill_listbox(self):
        self.list_client.delete(0, tk.END)
        self.support_list = []
        for client in gv.client_list:
            self.list_client.insert(tk.END, f"{client.ID} {client.FirstName} {client.LastName}")
            self.support_list.append(client)


    def open_view_conditional(self):
        if self.selected_client is None:
            messagebox.showwarning("ERRORE", "Nessun cliente selezionato!")
            return
        gv.CurrentClient = self.support_list[self.selected_client]
        self.controller.frames["ViewClient"].load_client_infos()
        self.controller.mostra_frame("ViewClient")



    def on_select(self, event = None):
        if event:
            widget = event.widget
            self.selected_client = widget.curselection()
        else:
            self.selected_client = self.list_client.curselection()

        if self.selected_client:
            self.selected_client = self.selected_client[0]
            value = self.list_client.get( self.selected_client)  # Testo della riga selezionata
            print(f"Indice selezionato: { self.selected_client}, Valore: {value}")


    def call_search(self):
        s= ""
        if (self.first_nameSrc.get() == s and
            self.last_nameSrc.get() == s and
            self.emailSrc.get() == s and
            self.phone_numberSrc.get() == s):
            self.fill_listbox()
            return
        tmplist = self.cc.search_client(self.first_nameSrc.get(),
                              self.last_nameSrc.get(),
                              self.emailSrc.get(),
                              self.phone_numberSrc.get())
        if not tmplist:
            messagebox.showwarning("ERRORE", "Nessun cliente trovato")
            return

        self.list_client.delete(0, tk.END)
        self.support_list = []  # 🔹 aggiorno anche la lista di supporto
        for client in tmplist:
            self.list_client.insert(tk.END, f"{client.ID} {client.FirstName} {client.LastName}")
            self.support_list.append(client)




