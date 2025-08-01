from Src.Class.User import User
import pandas as pd
import os
import Src.GlobalVariables.GlobalVariables as gv
from tkinter import messagebox

class AccountController():
    def __init__(self):
        #self.Psw_file_path = "DB/password.csv"
        #os.makedirs(os.path.dirname(self.Psw_file_path), exist_ok=True)

        self.User_file_path = "DB/user.csv"
        os.makedirs(os.path.dirname(self.User_file_path), exist_ok=True)


    def login(self, name, password):
        self.User = User
        self.name = name
        self.password = password

        if os.path.exists(self.User_file_path):
            df = pd.read_csv(self.User_file_path)


            utente = df[(df["UserName"] == name) & (df["Password"] == password)]

            if utente.empty:
                messagebox.showwarning("Utente inesistente", "Non esiste nessun utente con queste credenziali")
                return
            else:
                gv.canEnter = True

            gv.CurrentUser = utente
            print(gv.CurrentUser)
            if utente.iloc[0]["IsAdmin"] == True:
                gv.isAdminUser = True
            else:
                gv.isAdminUser = False





    def save_infos(self, name, password):
        df = pd.DataFrame({
            "Name": [name],
            "Password": [password]
        })


    def create_user(self, name, last_name, email, username, password, is_admin:bool):

        if not all([name, last_name, email, username, password]):
            print("Errore!")
            return


        if os.path.exists(self.User_file_path):
            df_exists = pd.read_csv(self.User_file_path)

            is_duplicate = ((df_exists["Name"] == name) & (df_exists["LastName"] == last_name) &
                            (df_exists["Email"]== email) & (df_exists["UserName"] == username) & (df_exists["Password"] == password)).any()

            if is_duplicate:
                print("Duplicate!")
                return

            if "ID" in df_exists.columns and not df_exists.empty:
                next_id = df_exists["ID"].max() + 1
            else:
                next_id = 1
        else:
            next_id = 1

            # Nuova riga con campo ID
        new_row = {
            "ID": next_id,
            "Name": name,
            "LastName": last_name,
            "Email": email,
            "UserName": username,
            "Password": password,
            "IsAdmin": is_admin
        }

        df_new = pd.DataFrame([new_row])

        if os.path.exists(self.User_file_path):
            df_new.to_csv(self.User_file_path, mode="a", header=False, index=False)
        else:
            df_new.to_csv(self.User_file_path, index= False)

    def LogOut(self):
        gv.isAdminUser = False
        gv.CanEnter = False
        gv.CurrentUser = ()

    def edit_personal_info(self, name, last_name, email, username, password):
        oldData = gv.CurrentUser.iloc[0]
        oldData["Name"] = name
        oldData["LastName"] = last_name
        oldData["Email"] = email
        oldData["UserName"] = username
        oldData["Password"] = password









