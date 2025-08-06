import pandas as pd
import Src.GlobalVariables.GlobalVariables as gv
import os
from tkinter import messagebox, simpledialog
from Src.Controllers.APIController import APIController
from Src.Class.Client import  Client

class ClientController:
    def __init__(self):
        self.Api = APIController()
        os.makedirs(os.path.dirname(gv.Clients_file_path), exist_ok=True)

    def create_client(self,next_id, name, last_name, email, address, cap, phone_number) :
        if not all([name, last_name, email, phone_number, address, cap]):
            messagebox.showwarning(
                "Campi vuoti",
                "Riempi tutti i campi!")
            return


        if gv.client_list:
            is_duplicate = any(
                c.FirstName == name and
                c.LastName == last_name and
                c.ID == next_id and
                c.city == address and
                c.PhoneNumber == phone_number and
                c.email == email and
                c.PostalCode == cap
                for c in gv.client_list
            )
            if is_duplicate:
                messagebox.showwarning(
                    "Cliente già esistente",
                    "L'account che stai cercando di creare è già presente nel software!")
                return



        new_client = Client(address, email, name, last_name, next_id, phone_number, cap)

        gv.client_list.append(new_client)

        APIController.write_client_on_csv()



