import tkinter as tk
import os
from tkinter import messagebox, simpledialog
import Src.GlobalVariables.GlobalVariables as gv
from Src.Controllers.APIController import APIController
from Src.Class.Vehicle import Model, Vehicle

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



