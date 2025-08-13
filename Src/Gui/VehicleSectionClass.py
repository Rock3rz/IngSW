import tkinter as tk
from traceback import print_tb

from Src.Controllers.VehicleController import VehicleController
import Src.GlobalVariables.GlobalVariables as gv
from Src.GlobalVariables.GlobalVariables import CurrentBrand
from tkinter import messagebox, simpledialog

#Classe di gestione e visione veicoli
class VehicleSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.vc = gv.vehicle_controller
        self.controller = controller
        self.supportList = []
        self.selected_vehicle = None
        tk.Label(self, text="VehicleSection").grid(row=1, column=0)



        self.vehicle_listBox = tk.Listbox(self)
        self.vehicle_listBox.grid(row=2, column=2,columnspan=10 ,sticky=tk.NSEW)

        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=3, column=0)
        tk.Button(self, text="Crea Veicolo", command = lambda: controller.mostra_frame("CreateVehicle")).grid(row=3, column=3, padx = 10)
        tk.Button(self, text="Visualizza", command = lambda: self.can_view_vehicle()).grid(row=3, column=4, padx = 10)
        tk.Button(self, text="Elimina", command = lambda: self.check_delete()).grid(row=3, column=5, padx = 10)


        #self.vehicle_listBox.bind("<<ListboxSelect>>", self.on_select)
        self.fill_vehicle_listbox()

    def fill_vehicle_listbox(self):
        self.vehicle_listBox.delete(0, tk.END)
        self.supportList = gv.vehicle_list
        for vehicle in self.supportList:
            self.vehicle_listBox.insert(tk.END, f"{vehicle.vehicle_id} {vehicle.model.brand} {vehicle.model.name} {vehicle.color} {vehicle.number_plate} {vehicle.price}")

    def can_view_vehicle(self):
        selection = self.vehicle_listBox.curselection()
        if not selection:
            messagebox.showwarning("Errore", "Nessun veicolo selezionato!")
            return

        index = selection[0]
        value = self.vehicle_listBox.get(index).split()[0]

        for vehicle in gv.vehicle_list:
            if int(vehicle.vehicle_id) == int(value):
                gv.CurrentVehicle = vehicle

        self.controller.frames["VehicleView"].load_model_infos()
        self.controller.mostra_frame("VehicleView")

    '''
    def on_select(self, event=None):
        if event:
            widget = event.widget
            self.selected_vehicle = widget.curselection()
        else:
            self.selected_vehicle = self.vehicle_listBox.curselection()

        if self.selected_vehicle:
            self.selected_vehicle = self.selected_vehicle[0]
            value = self.vehicle_listBox.get(self.selected_vehicle).split()[0]
            for vehicle in gv.vehicle_list:
                if int(vehicle.vehicle_id) == int(value):
                    gv.CurrentVehicle = vehicle
            self.controller.frames["VehicleView"].load_model_infos()
    '''


    def check_delete(self):
        self.vc.delete_vehicle()
        self.fill_vehicle_listbox()



