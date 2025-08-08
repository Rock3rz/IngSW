from Src.Class.User import User
import pandas as pd
import os
import Src.GlobalVariables.GlobalVariables as gv
from tkinter import messagebox, simpledialog
import smtplib
from email.message import EmailMessage
import random

from Src.Controllers.APIController import APIController


class AccountController:
    def __init__(self):

        os.makedirs(os.path.dirname(gv.User_file_path), exist_ok=True)
        self.name = None
        self.password = None


    def login(self, name, password):

        #self.User = User
        self.name = name
        self.password = password

        if gv.user_list:

            utente = next((u for u in gv.user_list if u.username == self.name and u.Password == self.password), None)
            #(valore_da_restituire for variabile in collezione if condizione)


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

        new_user = User(next_id, email, name, username, is_admin, last_name, password)

        gv.user_list.append(new_user)

        APIController.write_user_on_csv()

    def LogOut(self):
        gv.isAdminUser = False
        gv.canEnter = False
        gv.CurrentUser = None

    #Funzione che prende in ingresso i nuovi valori da modificare e li salva all'indice corretto nel "Database" .csv
    def edit_personal_info(self, name, last_name, email, username, password):

        index =next((i for i, user in enumerate(gv.user_list) if user.user_id == gv.CurrentUser.user_id), None)
        if index is None:
            messagebox.showwarning("ERRORE")
            return

        # Aggiorna i valori
        gv.CurrentUser.firstName = name
        gv.CurrentUser.last_name = last_name
        gv.CurrentUser.email = email
        gv.CurrentUser.username = username
        gv.CurrentUser.Password = password

        gv.user_list.pop(index)
        gv.user_list.insert(index, gv.CurrentUser)

        APIController.write_user_on_csv()


    def reset_password(self):
        nuova_pw = self.random_password(6)


        # 3. Chiedi la mail all’utente
        email_Destinatario = simpledialog.askstring("Recupero Password", "Inserisci la tua E-mail registrata : ")
        if not email_Destinatario:
            return
        # 4. Verifica che l’email esista nel DataFrame

        mask = next((user.email for user in gv.user_list if user.email == email_Destinatario), None)

        if mask is None:
            messagebox.showwarning(
                "Attenzione",
                f"Nessun account trovato con l'indirizzo {email_Destinatario}"
            )
            return

        index = next((i for i, user in enumerate(gv.user_list) if user.email == email_Destinatario), None)

        gv.user_list[index].Password = nuova_pw
        APIController.write_user_on_csv()

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


