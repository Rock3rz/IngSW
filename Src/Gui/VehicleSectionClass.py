import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv
from tkinter import messagebox
import os
from PIL import Image
import customtkinter as ctk

# Classe di gestione e visione veicoli
class VehicleSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")
        self.vc = gv.vehicle_controller
        self.controller = controller
        self.supportList = []
        self.selected_vehicle = None


        base_path = os.path.dirname(__file__)
        icon_dir = os.path.join(base_path, "..", "Images", "Icone")
        logout_img = Image.open(os.path.join(icon_dir, "Logout.png"))

        logout_icon = ctk.CTkImage(light_image=logout_img, dark_image=logout_img, size=(30, 30))

        header_frame = tk.Frame(self, bg="#000534", height=50)
        header_frame.pack(side="top", fill="x")
        header_frame.pack_propagate(False)

        back_btn = ctk.CTkButton(header_frame,
                                 text="Back",
                                 font=("Calisto MT", 18, "bold"),
                                 image=logout_icon,
                                 compound="left",
                                 width=150,
                                 corner_radius=10,
                                 fg_color="white",
                                 border_color="#000534",
                                 border_width=2,
                                 text_color="#000534",
                                 command=lambda: controller.mostra_frame("MainMenu"))
        back_btn.pack(side="left", padx=(20, 0))

        title_frame = tk.Frame(self, bg="#cfd7dc", height=40)
        title_frame.pack(side="top", fill="x")
        title_frame.pack_propagate(False)

        label_title = tk.Label(title_frame,
                               text="Parco Auto",
                               font=("Calisto MT", 20, "bold"),
                               bg="#cfd7dc",
                               fg="#000534")
        label_title.pack(side="left", padx=(10, 0))
        label_title.pack_propagate(False)

        header_border = tk.Frame(self, bg="#bfc9cf", height=2)
        header_border.pack(side="top", fill="x")
        header_border.pack_propagate(False)

        btw_border = tk.Frame(self, bg="#dee4e9", height=30)
        btw_border.pack(side="top", fill="x")
        btw_border.pack_propagate(False)

        main_frame = tk.Frame(self, bg="#dee4e9")
        main_frame.pack(side="top", fill="both", expand=True)

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

        self.price_min_var = tk.StringVar()
        self.price_max_var = tk.StringVar()


        main_frame.grid_columnconfigure(0, weight=0, minsize=30)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_columnconfigure(2, weight=1)
        main_frame.grid_columnconfigure(3, weight=0, minsize=30)
        main_frame.grid_rowconfigure(0, weight=1)

        # Spazi laterali
        tk.Frame(main_frame, bg="#dee4e9").grid(row=0, column=0, sticky="ns")
        tk.Frame(main_frame, bg="#dee4e9").grid(row=0, column=3, sticky="ns")

        # Sezioni
        self.left_frame = tk.Frame(main_frame, bg="#cfd7dc")
        self.right_frame = tk.Frame(main_frame, bg="#cfd7dc")
        self.left_frame.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)
        self.right_frame.grid(row=0, column=2, sticky=tk.NSEW, padx=5, pady=5)

        self.left_frame.grid_columnconfigure(0, weight=1)
        self.left_frame.grid_columnconfigure(1, weight=0)
        self.left_frame.grid_rowconfigure(1, weight=1)

        self.vehicle_listBox = tk.Listbox(self.left_frame,
                                          font=("Calibri", 12),
                                          width=50,
                                          height=50,
                                          bg="#dee4e9"
                                          )
        self.vehicle_listBox.grid(row=1, column=0, columnspan=10, sticky=tk.NSEW, padx=10, pady=(20,0))

        scrollbar = tk.Scrollbar(self.left_frame, orient="vertical", command=self.vehicle_listBox.yview)
        scrollbar.grid(row=1, column=2, sticky="nse", pady=(20, 0))
        self.vehicle_listBox.config(yscrollcommand=scrollbar.set)

        underListbox_frame = tk.Frame(self.left_frame, bg="#cfd7dc", height=10, width=400)
        underListbox_frame.grid(row=2, column=0, columnspan=10, pady=(0, 30))

        btn_frame = tk.Frame(self.left_frame, bg="#cfd7dc")
        btn_frame.grid(row=0, column=0, columnspan=2, pady=5)

        create_btn = ctk.CTkButton(btn_frame, text="Crea Veicolo", font=("Calisto MT", 18, "bold"), width=150, corner_radius=10,
                                   fg_color="white", border_color="#000534", border_width=2,
                                   text_color="#000534", command=lambda: controller.mostra_frame("CreateVehicle"))
        create_btn.pack(side="left", padx=5, pady=(20, 0))

        view_btn = ctk.CTkButton(btn_frame, text="Visualizza", font=("Calisto MT", 18, "bold"), width=150, corner_radius=10,
                                 fg_color="white", border_color="#000534", border_width=2,
                                 text_color="#000534", command=self.can_view_vehicle)
        view_btn.pack(side="left", padx=5, pady=(20, 0))

        delete_btn = ctk.CTkButton(btn_frame, text="Elimina",font=("Calisto MT", 18, "bold"), width=150, corner_radius=10,
                                   fg_color="white", border_color="#000534", border_width=2,
                                   text_color="#000534", command=self.check_delete)
        delete_btn.pack(side="left", padx=5, pady=(20, 0))

        # Lista iniziale
        self.fill_vehicle_listbox(gv.vehicle_list)


        self.right_frame.grid_columnconfigure(0, weight=0, minsize=12)
        for col in (1, 3, 5, 7):
            self.right_frame.grid_columnconfigure(col, weight=1)
        for col in (2, 4, 6):
            self.right_frame.grid_columnconfigure(col, weight=0, minsize=12)

        self.right_frame.grid_rowconfigure(3, weight=1)

        self.mainFrame = tk.Frame(self.right_frame, bg="#cfd7dc")
        self.mainFrame.grid(row=0, column=0, columnspan=8, sticky=tk.EW, padx=5, pady=(0, 5))

        self.filter_tick_var = tk.BooleanVar()
        self.filter_tick = ctk.CTkCheckBox(self.mainFrame,
                                           text="Filtra",
                                           font=("Calisto MT", 15, "bold"),
                                           width=100,
                                           corner_radius=10,
                                           fg_color="#000534",
                                           border_color="#000534",
                                           border_width=2,
                                           text_color="#000534",
                                           variable=self.filter_tick_var,
                                           command=self.active_filter)
        self.filter_tick.grid(row=0, column=0, sticky=tk.W, padx=(250, 10), pady=(10,0))
        self.filter_tick_var.set(True)

        self.search_tick_var = tk.BooleanVar()
        self.search_tick = ctk.CTkCheckBox(self.mainFrame,
                                           text="Ricerca",
                                           font=("Calisto MT", 15, "bold"),
                                           width=100,
                                           corner_radius=10,
                                           fg_color="#000534",
                                           border_color="#000534",
                                           border_width=2,
                                           text_color="#000534",
                                           variable=self.search_tick_var,
                                           command=self.active_search)
        self.search_tick.grid(row=0, column=1, sticky=tk.W, padx=(170, 10), pady=(10,0))
        self.search_tick_var.set(False)

        base_path = os.path.dirname(__file__)
        icon_dir = os.path.join(base_path, "..", "Images", "Icone")
        search_img = Image.open(os.path.join(icon_dir, "Ricerca.png"))


        self.search_icon = ctk.CTkImage(light_image=search_img, dark_image=search_img, size=(24, 24))

        self.searchSection = tk.Frame(self.right_frame, bg="#cfd7dc")
        self.searchSection.grid(row=1, column=0, columnspan=8, sticky=tk.EW, padx=5, pady=(0, 5))

        self.searchSection.grid_columnconfigure(0, weight=1)

        self.searchBox = ctk.CTkEntry(self.searchSection,
                                      font=("Calisto MT", 15),
                                      width=200,
                                      corner_radius=10,
                                      fg_color="white",
                                      text_color="#000534",
                                      border_color="#000534",
                                      border_width=2)
        self.searchBox.grid(row=0, column=0, sticky=tk.EW, padx=(5, 2), pady=5)

        icon_holder = tk.Frame(self.searchSection, bg="#cfd7dc")
        icon_holder.grid(row=0, column=1, sticky="w", padx=(2, 5), pady=5)
        icon_label = ctk.CTkLabel(icon_holder, image=self.search_icon, text="")
        icon_label.pack()


        tk.Frame(self.right_frame, bg="#dee4e9", width=8).grid(row=2, column=0, sticky="ns")
        tk.Label(self.right_frame, text="Brand", font=("Calisto MT", 14, "bold"), bg="#cfd7dc", fg="#000534").grid(row=2, column=1, sticky=tk.W, padx=5)
        tk.Label(self.right_frame, text="Modelli", font=("Calisto MT", 14, "bold"), bg="#cfd7dc", fg="#000534").grid(row=2, column=3, sticky=tk.W, padx=5)
        tk.Label(self.right_frame, text="Colori", font=("Calisto MT", 14, "bold"), bg="#cfd7dc", fg="#000534").grid(row=2, column=5, sticky=tk.W, padx=5)
        tk.Label(self.right_frame, text="Alimentazione", font=("Calisto MT", 14, "bold"), bg="#cfd7dc", fg="#000534").grid(row=2, column=7, sticky=tk.W, padx=5)


        tk.Frame(self.right_frame, bg="#dee4e9", width=8).grid(row=2, column=2, sticky="ns")
        tk.Frame(self.right_frame, bg="#dee4e9", width=8).grid(row=2, column=4, sticky="ns")
        tk.Frame(self.right_frame, bg="#dee4e9", width=8).grid(row=2, column=6, sticky="ns")

        tk.Frame(self.right_frame, bg="#dee4e9", width=8).grid(row=3, column=0, sticky="ns")
        self.brandSection = ctk.CTkScrollableFrame(self.right_frame, fg_color="#cfd7dc")
        self.brandSection.grid(row=3, column=1, sticky=tk.NSEW)

        tk.Frame(self.right_frame, bg="#dee4e9", width=8).grid(row=3, column=2, sticky="ns")
        self.modelSection = ctk.CTkScrollableFrame(self.right_frame, fg_color="#cfd7dc")
        self.modelSection.grid(row=3, column=3, sticky=tk.NSEW)
        tk.Frame(self.right_frame, bg="#dee4e9", width=8).grid(row=3, column=4, sticky="ns")
        self.colorSection = tk.Frame(self.right_frame, bg="#cfd7dc")
        self.colorSection.grid(row=3, column=5, sticky=tk.NSEW)
        tk.Frame(self.right_frame, bg="#dee4e9", width=8).grid(row=3, column=6, sticky="ns")
        self.fuelSection = tk.Frame(self.right_frame, bg="#cfd7dc")
        self.fuelSection.grid(row=3, column=7, sticky=tk.NSEW)

        tk.Label(self.fuelSection, text="Disponibilità", font=("Calisto MT", 14, "bold"), bg="#cfd7dc",
                 fg="#000534").grid(row=100, column=0, sticky=tk.W, pady=(20, 5), padx=5)

        self.unavailable_tick_var = tk.BooleanVar()
        self.sold_tick_var = tk.BooleanVar()
        self.available_tick_var = tk.BooleanVar()

        self.unavailable_tick = ctk.CTkCheckBox(
            self.fuelSection,
            text="Prenotati",
            font=("Calisto MT", 15, "bold"),
            width=100,
            corner_radius=10,
            fg_color="#000534",
            border_color="#000534",
            border_width=2,
            text_color="#000534",
            variable=self.unavailable_tick_var,
            command=lambda: self.show_available_vehicle(self.unavailable_tick_var.get(), self.sold_tick_var.get(), self.available_tick_var.get())
        )
        self.unavailable_tick.grid(row=101, column=0, sticky=tk.W, padx=5, pady=(5, 0))
        self.unavailable_tick_var.set(False)

        self.sold_tick = ctk.CTkCheckBox(
            self.fuelSection,
            text="Venduti",
            font=("Calisto MT", 15, "bold"),
            width=100,
            corner_radius=10,
            fg_color="#000534",
            border_color="#000534",
            border_width=2,
            text_color="#000534",
            variable=self.sold_tick_var,
            command=lambda: self.show_available_vehicle(self.unavailable_tick_var.get(), self.sold_tick_var.get(), self.available_tick_var.get())
        )
        self.sold_tick.grid(row=102, column=0, sticky=tk.W, padx=5, pady=(5, 0))
        self.sold_tick_var.set(False)

        self.available_tick = ctk.CTkCheckBox(self.fuelSection,
                                              text="Disponibili",
                                              font=("Calisto MT", 15, "bold"),
                                              width=100,
                                              corner_radius=10,
                                              fg_color="#000534",
                                              border_color="#000534",
                                              border_width=2,
                                              text_color="#000534",
                                              variable=self.available_tick_var,
                                              command=lambda: self.show_available_vehicle(self.unavailable_tick_var.get(), self.sold_tick_var.get(), self.available_tick_var.get()))
        self.available_tick.grid(row=103, column=0, sticky=tk.W, padx=5, pady=(5, 0))
        self.available_tick_var.set(False)

        price_frame = tk.Frame(self.right_frame, bg="#cfd7dc")
        price_frame.grid(row=13, column=0, columnspan=8, sticky=tk.EW, padx=5, pady=10)
        price_frame.grid_columnconfigure(0, weight=1)
        price_frame.grid_columnconfigure(1, weight=0)
        price_frame.grid_columnconfigure(2, weight=1)

        price_label = tk.Label(price_frame,
                               text="Prezzo (€)",
                               font=("Calisto MT", 14, "bold"),
                               bg="#cfd7dc",
                               fg="#000534")
        price_label.grid(row=0, column=1, pady=(0, 5))


        prices = [v.price for v in gv.vehicle_list] if gv.vehicle_list else []
        self.min_price = int(min(prices)) if prices else 0
        self.max_price = int(max(prices)) if prices else 100000


        self.sel_min_price = tk.IntVar(value=self.min_price)
        self.sel_max_price = tk.IntVar(value=self.max_price)


        slider_wrap = tk.Frame(price_frame, bg="#cfd7dc")
        slider_wrap.grid(row=1, column=0, columnspan=3, sticky=tk.EW, padx=40)
        slider_wrap.grid_columnconfigure(0, weight=1)
        slider_wrap.grid_columnconfigure(1, weight=1)
        self.min_slider = ctk.CTkSlider(slider_wrap, from_=self.min_price, to=self.max_price,
                                        command=lambda v: self.on_price_change(None))
        self.min_slider.grid(row=0, column=0, sticky=tk.EW, padx=(0, 10))
        self.min_slider.set(self.min_price)
        self.max_slider = ctk.CTkSlider(slider_wrap, from_=self.min_price, to=self.max_price,
                                        command=lambda v: self.on_price_change(None))
        self.max_slider.grid(row=0, column=1, sticky=tk.EW, padx=(10, 0))
        self.max_slider.set(self.max_price)
        self._range_slider_fallback = True

        self.price_min_lbl = tk.Label(price_frame, text=f"{self.sel_min_price.get()} €", font=("Calisto MT", 10, "bold"),
                               bg="#cfd7dc",
                               fg="#000534")
        self.price_min_lbl.grid(row=2, column=0, sticky=tk.W, padx=10, pady=(5, 0))
        self.price_max_lbl = tk.Label(price_frame, text=f"{self.sel_max_price.get()} €", font=("Calisto MT", 10, "bold"),
                               bg="#cfd7dc",
                               fg="#000534")
        self.price_max_lbl.grid(row=2, column=2, sticky=tk.E, padx=10, pady=(5, 0))


        self.searchBox.bind("<KeyRelease>", lambda e: self.on_search_triggered())

        self.refresh_brand_checkboxes()
        self.refresh_model_checkboxes()
        self.refresh_color_checkboxes()
        self.refresh_fuel_checkboxes()

        self.active_filter()

    def refresh_brand_checkboxes(self):
        for cb in self.brandTicks.values():
            cb.destroy()
        self.brandTickValues.clear()
        self.brandTicks.clear()

        for i, brand in enumerate(gv.brand_list):
            self.brandTickValues[i] = tk.BooleanVar()
            self.brandTicks[i] = ctk.CTkCheckBox(
                self.brandSection,
                text=f"{brand}",
                variable=self.brandTickValues[i],
                command=self.on_brand_filter_change,
                font=("Calisto MT", 14, "bold"),
                corner_radius=10,
                fg_color="#000534",
                border_color="#000534",
                border_width=2,
                text_color="#000534",
            )
            self.brandTicks[i].grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)

    def refresh_model_checkboxes(self):
        for cb in self.modelTicks.values():
            cb.destroy()
        self.modelTickValues.clear()
        self.modelTicks.clear()

        selected_brands = self.get_selected_brands()
        if not selected_brands:
            return

        # Filtra i modelli che appartengono ai brand selezionati
        filtered_models = [m for m in gv.model_list if m.brand in selected_brands]
        for idx, model in enumerate(filtered_models):
            self.modelTickValues[model.model_id] = tk.BooleanVar()
            self.modelTicks[model.model_id] = ctk.CTkCheckBox(
                self.modelSection,
                text=f"{model.name}",
                variable=self.modelTickValues[model.model_id],
                command=self.apply_filter,
                font=("Calisto MT", 14, "bold"),
                corner_radius=10,
                fg_color="#000534",
                border_color="#000534",
                border_width=2,
                text_color="#000534",
            )
            self.modelTicks[model.model_id].grid(row=idx, column=0, sticky=tk.W, padx=5, pady=2)

    def refresh_color_checkboxes(self):
        for cb in self.colorTicks.values():
            cb.destroy()
        self.colorTickValues.clear()
        self.colorTicks.clear()
        colors = sorted({v.color for v in gv.vehicle_list})
        for idx, color in enumerate(colors):
            self.colorTickValues[color] = tk.BooleanVar()
            self.colorTicks[color] = ctk.CTkCheckBox(
                self.colorSection,
                text=str(color),
                variable=self.colorTickValues[color],
                command=self.apply_filter,
                font=("Calisto MT", 14, "bold"),
                corner_radius=10,
                fg_color="#000534",
                border_color="#000534",
                border_width=2,
                text_color="#000534",
            )
            self.colorTicks[color].grid(row=idx, column=0, sticky=tk.W, padx=5, pady=2)

    def refresh_fuel_checkboxes(self):
        for cb in self.fuelTicks.values():
            cb.destroy()
        self.fuelTickValues.clear()
        self.fuelTicks.clear()
        fuels = sorted({v.fuel_type for v in gv.vehicle_list})
        for idx, fuel in enumerate(fuels):
            self.fuelTickValues[fuel] = tk.BooleanVar()
            self.fuelTicks[fuel] = ctk.CTkCheckBox(
                self.fuelSection,
                text=str(fuel),
                variable=self.fuelTickValues[fuel],
                command=self.apply_filter,
                font=("Calisto MT", 14, "bold"),
                corner_radius=10,
                fg_color="#000534",
                border_color="#000534",
                border_width=2,
                text_color="#000534",
            )
            self.fuelTicks[fuel].grid(row=idx, column=0, sticky=tk.W, padx=5, pady=2)

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
        self.refresh_model_checkboxes()
        self.apply_filter()

    def apply_filter(self):
        brand_bools = [self.brandTickValues[i].get() for i in self.brandTickValues]
        selected_model_ids = self.get_selected_model_ids()
        selected_colors = [c for c, var in self.colorTickValues.items() if var.get()]
        selected_fuels = [f for f, var in self.fuelTickValues.items() if var.get()]

        price_min, price_max = self.get_selected_price_range()

        filtered = self.vc.filter_vehicle(
            brand_bools,
            selected_model_ids,
            colors=selected_colors,
            fuels=selected_fuels,
            price_min=price_min,
            price_max=price_max,
        )
        self.fill_vehicle_listbox(filtered)

    def get_selected_price_range(self):
        # Restituisce (min, max) selezionati oppure (None, None) se l'intervallo è completo
        try:
            if hasattr(self, "_range_slider_fallback") and not self._range_slider_fallback:
                values = self.price_slider.get()
                sel_min = int(values[0]) if isinstance(values, (list, tuple)) else int(values)
                sel_max = int(values[1]) if isinstance(values, (list, tuple)) else int(values)
            elif hasattr(self, "_range_slider_fallback") and self._range_slider_fallback:
                sel_min = int(self.min_slider.get())
                sel_max = int(self.max_slider.get())
            else:
                return None, None
        except Exception:
            return None, None

        self.sel_min_price.set(sel_min)
        self.sel_max_price.set(sel_max)
        if hasattr(self, "price_min_lbl") and hasattr(self, "price_max_lbl"):
            self.price_min_lbl.config(text=f"{sel_min} €")
            self.price_max_lbl.config(text=f"{sel_max} €")

        if sel_min <= self.min_price and sel_max >= self.max_price:
            return None, None
        return float(sel_min), float(sel_max)

    def on_price_change(self, _event):
        if self.filter_tick_var.get():
            self.apply_filter()

    def active_search(self):
        self.fill_vehicle_listbox(gv.vehicle_list)
        self.search_tick_var.set(True)
        self.filter_tick_var.set(False)


        for var, cb in zip(self.brandTickValues.values(), self.brandTicks.values()):
            var.set(False)
            cb.configure(state=tk.DISABLED)


        for var, cb in zip(self.modelTickValues.values(), self.modelTicks.values()):
            var.set(False)
            cb.configure(state=tk.DISABLED)


        for var, cb in zip(self.colorTickValues.values(), self.colorTicks.values()):
            var.set(False)
            cb.configure(state=tk.DISABLED)


        for var, cb in zip(self.fuelTickValues.values(), self.fuelTicks.values()):
            var.set(False)
            cb.configure(state=tk.DISABLED)


        if hasattr(self, "_range_slider_fallback") and not self._range_slider_fallback:
            try:
                self.price_slider.configure(state="disabled")
            except Exception:
                pass
        elif hasattr(self, "_range_slider_fallback") and self._range_slider_fallback:
            try:
                self.min_slider.configure(state="disabled")
                self.max_slider.configure(state="disabled")
            except Exception:
                pass


        self.searchBox.configure(state="normal")

    def active_filter(self):
        self.fill_vehicle_listbox(gv.vehicle_list)
        self.search_tick_var.set(False)
        self.filter_tick_var.set(True)
        for brand in self.brandTicks.values():
            brand.configure(state=tk.NORMAL)
        for model in self.modelTicks.values():
            model.configure(state=tk.NORMAL)
        for color in self.colorTicks.values():
            color.configure(state=tk.NORMAL)
        for fuel in self.fuelTicks.values():
            fuel.configure(state=tk.NORMAL)

        if hasattr(self, "_range_slider_fallback") and not self._range_slider_fallback:
            try:
                self.price_slider.configure(state="normal")
                # reset all range
                if hasattr(self.price_slider, "set"):
                    self.price_slider.set(self.min_price, self.max_price)
            except Exception:
                pass
        elif hasattr(self, "_range_slider_fallback") and self._range_slider_fallback:
            try:
                self.min_slider.configure(state="normal")
                self.max_slider.configure(state="normal")
                self.min_slider.set(self.min_price)
                self.max_slider.set(self.max_price)
            except Exception:
                pass

        if hasattr(self, "price_min_lbl") and hasattr(self, "price_max_lbl"):
            self.price_min_lbl.config(text=f"{self.min_price} €")
            self.price_max_lbl.config(text=f"{self.max_price} €")

        self.searchBox.delete(0, tk.END)
        self.searchBox.configure(state="disabled")

    def on_search_triggered(self):
        self.fill_vehicle_listbox(self.vc.search_vehicle(self.searchBox.get()))

    def show_available_vehicle(self, reserved: bool, sold: bool, available: bool):
        # Filtra stato disponibilità:
        # - Prenotati: is_available == False e sold == False
        # - Venduti: sold == True
        # - Disponibili: is_available == True e sold == False
        # - Entrambi:  tutti i non disponibili
        # - Nessuno:   tutti i veicoli
        if reserved and not sold:
            result = [v for v in gv.vehicle_list if (not v.is_available) and (not bool(getattr(v, 'sold', False)))]
        elif sold:
            result = [v for v in gv.vehicle_list if bool(getattr(v, 'sold', False))]
        elif reserved and sold:
            result = [v for v in gv.vehicle_list if (not v.is_available)]
        elif available and not reserved and not sold:
            result = [v for v in gv.vehicle_list if v.is_available and (not bool(getattr(v, "sold", False)))]
        else:
            result = list(gv.vehicle_list)
        self.fill_vehicle_listbox(result)















