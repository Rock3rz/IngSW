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

        if os.path.exists(gv.Clients_file_path):
            df_exists = pd.read_csv(gv.Clients_file_path)

            if "ClientID" in df_exists.columns and not df_exists.empty:
                next_id = df_exists["ClientID"].max() + 1
            else:
                next_id = 1
            self.id.insert(0, next_id)
        self.id.config(state="readonly")







        tk.Button(self, text="Crea Utente", command=lambda: self.cc.create_client(self.id.get(),
                                                                                  self.name.get(),
                                                                                  self.surname.get(),
                                                                                  self.email.get(),
                                                                                  self.address.get(),
                                                                                  self.phone.get(),
                                                                                  self.cap.get())).grid(row=10, column=1)
        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("ClientSection")).grid(row=9, column=1)

    def clear_fields(self):
        self.name.delete(0, tk.END)
        self.surname.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.phone.delete(0, tk.END)
        self.cap.delete(0, tk.END)

    def fill_listbox(self):
        self.useListBox.delete(0, tk.END)
        self.df = pd.read_csv(gv.Clients_file_path, usecols=["ID","Name", "LastName", "Email","Address","CAP", "PhoneNumber"])
        print(self.df)

        for _, row in self.df.iterrows():
            self.useListBox.insert(tk.END, f"{row['ClientID']} {row['Name']} {row['LastName']}")
