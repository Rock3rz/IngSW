import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from Src.Controllers.VehicleController import VehicleController
import Src.GlobalVariables.GlobalVariables as gv
from Src.GlobalVariables.GlobalVariables import vehicle_list
from Src.Class.Vehicle import Vehicle, FuelType


class CreateVehicle(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.vc = gv.vehicle_controller
        self.controller = controller
        self.current_fuel_type = None

        # Convert Listbox to Combobox for brands
        self.brand_listBox = ttk.Combobox(self, state="readonly")
        self.brand_listBox.grid(row=2, column=0, sticky=tk.NSEW)

        # Convert Listbox to Combobox for models
        self.model_listBox = ttk.Combobox(self, state="readonly")
        self.model_listBox.grid(row=2, column=1, sticky=tk.NSEW)

        # Campi di fill per creazione veicolo
        tk.Label(self, text="ID").grid(row=1, column=3, sticky=tk.NSEW)
        self.Vehicle_ID = tk.Entry(self)
        self.Vehicle_ID.grid(row=1, column=4, sticky=tk.NSEW)
        self.Vehicle_ID.configure(state="readonly")

        tk.Label(self, text="Brand").grid(row=2, column=3, sticky=tk.NSEW)
        self.Brand = tk.Entry(self)
        self.Brand.grid(row=2, column=4, sticky=tk.NSEW)
        self.Brand.configure(state="readonly")

        tk.Label(self, text="Modello").grid(row=3, column=3, sticky=tk.NSEW)
        self.Model = tk.Entry(self)
        self.Model.grid(row=3, column=4, sticky=tk.NSEW)
        self.Model.configure(state="readonly")

        tk.Label(self, text="Anno Registrazione").grid(row=4, column=3, sticky=tk.NSEW)
        self.Year = tk.Entry(self)
        self.Year.grid(row=4, column=4, sticky=tk.NSEW)
        self.Year.configure(state="readonly")

        tk.Label(self, text="Colore").grid(row=5, column=3, sticky=tk.NSEW)
        self.Color = tk.Entry(self)
        self.Color.grid(row=5, column=4, sticky=tk.NSEW)
        self.Color.configure(state="readonly")



        fuel_names = [fuel.name for fuel in FuelType]
        self.fuelTypeCompoBox = ttk.Combobox(self,values = fuel_names, state="disabled")
        self.fuelTypeCompoBox.grid(row=6, column=4, sticky=tk.NSEW)



        tk.Label(self, text="KM").grid(row=7, column=3, sticky=tk.NSEW)
        self.Kilometers = tk.Entry(self)
        self.Kilometers.grid(row=7, column=4, sticky=tk.NSEW)
        self.Kilometers.configure(state="readonly")

        tk.Label(self, text="Cilindrata").grid(row=8, column=3, sticky=tk.NSEW)
        self.Displacement = tk.Entry(self)
        self.Displacement.grid(row=8, column=4, sticky=tk.NSEW)
        self.Displacement.configure(state="readonly")

        tk.Label(self, text="Cavalli").grid(row=9, column=3, sticky=tk.NSEW)
        self.HP = tk.Entry(self)
        self.HP.grid(row=9, column=4, sticky=tk.NSEW)
        self.HP.configure(state="readonly")

        tk.Label(self, text="Targa").grid(row=10, column=3, sticky=tk.NSEW)
        self.NumberPlate = tk.Entry(self)
        self.NumberPlate.grid(row=10, column=4, sticky=tk.NSEW)
        self.NumberPlate.configure(state="readonly")

        tk.Label(self, text="Prezzo").grid(row=11, column = 3, sticky=tk.NSEW)
        self.Price = tk.Entry(self)
        self.Price.grid(row=11, column = 4, sticky=tk.NSEW)
        self.Price.configure(state="readonly")


        self.isAvailableTick = tk.BooleanVar()
        self.isAvailableCheckBox = tk.Checkbutton(self, text="Disponibile", variable=self.isAvailableTick)
        self.isAvailableCheckBox.grid(row=12, column=4, sticky=tk.NSEW)


        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("VehicleSection")).grid(row=3, column=0)
        tk.Button(self, text="Crea Brand", command=lambda: (self.vc.create_brand(), self.fill_brand_listbox())).grid(row=3, column=1, padx=10)
        tk.Button(self, text="Crea Model", command=lambda: self.check_brand_selected()).grid(row=3, column=2, padx=10)
        tk.Button(self, text="Salva", command = lambda: self.save_vehicle()).grid(row=20, column=3, padx=10)

        ##aggiorniamo le tabelle
        self.fill_brand_listbox()

        # bindings
        self.brand_listBox.bind("<<ComboboxSelected>>", self.on_select_brand)
        self.model_listBox.bind("<<ComboboxSelected>>", self.on_selected_model)
        self.fuelTypeCompoBox.bind("<<ComboboxSelected>>", self.on_selected_fuel)



    # Filling comboboxes
    def fill_brand_listbox(self):
        # Populate the brand combobox
        try:
            brands = list(gv.brand_list)
        except Exception:
            brands = []
        self.brand_listBox['values'] = brands
        self.brand_listBox.set("")

    def fill_model_listbox(self):
        # Populate the model combobox based on selected brand
        self.tmp_model_list = []
        values = []
        for model in gv.model_list:
            if model.brand == gv.CurrentBrand:
                self.tmp_model_list.append(model)
                values.append(f"{model.model_id}  {model.name}")
        self.model_listBox['values'] = values
        self.model_listBox.set("")

    def fill_vehicle_fields(self):
        for model in gv.model_list:
            if model.model_id == gv.CurrentModel:
                tmpModel = model


        self.Brand.configure(state="normal")
        self.Brand.delete(0, tk.END)
        self.Brand.insert(0, tmpModel.brand)
        self.Brand.configure(state="readonly")


        self.Model.configure(state="normal")
        self.Model.delete(0, tk.END)
        self.Model.insert(0, tmpModel.name)
        self.Model.configure(state="readonly")

        self.Displacement.configure(state="normal")
        self.Displacement.delete(0, tk.END)
        self.Displacement.insert(0, tmpModel.displacement)
        self.Displacement.configure(state="readonly")

        self.HP.configure(state="normal")
        self.HP.delete(0, tk.END)
        self.HP.insert(0, tmpModel.hp)
        self.HP.configure(state="readonly")


        if gv.vehicle_list:
            nextID = max(v.vehicle_id for v in gv.vehicle_list) + 1
        else:
            nextID = 1

        self.Vehicle_ID.configure(state="normal")
        self.Vehicle_ID.delete(0, tk.END)
        self.Vehicle_ID.insert(0, nextID)
        self.Vehicle_ID.configure(state="readonly")

    def unlock_fields(self):
        self.Year.configure(state="normal")
        self.Color.configure(state="normal")
        self.Kilometers.configure(state="normal")
        self.Price.configure(state="normal")
        self.NumberPlate.configure(state="normal")
        self.fuelTypeCompoBox.configure(state="readonly")

    def save_vehicle(self):
        self.vc.create_vehicle(
            gv.CurrentModel,
            self.Year.get(),
            self.Color.get(),
            self.current_fuel_type,
            self.Vehicle_ID.get(),
            self.isAvailableTick.get(),
            self.Kilometers.get(),
            self.NumberPlate.get(),
            self.Price.get()
        )


    # Conditional Checkers
    def check_brand_selected(self):
        if not gv.CurrentBrand:
            messagebox.showwarning("Errorino", "Non hai selezionato alcun brand!")
            return
        self.controller.frames["CreateModel"].loadModel()
        self.controller.mostra_frame("CreateModel")
        for model in gv.model_list:
            print(model.brand, model.name)


    def check_model_selected(self):
        print("Seleziona un modello")



    # eventi On_pressed
    def on_select_brand(self, event=None):
        # Get selected brand from combobox
        value = self.brand_listBox.get()
        if value:
            gv.CurrentBrand = value
            self.fill_model_listbox()
            print(f"Brand selezionato: {value}")

    def on_selected_model(self, event= None):
        # Get selected model from combobox and parse ID
        value_str = self.model_listBox.get()
        if value_str:
            try:
                value = int(value_str.split()[0])
                gv.CurrentModel = value
                print(gv.CurrentModel)
                self.unlock_fields()
                self.fill_vehicle_fields()
            except Exception:
                pass
            #sblocca i campi di fill

    def on_selected_fuel(self, event=None):
        value = self.fuelTypeCompoBox.get()
        if value:
            self.current_fuel_type = value
            print(f"Fuel type selected: {value}")



