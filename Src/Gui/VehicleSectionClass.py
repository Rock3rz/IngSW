import tkinter as tk
from Src.Controllers.VehicleController import VehicleController
import Src.GlobalVariables.GlobalVariables as gv
from Src.GlobalVariables.GlobalVariables import CurrentBrand
from tkinter import messagebox, simpledialog

#Classe di gestione e visione veicoli
class VehicleSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        #self.vc = VehicleController()
        self.controller = controller

        tk.Label(self, text="VehicleSection").grid(row=1, column=0)



        self.vehicle_listBox = tk.Listbox(self)
        self.vehicle_listBox.grid(row=2, column=2, sticky=tk.NSEW)

        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=3, column=0)
        tk.Button(self, text="Crea Veicolo", command = lambda: controller.mostra_frame("CreateVehicle")).grid(row=3, column=3, padx = 10)
        tk.Button(self, text="Visualizza").grid(row=3, column=4, padx = 10)
        tk.Button(self, text="Elimina").grid(row=3, column=5, padx = 10)




