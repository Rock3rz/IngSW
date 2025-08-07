import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv
from Src.Controllers.ClientController import ClientController

#Classe di gestione e visione clienti
class ViewClient(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.cc = ClientController
        tk.Label(self, text="Nome").grid(row=2, column=1)
        self.name = tk.Entry(self)
        self.name.grid(row=2, column=2)

        tk.Label(self, text="Cognome").grid(row=3, column=1)
        self.surname = tk.Entry(self)
        self.surname.grid(row=3, column=2)

        tk.Label(self, text="Email").grid(row=4, column=1)
        self.email = tk.Entry(self)
        self.email.grid(row=4, column=2)

        tk.Label(self, text="Indrizzo").grid(row=5, column=1)
        self.address = tk.Entry(self)
        self.address.grid(row=5, column=2)

        tk.Label(self, text="CAP").grid(row=6, column=1)
        self.cap = tk.Entry(self)
        self.cap.grid(row=6, column=2)

        tk.Label(self, text="Telefono").grid(row=7, column=1)
        self.phone = tk.Entry(self)
        self.phone.grid(row=7, column=2)

        tk.Label(self, text="ID").grid(row=8, column=1)
        self.id = tk.Entry(self)
        self.id.grid(row=8, column=2)


        tk.Label(self, text="Info Cliente").grid(row=1, column=1)
        tk.Button(self, text= "Modifica informazioni", command= lambda: self.enable_fields()).grid(row = 9, column=2)
        tk.Button(self, text= "Salva", command= lambda: self.edit_info()).grid(row = 9, column=3)
        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("ClientSection")).grid(row=9, column=1)

    def enable_fields(self):
        self.name.config(state="normal")
        self.surname.config(state="normal")
        self.email.config(state="normal")
        self.address.config(state="normal")
        self.phone.config(state="normal")
        self.cap.config(state="normal")
        self.id.config(state="normal")


    def clear_fields(self):
        self.name.delete(0, tk.END)
        self.surname.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.phone.delete(0, tk.END)
        self.cap.delete(0, tk.END)
        self.id.delete(0, tk.END)

    def disable_fields(self):
        self.name.config(state="readonly")
        self.surname.config(state="readonly")
        self.email.config(state="readonly")
        self.address.config(state="readonly")
        self.phone.config(state="readonly")
        self.cap.config(state="readonly")
        self.id.config(state="readonly")


    def load_client_infos(self):
        if gv.CurrentClient is not None:
            self.enable_fields()
            self.clear_fields()

            #self.name.delete(0, tk.END)
            self.name.insert(0, gv.CurrentClient.FirstName)

            #self.surname.delete(0, tk.END)
            self.surname.insert(0, gv.CurrentClient.LastName)

            # self.email.delete(0, tk.END)
            self.email.insert(0, gv.CurrentClient.email)

            # self.address.delete(0, tk.END)
            self.address.insert(0, gv.CurrentClient.city)

            # self.name.delete(0, tk.END)
            self.phone.insert(0, gv.CurrentClient.PhoneNumber)

            # self.name.delete(0, tk.END)
            self.cap.insert(0, gv.CurrentClient.PostalCode)

            # self.name.delete(0, tk.END)
            self.id.insert(0, gv.CurrentClient.ID)

            self.disable_fields()

    def edit_info(self):
        self.cc.edit_client_infos(self.name.get(),
                                  self.surname.get(),
                                  self.email.get(),
                                  self.address.get(),
                                  self.cap.get(),
                                  self.phone.get()
                                  )
        self.load_client_infos()
        self.disable_fields()



