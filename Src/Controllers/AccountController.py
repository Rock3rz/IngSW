from Src.Class.User import User
import pandas as pd
import os

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


    def save_infos(self, name, password):
        df = pd.DataFrame({
            "Name": [name],
            "Password": [password]
        })

        #if os.path.exists(self.Psw_file_path):
            #df.to_csv(self.Psw_file_path, mode='a', header = False, index = False)
        #else:
            #df.to_csv(self.Psw_file_path, index = False)

    def create_user(self, name, last_name, email, username, password, is_admin:bool):

        if not all([name, last_name, email, username, password]):
            print("Errore!")
            return
        '''
        df = pd.DataFrame({
            "Name": [name],
            "LastName": [last_name],
            "Email": [email],
            "UserName": [username],
            "Password": [password],
            "IsAdmin": [is_admin]
        })
        '''

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







