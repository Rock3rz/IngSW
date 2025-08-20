import pandas as pd
import Src.GlobalVariables.GlobalVariables as gv
import os
from tkinter import messagebox, simpledialog
from Src.Controllers.APIController import APIController
from Src.Class.Client import  Client

class ClientController:
    def __init__(self):
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


        #creo un nuovo cliente da inserire nella lista
        new_client = Client(address, email, name, last_name, next_id, phone_number, cap)

        #Lo inserisco
        gv.client_list.append(new_client)

        #salvo le info attraverso la API
        APIController.write_client_on_csv()

    def edit_client_infos(self, name, last_name, email, address, cap, phone_number):

        index = next((i for i, client in enumerate(gv.client_list) if client.ID == gv.CurrentClient.ID), None)
        if index is None:
            messagebox.showwarning("ERRORE")
            return
        gv.CurrentClient.FirstName = name
        gv.CurrentClient.LastName = last_name
        gv.CurrentClient.email = email
        gv.CurrentClient.city = address
        gv.CurrentClient.PhoneNumber = phone_number
        gv.CurrentClient.PostalCode = cap

        gv.client_list.pop(index)
        gv.client_list.insert(index, gv.CurrentClient)
        APIController.write_client_on_csv()

    def search_client(self, name, last_name, email, phone):
        risultati = []
        for client in gv.client_list:
            if (
                    (name == "" or client.FirstName.lower() == name.lower()) and
                    (last_name == "" or client.LastName.lower() == last_name.lower()) and
                    (email == "" or client.email.lower() == email.lower()) and
                    (phone == "" or client.PhoneNumber == phone)
            ):
                risultati.append(client)
        return risultati

    def search_client_by_string(self, search_string):
        tmp_client_list = []
        for client in gv.client_list:
            if( search_string.lower() in client.FirstName.lower() or
                search_string.lower() in client.LastName.lower() or
                search_string.lower() in client.email.lower()):
                tmp_client_list.append(client)
        return tmp_client_list







