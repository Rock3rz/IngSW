from Src.Class.User import User
import pandas as pd
import os
import Src.GlobalVariables.GlobalVariables as gv
from tkinter import messagebox, simpledialog
import smtplib
from email.message import EmailMessage
import random

class AccountController:
    def __init__(self):
        #self.Psw_file_path = "DB/password.csv"
        #os.makedirs(os.path.dirname(self.Psw_file_path), exist_ok=True)


        os.makedirs(os.path.dirname(gv.User_file_path), exist_ok=True)


    def login(self, name, password):
        self.User = User
        self.name = name
        self.password = password

        if gv.user_list:

            utente = next((u for u in gv.user_list if u.username == name and u.Password == password), None)
            #(valore_da_restituire for variabile in collezione if condizione)

            print("l'utente selezionato è ")
            print(utente)

            if not utente:
                messagebox.showwarning("Utente inesistente", "Non esiste nessun utente con queste credenziali")
                return
            else:
                gv.canEnter = True

            gv.CurrentUser = utente
            print(gv.CurrentUser)
            if utente.isAdmin:
                gv.isAdminUser = True
            else:
                gv.isAdminUser = False



    def create_user(self, name, last_name, email, username, password, is_admin:bool):

        if not all([name, last_name, email, username, password]):
            messagebox.showwarning(
                "Campi vuoti",
                "Riempi tutti i campi!")
            return

        '''
         if os.path.exists(gv.User_file_path):
            df_exists = pd.read_csv(gv.User_file_path)

            is_duplicate = ((df_exists["Name"] == name) & (df_exists["LastName"] == last_name) &
                            (df_exists["Email"]== email) & (df_exists["UserName"] == username) & (df_exists["Password"] == password)).any()

            if is_duplicate:
                messagebox.showwarning(
                    "Utente già esistente",
                    "L'account che stai cercando di creare è già presente nel software, se non ricordi le credenziali, effettua il recupero password!")
                return

            if "ID" in df_exists.columns and not df_exists.empty:
                next_id = df_exists["ID"].max() + 1
            else:
                next_id = 1
        else:
            next_id = 1
        '''
        if gv.user_list:
            is_duplicate = any(
                u.firstName == name and
                u.LastName == last_name and
                u.email == email and
                u.username == username and
                u.Password == password
                for u in gv.user_list
            )
            if is_duplicate:
                messagebox.showwarning(
                    "Utente già esistente",
                    "L'account che stai cercando di creare è già presente nel software, se non ricordi le credenziali, effettua il recupero password!")
                return

            next_id = max(u.user_id for u in gv.user_list) +1
        else:
            next_id = 1

        '''
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
        '''
        new_user = User(next_id, email, name, username, is_admin, last_name, password)

        ##df_new = pd.DataFrame([new_row])

        gv.user_list.append(new_user)



        ##if os.path.exists(gv.User_file_path):
         ##   df_new.to_csv(gv.User_file_path, mode="a", header=False, index=False)
        ##else:
        ##    df_new.to_csv(gv.User_file_path, index= False)
        print("Tutti gli utenti")
        for u in gv.user_list:
            print(f"{u.user_id} {u.firstName}{u.LastName}{u.username}{u.isAdmin}{u.Password}{u.email}")

    def LogOut(self):
        gv.isAdminUser = False
        gv.canEnter = False
        gv.CurrentUser = pd.DataFrame()

    #Funzione che prende in ingresso i nuovi valori da modificare e li salva all'indice corretto nel "Database" .csv
    def edit_personal_info(self, name, last_name, email, username, password):
        df = pd.read_csv(gv.User_file_path)


        user_id = gv.CurrentUser.iloc[0]["ID"]  #genero la stringa con l'id corrispondente al current user
        index = df[df["ID"] == user_id].index[0] # la cerco all'interno del "DB" e ne recupero l'indice


        # Aggiorna i valori
        df.at[index, "Name"] = name
        df.at[index, "LastName"] = last_name
        df.at[index, "Email"] = email
        df.at[index, "UserName"] = username
        df.at[index, "Password"] = password

        # Salva di nuovo il CSV
        df.to_csv(gv.User_file_path, index=False)

        # Aggiorna il CurrentUser globale con i nuovi dati
        gv.CurrentUser = df[df["ID"] == user_id]

    def reset_password(self):
        nuova_pw = self.random_password(6)


        self.df = pd.read_csv(gv.User_file_path)

        # 3. Chiedi la mail all’utente
        email_Destinatario = simpledialog.askstring("Recupero Password", "Inserisci la tua E-mail registrata : ")
        if not email_Destinatario:
            return
        # 4. Verifica che l’email esista nel DataFrame
        mask = self.df['Email'] == email_Destinatario
        if not mask.any():
            messagebox.showwarning(
                "Attenzione",
                f"Nessun account trovato con l'indirizzo {email_Destinatario}"
            )
            return
        # 5. Aggiorna la password nel DataFrame
        self.df.loc[mask, 'Password'] = nuova_pw
        # 6. Salva sul CSV
        self.df.to_csv(gv.User_file_path, index=False)

        # 7. Invia l’email con la nuova password
        self.invia_email(email_Destinatario,
                         "Recupero PW",
                         f"Questa è la tua nuova password : {nuova_pw} ",
                         "ingegneriadelsw2025@libero.it",
                         "IngSW2025!",
                         )

        messagebox.showinfo(
            "Fatto",
            f"Se l'account esiste, una mail con la nuova password è stata inviata a {email_Destinatario}."
        )


    @staticmethod
    def invia_email(destinatario, oggetto, corpo, mittente, password):
        msg = EmailMessage()
        msg['Subject'] = oggetto
        msg['From'] = mittente
        msg['To'] = destinatario
        msg.set_content(corpo)

        with smtplib.SMTP_SSL("smtp.libero.it", 465) as smtp:
            smtp.login(mittente, password)
            smtp.send_message(msg)

    @staticmethod
    def random_password(length: int = 6):
        password_temporanea = random.choices(range(1, 9), k = length )
        return ''.join(str(digit) for digit in password_temporanea)


