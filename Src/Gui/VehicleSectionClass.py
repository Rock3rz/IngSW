import tkinter as tk

from Src.Controllers.VehicleController import VehicleController
import Src.GlobalVariables.GlobalVariables as gv
from tkinter import messagebox

# Classe di gestione e visione veicoli
class VehicleSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.vc = gv.vehicle_controller
        self.controller = controller
        self.supportList = []
        self.selected_vehicle = None

        # Dizionari per i check Brand
        self.brandTickValues = {}
        self.brandTicks = {}
        # Dizionari per i check Modelli
        self.modelTickValues = {}
        self.modelTicks = {}
        # Dizionari per i check Colori
        self.colorTickValues = {}
        self.colorTicks = {}
        # Dizionari per i check Alimentazione
        self.fuelTickValues = {}
        self.fuelTicks = {}

        # Variabili prezzo
        self.price_min_var = tk.StringVar()
        self.price_max_var = tk.StringVar()

        # Layout principale: due colonne (sinistra lista veicoli, destra filtri)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Sezioni
        self.left_frame = tk.Frame(self)
        self.right_frame = tk.Frame(self)
        self.left_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)
        self.right_frame.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)

        # Left frame
        self.left_frame.grid_columnconfigure(0, weight=1)
        self.left_frame.grid_columnconfigure(1, weight=1)
        self.left_frame.grid_rowconfigure(1, weight=1)

        tk.Label(self.left_frame, text="VehicleSection").grid(row=0, column=0, columnspan=2, sticky=tk.W)

        self.vehicle_listBox = tk.Listbox(self.left_frame)
        self.vehicle_listBox.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

        tk.Button(self.left_frame, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=2, column=0, sticky=tk.EW, pady=2)
        tk.Button(self.left_frame, text="Crea Veicolo", command=lambda: controller.mostra_frame("CreateVehicle")).grid(row=2, column=1, sticky=tk.EW, padx=5, pady=2)
        tk.Button(self.left_frame, text="Visualizza", command=self.can_view_vehicle).grid(row=3, column=0, sticky=tk.EW, pady=2)
        tk.Button(self.left_frame, text="Elimina", command=self.check_delete).grid(row=3, column=1, sticky=tk.EW, padx=5, pady=2)

        # Lista iniziale
        self.fill_vehicle_listbox(gv.vehicle_list)

        # Right frame: quattro colonne (0=Brand, 1=Modelli, 2=Colori, 3=Alimentazione)
        for col in range(4):
            self.right_frame.grid_columnconfigure(col, weight=1)
        self.right_frame.grid_rowconfigure(1, weight=1)

        # Etichette delle colonne
        tk.Label(self.right_frame, text="Brand").grid(row=0, column=0, sticky=tk.W, padx=5)
        tk.Label(self.right_frame, text="Modelli").grid(row=0, column=1, sticky=tk.W, padx=5)
        tk.Label(self.right_frame, text="Colori").grid(row=0, column=2, sticky=tk.W, padx=5)
        tk.Label(self.right_frame, text="Alimentazione").grid(row=0, column=3, sticky=tk.W, padx=5)

        # Contenitori check
        self.brandSection = tk.Frame(self.right_frame)
        self.brandSection.grid(row=1, column=0, sticky=tk.NSEW)
        self.modelSection = tk.Frame(self.right_frame)
        self.modelSection.grid(row=1, column=1, sticky=tk.NSEW)
        self.colorSection = tk.Frame(self.right_frame)
        self.colorSection.grid(row=1, column=2, sticky=tk.NSEW)
        self.fuelSection = tk.Frame(self.right_frame)
        self.fuelSection.grid(row=1, column=3, sticky=tk.NSEW)
        self.searchSection = tk.Frame(self.right_frame)
        self.searchSection.grid(row=3, column=3, sticky=tk.NSEW)

        self.mainFrame = tk.Frame(self.right_frame)
        self.mainFrame.grid(row = 1, column = 4, sticky = tk.NSEW)


        self.filter_tick_var = tk.BooleanVar()
        self.filter_tick = tk.Checkbutton(self.mainFrame, text="Filtra", variable=self.filter_tick_var, command = lambda: self.active_filter())
        self.filter_tick.grid(row = 0, column = 0, sticky = tk.NSEW)
        self.filter_tick_var.set(True)

        self.search_tick_var = tk.BooleanVar()
        self.search_tick = tk.Checkbutton(self.mainFrame, text="Ricerca", variable=self.search_tick_var, command = lambda: self.active_search())
        self.search_tick.grid(row = 0, column = 1, sticky = tk.NSEW)
        self.search_tick_var.set(False)



        self.searchBox = tk.Entry(self.searchSection)
        self.searchBox.grid(row=0, column=0, sticky=tk.EW, padx=5, pady=5)
        self.searchButton = tk.Button(self.searchSection, text="Search").grid(row = 0, column = 1, sticky=tk.EW, padx=5, pady=5)


        # Sezione prezzo (riga successiva)
        price_frame = tk.Frame(self.right_frame)
        price_frame.grid(row=2, column=0, columnspan=4, sticky=tk.EW, padx=5, pady=5)
        tk.Label(price_frame, text="Prezzo min").grid(row=0, column=0, sticky=tk.W)
        self.min_entry = tk.Entry(price_frame, textvariable=self.price_min_var, width=10)
        self.min_entry.grid(row=0, column=1, sticky=tk.W, padx=(2, 10))
        tk.Label(price_frame, text="Prezzo max").grid(row=0, column=2, sticky=tk.W)
        self.max_entry = tk.Entry(price_frame, textvariable=self.price_max_var, width=10)
        self.max_entry.grid(row=0, column=3, sticky=tk.W, padx=(2, 10))

        # Applica filtro alla pressione di Invio o all'uscita dal campo
        self.min_entry.bind("<Return>", lambda e: self.apply_filter())
        self.max_entry.bind("<Return>", lambda e: self.apply_filter())
        self.min_entry.bind("<FocusOut>", lambda e: self.apply_filter())
        self.max_entry.bind("<FocusOut>", lambda e: self.apply_filter())
        self.searchBox.bind("<KeyRelease>", lambda e: self.on_search_triggered())

        self.refresh_brand_checkboxes()
        self.refresh_model_checkboxes()  # inizialmente vuota (nessun brand selezionato)
        self.refresh_color_checkboxes()
        self.refresh_fuel_checkboxes()

        self.active_filter()

    def refresh_brand_checkboxes(self):
        # Pulisci precedenti
        for cb in self.brandTicks.values():
            cb.destroy()
        self.brandTickValues.clear()
        self.brandTicks.clear()

        # Crea i check per i brand
        for i, brand in enumerate(gv.brand_list):
            self.brandTickValues[i] = tk.BooleanVar()
            self.brandTicks[i] = tk.Checkbutton(
                self.brandSection,
                text=f"{brand}",
                variable=self.brandTickValues[i],
                command=self.on_brand_filter_change
            )
            self.brandTicks[i].grid(row=i, column=0, sticky=tk.W)

    def refresh_model_checkboxes(self):
        # Ricostruisci la colonna modelli in base ai brand selezionati
        for cb in self.modelTicks.values():
            cb.destroy()
        self.modelTickValues.clear()
        self.modelTicks.clear()

        selected_brands = self.get_selected_brands()
        if not selected_brands:
            return  # Nessun brand selezionato -> nessun modello mostrato

        # Filtra i modelli che appartengono ai brand selezionati
        filtered_models = [m for m in gv.model_list if m.brand in selected_brands]
        for idx, model in enumerate(filtered_models):
            self.modelTickValues[model.model_id] = tk.BooleanVar()
            self.modelTicks[model.model_id] = tk.Checkbutton(
                self.modelSection,
                text=f"{model.name}",
                variable=self.modelTickValues[model.model_id],
                command=self.apply_filter
            )
            self.modelTicks[model.model_id].grid(row=idx, column=0, sticky=tk.W)

    def refresh_color_checkboxes(self):
        # Pulisci precedenti
        for cb in self.colorTicks.values():
            cb.destroy()
        self.colorTickValues.clear()
        self.colorTicks.clear()
        # Colori disponibili da tutta la lista veicoli
        colors = sorted({v.color for v in gv.vehicle_list})
        for idx, color in enumerate(colors):
            self.colorTickValues[color] = tk.BooleanVar()
            self.colorTicks[color] = tk.Checkbutton(
                self.colorSection,
                text=str(color),
                variable=self.colorTickValues[color],
                command=self.apply_filter
            )
            self.colorTicks[color].grid(row=idx, column=0, sticky=tk.W)

    def refresh_fuel_checkboxes(self):
        # Pulisci precedenti
        for cb in self.fuelTicks.values():
            cb.destroy()
        self.fuelTickValues.clear()
        self.fuelTicks.clear()
        # Alimentazioni disponibili da tutta la lista veicoli
        fuels = sorted({v.fuel_type for v in gv.vehicle_list})
        for idx, fuel in enumerate(fuels):
            self.fuelTickValues[fuel] = tk.BooleanVar()
            self.fuelTicks[fuel] = tk.Checkbutton(
                self.fuelSection,
                text=str(fuel),
                variable=self.fuelTickValues[fuel],
                command=self.apply_filter
            )
            self.fuelTicks[fuel].grid(row=idx, column=0, sticky=tk.W)

    def get_selected_brands(self):
        selected = []
        for i, var in self.brandTickValues.items():
            if var.get():
                selected.append(gv.brand_list[i])
        return selected

    def get_selected_model_ids(self):
        return [mid for mid, var in self.modelTickValues.items() if var.get()]

    def fill_vehicle_listbox(self, vehicleList):
        self.vehicle_listBox.delete(0, tk.END)
        self.supportList = vehicleList
        for vehicle in self.supportList:
            self.vehicle_listBox.insert(
                tk.END,
                f"{vehicle.vehicle_id} {vehicle.model.brand} {vehicle.model.name} {vehicle.color} {vehicle.number_plate} {vehicle.price}"
            )

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

    def check_delete(self):
        self.vc.delete_vehicle()
        self.fill_vehicle_listbox(gv.vehicle_list)

    def on_brand_filter_change(self):
        # Cambiando i brand, aggiorna la colonna modelli e applica il filtro
        self.refresh_model_checkboxes()
        self.apply_filter()

    def apply_filter(self):
        # Calcola selezioni
        brand_bools = [self.brandTickValues[i].get() for i in self.brandTickValues]
        selected_model_ids = self.get_selected_model_ids()
        selected_colors = [c for c, var in self.colorTickValues.items() if var.get()]
        selected_fuels = [f for f, var in self.fuelTickValues.items() if var.get()]

        # Parsing prezzo
        def parse_price(val):
            val = val.strip()
            if not val:
                return None
            try:
                return float(val.replace(",", "."))
            except ValueError:
                return None
        price_min = parse_price(self.price_min_var.get())
        price_max = parse_price(self.price_max_var.get())

        # Applica filtraggio combinato brand+modelli+colori+alimentazione+prezzo
        filtered = self.vc.filter_vehicle(
            brand_bools,
            selected_model_ids,
            colors=selected_colors,
            fuels=selected_fuels,
            price_min=price_min,
            price_max=price_max,
        )
        self.fill_vehicle_listbox(filtered)

    def active_search(self):
        self.fill_vehicle_listbox(gv.vehicle_list)
        self.search_tick_var.set(True)
        self.filter_tick_var.set(False)

        # Reset e disabilita brand
        for var, cb in zip(self.brandTickValues.values(), self.brandTicks.values()):
            var.set(False)
            cb.config(state=tk.DISABLED)

        # Reset e disabilita modelli
        for var, cb in zip(self.modelTickValues.values(), self.modelTicks.values()):
            var.set(False)
            cb.config(state=tk.DISABLED)

        # Reset e disabilita colori
        for var, cb in zip(self.colorTickValues.values(), self.colorTicks.values()):
            var.set(False)
            cb.config(state=tk.DISABLED)

        # Reset e disabilita fuel
        for var, cb in zip(self.fuelTickValues.values(), self.fuelTicks.values()):
            var.set(False)
            cb.config(state=tk.DISABLED)

        # Reset campi prezzo
        self.price_min_var.set("")
        self.price_max_var.set("")
        self.min_entry.config(state="disabled")
        self.max_entry.config(state="disabled")

        # Abilita la searchbox
        self.searchBox.config(state="normal")

    def active_filter(self):
        self.fill_vehicle_listbox(gv.vehicle_list)
        self.search_tick_var.set(False)
        self.filter_tick_var.set(True)
        for brand in self.brandTicks.values():
            brand.config(state=tk.NORMAL)
        for model in self.modelTicks.values():
            model.config(state=tk.NORMAL)
        for color in self.colorTicks.values():
            color.config(state=tk.NORMAL)
        for fuel in self.fuelTicks.values():
            fuel.config(state=tk.NORMAL)
        self.min_entry.delete(0, tk.END)
        self.max_entry.delete(0, tk.END)
        self.min_entry.config(state="normal")
        self.max_entry.config(state="normal")
        self.searchBox.delete(0, tk.END)
        self.searchBox.config(state="disabled")

    def on_search_triggered(self):
        self.fill_vehicle_listbox(self.vc.search_vehicle(self.searchBox.get()))










