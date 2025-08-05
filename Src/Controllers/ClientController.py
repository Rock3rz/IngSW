import pandas as pd
import Src.GlobalVariables.GlobalVariables as gv
import os
from tkinter import messagebox, simpledialog
from Src.Controllers.APIController import APIController


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

        if os.path.exists(gv.Clients_file_path):
            df_exists = pd.read_csv(gv.Clients_file_path)

            is_duplicate = ((df_exists["Name"] == name) & (df_exists["LastName"] == last_name) &
                            (df_exists["Email"]== email) & (df_exists["PhoneNumber"] == phone_number)).any()

            if is_duplicate:
                messagebox.showwarning(
                    "Cliente già esistente",
                    "L'account cliente che stai cercando di creare è già presente nel software!")
                return

            #APIController.write_user_on_csv()
            '''
             if "ClientID" in df_exists.columns and not df_exists.empty:
                next_id = df_exists["ClientID"].max() + 1
            else:
                next_id = 1
        else:
            next_id = 1
            # Nuova riga con campo ID
            
             new_row = {
            "ClientID": next_id,
            "Name": name,
            "LastName": last_name,
            "Email": email,
            "Address": address,
            "CAP": cap,
            "PhoneNumber": phone_number
        }

        df_new = pd.DataFrame([new_row])

        if os.path.exists(gv.Clients_file_path):
            df_new.to_csv(gv.Clients_file_path, mode="a", header=False, index=False)
        else:
            df_new.to_csv(gv.Clients_file_path, index= False)
            '''



