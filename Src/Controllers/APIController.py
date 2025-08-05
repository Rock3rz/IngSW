import pandas as pd
import os
import Src.GlobalVariables.GlobalVariables as gv
from Src.Class.User import User

class APIController:
    def __init__(self):
        if os.path.exists(gv.User_file_path):
            self.df = pd.read_csv(gv.User_file_path)
            self.refresh_user_list()

        else:
            self.df = pd.DataFrame()

    def refresh_user_list(self):
        for _, row in self.df.iterrows():
            gv.user_list.append(User(
                user_id=int(row["ID"]),
                email=str(row["Email"]),
                first_name=str(row["Name"]),
                username=str(row["UserName"]),
                is_admin=bool(bool(row["IsAdmin"])),
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

