import pandas as pd
import os
import Src.GlobalVariables.GlobalVariables as gv
from Src.Class.Client import Client
from Src.Class.User import User

class APIController:
    def __init__(self):
        if os.path.exists(gv.User_file_path):
            self.df = pd.read_csv(gv.User_file_path)
            self.refresh_user_list()

        else:
            self.df = pd.DataFrame()

        if os.path.exists(gv.Clients_file_path):
            self.df = pd.read_csv(gv.Clients_file_path)
            self.refresh_client_list()
        else:
            self.df = pd.DataFrame()

    @staticmethod
    def refresh_user_list():
        if os.path.exists(gv.User_file_path):
            df = pd.read_csv(gv.User_file_path)
            #svuoto la lista prima di ricaricarla sennò ottengo delle copie
            gv.user_list.clear()

            for _, row in df.iterrows():
                gv.user_list.append(User(
                    user_id=int(row["ID"]),
                    email=str(row["Email"]),
                    first_name=str(row["Name"]),
                    username=str(row["UserName"]),
                    is_admin=bool(row["IsAdmin"]),
                    last_name=str(row["LastName"]),
                    password=str(row["Password"]),
                ))

    @staticmethod
    def write_user_on_csv():
        data = []
        for user in gv.user_list:
            data.append({
                "ID" : user.user_id,
                "Name": user.firstName,
                "LastName" : user.LastName,
                "Email": user.email,
                "UserName" : user.username,
                "Password" : user.Password,
                "IsAdmin" : user.isAdmin,
            })
        df = pd.DataFrame(data)
        df.to_csv(gv.User_file_path, index = False)
        APIController.refresh_user_list()


    @staticmethod
    def refresh_client_list():
        if os.path.exists(gv.Clients_file_path):
            df = pd.read_csv(gv.Clients_file_path)

            #svuoto la lista
            gv.client_list.clear()

            for _, row in df.iterrows():
                gv.client_list.append(Client(
                    client_id = int(row["Client_ID"]),
                    first_name=str(row["First_Name"]),
                    last_name=str(row["Last_Name"]),
                    email=str(row["Email"]),
                    phone_number= int(row["PhoneNumber"]),
                    city=str(row["Address"]),
                    postal_code=int(row["PostalCode"]),

                ))

    @staticmethod
    def write_client_on_csv():
        data = []
        for client in gv.client_list:
            data.append({
                "Client_ID": client.ID,
                "First_Name": client.FirstName,
                "Last_Name": client.LastName,
                "Email": client.email,
                "PhoneNumber": client.PhoneNumber,
                "Address": client.city,
                "PostalCode": client.PostalCode,
            })
        df = pd.DataFrame(data)
        df.to_csv(gv.Clients_file_path, index=False)
        APIController.refresh_client_list()