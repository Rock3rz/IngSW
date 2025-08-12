import tkinter as tk
import os
from logging import exception
from tkinter import messagebox, simpledialog
import Src.GlobalVariables.GlobalVariables as gv
from Src.Controllers.APIController import APIController
from Src.Class.Vehicle import Model, Vehicle
from typing import Optional

class VehicleController():
    def __init__(self):
        #api = APIController()
        os.makedirs(os.path.dirname(gv.Brand_file_path), exist_ok=True)

    def create_brand(self):

        new_brand = simpledialog.askstring("Brand", "Inserire un brand")
        if new_brand:
            # Confronto case-insensitive
            if new_brand.lower() in (b.lower() for b in gv.brand_list):
                messagebox.showwarning("Errore", f"Il brand '{new_brand}' esiste già!")
            else:
                gv.brand_list.append(new_brand)
                messagebox.showinfo("Successo", f"Brand '{new_brand}' aggiunto!")
        APIController.write_brand_on_csv()

    def create_Model(self, name, displacement, hp, next_id):

        if not all([name,displacement,hp]):
            messagebox.showwarning(
                "Campi vuoti",
                "Riempi tutti i campi!")
            return

        #verifico l'esistenza e assegno l'indice incrementale
        if gv.model_list:
            is_duplicate = any(m.brand == gv.CurrentBrand and
                               m.name == name and
                               m.displacement == displacement and
                               m.hp == hp
                               for m in gv.model_list)

            if is_duplicate:
                messagebox.showwarning("Errore", "Il modello esiste già ")
                return



        newModel = Model(gv.CurrentBrand,
                             name,
                             displacement,
                             hp, next_id)

        gv.model_list.append(newModel)

    def create_vehicle(self,
                       vehicle_id,
                       model_id,
                       year,
                       color,
                       fuel_type,
                       is_available,
                       km,
                       plate,
                       price,
                       image = None ):
        if not all([vehicle_id,model_id,year,color,fuel_type,km,plate,price]):
            messagebox.showwarning(
                "Campi vuoti",
                "Riempi tutti i campi!")
            return

        '''
        for model in gv.model_list:
            if model.model_id == model_id:
                tmpModel = model
        '''
        tmp_model = gv.model_recovery(model_id)

        new_vehicle = Vehicle(tmp_model, year, color, fuel_type, vehicle_id, is_available, km, plate, price, image = None)
        gv.vehicle_list.append(new_vehicle)
        APIController.write_vehicle_on_csv()

    def delete_vehicle(self):
        # 1) Verifica che un veicolo sia selezionato
        current = gv.CurrentVehicle
        if current is None:
            messagebox.showwarning("Errore", "Selezionare un veicolo")
            return

        try:
            index = gv.vehicle_list.index(current)
        except ValueError:
            # Il veicolo selezionato non è più presente nella lista
            messagebox.showwarning("Errore", "Veicolo non trovato")
            gv.CurrentVehicle = None
            return

        if index is None:
            messagebox.showwarning("Errore", "Selezionare un veicolo")
            return
        answer = messagebox.askyesno("Conferma", "Vuoi eliminare il veicolo?")

        if answer:

            print(index)
            gv.vehicle_list.pop(index)
            APIController.write_vehicle_on_csv()
            gv.CurrentVehicle = None
        else:
            return



