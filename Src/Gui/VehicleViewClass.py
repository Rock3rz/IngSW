import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv

class VehicleView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        tk.Label(self, text="VehicleView").grid(row=0, column=0)

        self.isAvailableVar = tk.BooleanVar()

        tk.Label(self, text="Brand").grid(row=1, column=0)
        self.brand = tk.Entry(self)
        self.brand.grid(row=1, column=1)

        tk.Label(self, text="Modello").grid(row=2, column=0)
        self.model = tk.Entry(self)
        self.model.grid(row=2, column=1)

        tk.Label(self, text="Cilindrata").grid(row=3, column=0)
        self.displacement = tk.Entry(self)
        self.displacement.grid(row=3, column=1)

        tk.Label(self, text="Cavalli").grid(row=4, column=0)
        self.hp = tk.Entry(self)
        self.hp.grid(row=4, column=1)

        tk.Label(self, text="Targa").grid(row=5, column=0)
        self.number_plate = tk.Entry(self)
        self.number_plate.grid(row=5, column=1)

        tk.Label(self, text="Colore").grid(row=6, column=0)
        self.color = tk.Entry(self)
        self.color.grid(row=6, column=1)

        tk.Label(self, text="Anno Registrazione").grid(row=7, column=0)
        self.year = tk.Entry(self)
        self.year.grid(row=7, column=1)

        tk.Label(self, text="Prezzo").grid(row=8, column=0)
        self.price = tk.Entry(self)
        self.price.grid(row=8, column=1)

        tk.Label(self, text="Km").grid(row=9, column=0)
        self.kilometers = tk.Entry(self)
        self.kilometers.grid(row=9, column=1)

        tk.Label(self, text="ID").grid(row=10, column=0)
        self.vehicle_id = tk.Entry(self)
        self.vehicle_id.grid(row=10, column=1)

        tk.Label(self, text="Tipo Carburante").grid(row=11, column=0)
        self.fuel_type = tk.Entry(self)
        self.fuel_type.grid(row=11, column=1)

        self.isAvailableTickBox = tk.Checkbutton(
            self, text="Disponibile", variable=self.isAvailableVar
        )
        self.isAvailableTickBox.grid(row=12, column=1)

        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("VehicleSection")).grid(row=12, column=0)

    def load_model_infos(self):
        if gv.CurrentVehicle is not None:
            self.unlock_fields()
            self.clear_fields()
            self.brand.insert(0, gv.CurrentVehicle.model.brand)
            self.model.insert(0, gv.CurrentVehicle.model.name)
            self.displacement.insert(0, gv.CurrentVehicle.model.displacement)
            self.hp.insert(0, gv.CurrentVehicle.model.hp)
            self.number_plate.insert(0, gv.CurrentVehicle.number_plate)
            self.color.insert(0, gv.CurrentVehicle.color)
            self.year.insert(0, gv.CurrentVehicle.registration_year)
            self.price.insert(0, gv.CurrentVehicle.price)
            self.kilometers.insert(0, gv.CurrentVehicle.km)
            self.vehicle_id.insert(0, gv.CurrentVehicle.vehicle_id)
            self.fuel_type.insert(0, gv.CurrentVehicle.fuel_type)
            self.isAvailableVar.set(gv.CurrentVehicle.is_available)
            self.lock_fields()

    def clear_fields(self):
        self.brand.delete(0, tk.END)
        self.model.delete(0, tk.END)
        self.displacement.delete(0, tk.END)
        self.hp.delete(0, tk.END)
        self.number_plate.delete(0, tk.END)
        self.color.delete(0, tk.END)
        self.year.delete(0, tk.END)
        self.price.delete(0, tk.END)
        self.kilometers.delete(0, tk.END)
        self.vehicle_id.delete(0, tk.END)
        self.fuel_type.delete(0, tk.END)
        self.isAvailableVar.set(False)

    def unlock_fields(self):
        self.brand.configure(state="normal")
        self.model.configure(state="normal")
        self.displacement.configure(state="normal")
        self.hp.configure(state="normal")
        self.number_plate.configure(state="normal")
        self.color.configure(state="normal")
        self.year.configure(state="normal")
        self.price.configure(state="normal")
        self.kilometers.configure(state="normal")
        self.vehicle_id.configure(state="normal")
        self.fuel_type.configure(state="normal")
        self.isAvailableTickBox.configure(state="normal")

    def lock_fields(self):
        self.brand.configure(state="readonly")
        self.model.configure(state="readonly")
        self.displacement.configure(state="readonly")
        self.hp.configure(state="readonly")
        self.number_plate.configure(state="readonly")
        self.color.configure(state="readonly")
        self.year.configure(state="readonly")
        self.price.configure(state="readonly")
        self.kilometers.configure(state="readonly")
        self.vehicle_id.configure(state="readonly")
        self.fuel_type.configure(state="readonly")
        self.isAvailableTickBox.configure(state="disabled")




