import tkinter as tk

from pygame.sprite import collide_mask

import Src.GlobalVariables.GlobalVariables as gv
from Src.Controllers.VehicleController import  VehicleController
from Src.GlobalVariables.GlobalVariables import model_list


class CreateModel(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.vc = gv.vehicle_controller
        tk.Label(self, text="Create Model").grid(column=0, row=0)

        tk.Label(self, text="Brand").grid(column=0, row=1)
        self.brand = tk.Entry(self)
        self.brand.grid(row=1, column=1)

        tk.Label(self, text="Nome").grid(column=0, row=2)
        self.name = tk.Entry(self)
        self.name.grid(row=2, column=1)

        tk.Label(self, text="Cilindrata").grid(column=0, row=3)
        self.displacement = tk.Entry(self)
        self.displacement.grid(row=3, column=1)

        tk.Label(self, text="Cavalli").grid(column=0, row=4)
        self.hp = tk.Entry(self)
        self.hp.grid(row=4, column=1)

        tk.Label(self, text="ID").grid(column=0, row=5)
        self.model_ID = tk.Entry(self)
        self.model_ID.grid(row=5, column=1)

        tk.Button(self, text="Salva",command= lambda: self.saveModel()).grid(column=2, row=6)
        tk.Button(self, text="Back", command = lambda: self.back_function()).grid(column=3, row=6)

    def clearFields(self):
        self.brand.delete(0, tk.END)
        self.name.delete(0, tk.END)
        self.displacement.delete(0, tk.END)
        self.hp.delete(0, tk.END)
        self.model_ID.delete(0, tk.END)

    def saveModel(self):
        self.vc.create_Model(
            self.name.get(),
            self.displacement.get(),
            self.hp.get(),
            self.model_ID.get(),
        )
        for models in model_list:
            print(models.brand, models.name, models.displacement, models.hp, models.model_id)

        self.clearFields()
        self.controller.mostra_frame("CreateVehicle")

    def loadModel(self):
        if gv.model_list:
            next_id = max(int(m.model_id) for m in gv.model_list) + 1
        else:

            next_id = 1
        print(gv.CurrentBrand)

        self.brand.configure(state = "normal")
        self.brand.delete(0, tk.END)
        self.brand.insert(tk.END, gv.CurrentBrand)
        self.brand.configure(state = "readonly")

        self.model_ID.configure(state="normal")
        self.model_ID.delete(0, tk.END)
        self.model_ID.insert(tk.END, next_id)
        self.model_ID.configure(state="readonly")

    def back_function(self):
        self.controller.mostra_frame("VehicleSection")
        gv.CurrentBrand = None
        self.controller.frames["CreateVehicle"].brand_listBox.selection_clear(0, tk.END)



