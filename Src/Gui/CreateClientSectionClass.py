import pandas as pd
import tkinter as tk
import os
import Src.GlobalVariables.GlobalVariables as gv

from Src.Controllers.ClientController import ClientController


class CreateClientSectionClass(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.cc = ClientController()
        tk.Label(self, text="ClientSection").grid(row=1, column=1)

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

        next_id = self.calcola_prossimo_numero()
        self.id.insert(0, next_id)
        self.id.config(state="readonly")





        create_client = tk .Button(self, text="Crea Utente", command=lambda: (self.cc.create_client(self.id.get(),
                                                                                  self.name.get(),
                                                                                  self.surname.get(),
                                                                                  self.email.get(),
                                                                                  self.address.get(),
                                                                                  self.phone.get(),
                                                                                  self.cap.get()), self.clear_fields()))
        create_client.grid(row=10, column=1)
        tk.Button(
            self,
            text="Back",
            command=lambda: (
                controller.frames["ClientSection"].fill_listbox(),  # aggiorna la listbox
                controller.mostra_frame("ClientSection")  # poi mostra il frame
            )
        ).grid(row=9, column=1)

    def clear_fields(self):
        self.name.delete(0, tk.END)
        self.surname.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.phone.delete(0, tk.END)
        self.cap.delete(0, tk.END)
        self.id.config(state="normal")
        self.id.delete(0, tk.END)
        self.id.insert(0, self.calcola_prossimo_numero())
        self.id.config(state = "readonly")


    def calcola_prossimo_numero(self) -> str:
        if not gv.client_list:
            return str(1)
        else:
            return  str(max(c.ID for c in gv.client_list) + 1)


