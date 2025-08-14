import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from Src.Controllers.VehicleController import VehicleController
import Src.GlobalVariables.GlobalVariables as gv
from Src.GlobalVariables.GlobalVariables import vehicle_list
from Src.Class.Vehicle import Vehicle, FuelType
import os
from tkinter import PhotoImage
import customtkinter as ctk
from PIL import Image


class CreateVehicle(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")
        self.vc = gv.vehicle_controller
        self.controller = controller
        self.current_fuel_type = None

        base_path = os.path.dirname(__file__)
        icon_dir = os.path.join(base_path, "..", "Images", "Icone")
        logout_icon = PhotoImage(file=os.path.join(icon_dir, "Logout.png"))

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
                                 command=lambda: (self.controller.mostra_frame("VehicleSection"),
                                                 self.controller.frames["VehicleSection"].refresh_brand_checkboxes(),
                                                 self.controller.frames["VehicleSection"].refresh_model_checkboxes()))
        back_btn.pack(side="left", padx=(20, 0))

        title_frame = tk.Frame(self, bg="#cfd7dc", height=40)
        title_frame.pack(side="top", fill="x")
        title_frame.pack_propagate(False)

        label_title = tk.Label(title_frame,
                               text="Compila Nuova Scheda Veicolo",
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

        content_frame = tk.Frame(self, bg="#cfd7dc")
        content_frame.pack(anchor="center", pady=20, padx=20)

        CB_frame = tk.Frame(content_frame, bg="#000534", width=270, height=270)
        CB_frame.pack(side="left", anchor="n", padx=(100, 30), pady=(20, 50))
        CB_frame.pack_propagate(False)


        self.brand_listBox = ctk.CTkComboBox(
            CB_frame,
            font=("Calisto MT", 15),
            width=200,
            corner_radius=10,
            fg_color="white",
            text_color="#000534",
            border_color="#000534",
            border_width=2,
            dropdown_fg_color="white",
            dropdown_text_color="#000534",
            values=[],
            command=self.on_select_brand
        )
        #self.brand_listBox = ttk.Combobox(CB_frame, state="readonly")
        self.brand_listBox.grid(row=2, column=0, sticky=tk.NSEW)


        #self.model_listBox = ttk.Combobox(CB_frame, state="readonly")
        self.model_listBox = ctk.CTkComboBox(
            CB_frame,
            font=("Calisto MT", 15),
            width=200,
            corner_radius=10,
            fg_color="white",
            text_color="#000534",
            border_color="#000534",
            border_width=2,
            dropdown_fg_color="white",
            dropdown_text_color="#000534",
            values=[],
            command = self.on_selected_model
        )
        self.model_listBox.grid(row=2, column=1, sticky=tk.NSEW)
        self.model_listBox.set("")



        '''        
        self.brand_listBox = ttk.Combobox(CB_frame, state="readonly")
        self.brand_listBox.grid(row=2, column=0, sticky=tk.NSEW)


        self.model_listBox = ttk.Combobox(CB_frame, state="readonly")
        self.model_listBox.grid(row=2, column=1, sticky=tk.NSEW)
        
        #Campi di fill per creazione veicolo
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
        '''

        info_frame = tk.Frame(content_frame, bg="#cfd7dc")
        info_frame.pack(side="left", fill="both", expand=True)
        info_frame.pack_propagate(False)

        BrandLabel = tk.Label(info_frame, text="Brand", font=("Calisto MT", 15, "bold"),
                              bg="#cfd7dc", fg="#000534")
        BrandLabel.grid(row=0, column=0, padx=(70, 50), pady=(30, 0))
        self.Brand = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                  corner_radius=10, fg_color="white", text_color="#000534",
                                  border_color="#000534", border_width=2)
        self.Brand.grid(row=1, column=0, padx=(70, 50), pady=5)

        ModelLabel = tk.Label(info_frame, text="Modello", font=("Calisto MT", 15, "bold"),
                              bg="#cfd7dc", fg="#000534")
        ModelLabel.grid(row=0, column=1, padx=(70, 50), pady=(30, 0))
        self.Model = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                  corner_radius=10, fg_color="white", text_color="#000534",
                                  border_color="#000534", border_width=2)
        self.Model.grid(row=1, column=1, padx=(70, 50), pady=5)

        DisplacementLabel = tk.Label(info_frame, text="Cilindrata", font=("Calisto MT", 15, "bold"),
                                     bg="#cfd7dc", fg="#000534")
        DisplacementLabel.grid(row=2, column=0, padx=(70, 50), pady=(30, 0))
        self.Displacement = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                         corner_radius=10, fg_color="white", text_color="#000534",
                                         border_color="#000534", border_width=2)
        self.Displacement.grid(row=3, column=0, padx=(70, 50), pady=5)

        HP_Label = tk.Label(info_frame, text="Cavalli", font=("Calisto MT", 15, "bold"),
                            bg="#cfd7dc", fg="#000534")
        HP_Label.grid(row=2, column=1, padx=(70, 50), pady=(30, 0))
        self.HP = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                               corner_radius=10, fg_color="white", text_color="#000534",
                               border_color="#000534", border_width=2)
        self.HP.grid(row=3, column=1, padx=(70, 50), pady=5)

        plateLabel = tk.Label(info_frame, text="Targa", font=("Calisto MT", 15, "bold"),
                              bg="#cfd7dc", fg="#000534")
        plateLabel.grid(row=4, column=0, padx=(70, 50), pady=(30, 0))
        self.NumberPlate = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                         corner_radius=10, fg_color="white", text_color="#000534",
                                         border_color="#000534", border_width=2)
        self.NumberPlate.grid(row=5, column=0, padx=(70, 50), pady=5)

        YearLabel = tk.Label(info_frame, text="Anno Registrazione", font=("Calisto MT", 15, "bold"),
                             bg="#cfd7dc", fg="#000534")
        YearLabel.grid(row=4, column=1, padx=(70, 50), pady=(30, 0))
        self.Year = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                 corner_radius=10, fg_color="white", text_color="#000534",
                                 border_color="#000534", border_width=2)
        self.Year.grid(row=5, column=1, padx=(70, 50), pady=5)

        fueltypeLabel = tk.Label(info_frame, text="Tipo Carburante", font=("Calisto MT", 15, "bold"),
                                 bg="#cfd7dc", fg="#000534")
        fueltypeLabel.grid(row=6, column=0, padx=(70, 50), pady=(30, 0))
        fuel_names = [fuel.name for fuel in FuelType]
        #self.fuelTypeComboBox = ttk.Combobox(info_frame, values=fuel_names, state="disabled")
        self.fuelTypeComboBox = ctk.CTkComboBox(
            info_frame,
            values=fuel_names,
            state="disabled",
            font=("Calisto MT", 15),
            width=200,
            corner_radius=10,
            fg_color="white",
            text_color="#000534",
            border_color="#000534",
            border_width=2,
            dropdown_fg_color="white",
            dropdown_text_color="#000534",
            command = self.on_selected_fuel
        )
        self.fuelTypeComboBox.grid(row=7, column=0, padx=(70, 50), pady=5)
        self.fuelTypeComboBox.set("")


        KM_Label = tk.Label(info_frame, text="Km", font=("Calisto MT", 15, "bold"),
                            bg="#cfd7dc", fg="#000534")
        KM_Label.grid(row=6, column=1, padx=(70, 50), pady=(30, 0))
        self.Kilometers = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                       corner_radius=10, fg_color="white", text_color="#000534",
                                       border_color="#000534", border_width=2)
        self.Kilometers.grid(row=7, column=1, padx=(70, 50), pady=5)

        ColorLabel = tk.Label(info_frame, text="Colore", font=("Calisto MT", 15, "bold"),
                              bg="#cfd7dc", fg="#000534")
        ColorLabel.grid(row=8, column=0, padx=(70, 50), pady=(30, 0))
        self.Color = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                  corner_radius=10, fg_color="white", text_color="#000534",
                                  border_color="#000534", border_width=2)
        self.Color.grid(row=9, column=0, padx=(70, 50), pady=5)

        ID_Label = tk.Label(info_frame, text="ID", font=("Calisto MT", 15, "bold"),
                            bg="#cfd7dc", fg="#000534")
        ID_Label.grid(row=8, column=1, padx=(70, 50), pady=(30, 0))
        self.Vehicle_ID = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                       corner_radius=10, fg_color="white", text_color="#000534",
                                       border_color="#000534", border_width=2)
        self.Vehicle_ID.grid(row=9, column=1, padx=(70, 50), pady=5)

        price_Label = tk.Label(info_frame, text="Prezzo", font=("Calisto MT", 15, "bold"),
                               bg="#cfd7dc", fg="#000534")
        price_Label.grid(row=10, column=0, padx=(70, 50), pady=(30, 0))
        self.Price = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                  corner_radius=10, fg_color="white", text_color="#000534",
                                  border_color="#000534", border_width=2)
        self.Price.grid(row=11, column=0, padx=(70, 50), pady=5)

        self.isAvailableTick = tk.BooleanVar()
        self.isAvailableTickBox = ctk.CTkCheckBox(info_frame,
                                                  text="Disponibile",
                                                  font=("Calisto MT", 18, "bold"),
                                                  width=150, corner_radius=10,
                                                  fg_color="#000534", border_color="#000534",
                                                  border_width=2, text_color="#000534",
                                                  variable=self.isAvailableTick)
        self.isAvailableTickBox.grid(row=10, column=1, columnspan=2, padx=(70, 50), pady=(30, 0))


        #tk.Button(self, text="Back", command=lambda: controller.mostra_frame("VehicleSection")).grid(row=3, column=0)
        tk.Button(CB_frame, text="Crea Brand", command=lambda: (self.vc.create_brand(), self.fill_brand_listbox())).grid(row=3, column=1, padx=10)
        tk.Button(CB_frame, text="Crea Model", command=lambda: self.check_brand_selected()).grid(row=3, column=2, padx=10)
        tk.Button(CB_frame, text="Salva", command = lambda: self.save_vehicle()).grid(row=20, column=3, padx=10)

        ##aggiorniamo le tabelle
        self.fill_brand_listbox()

        #bindings
        self.brand_listBox.bind("<<ComboboxSelected>>", self.on_select_brand)
        self.model_listBox.bind("<<ComboboxSelected>>", self.on_selected_model)
        self.fuelTypeComboBox.bind("<<ComboboxSelected>>", self.on_selected_fuel)



    # Filling comboboxes
    def fill_brand_listbox(self):
        try:
            brands = list(gv.brand_list)
        except Exception:
            brands = []
        self.brand_listBox.configure (values = brands)
        self.brand_listBox.set("")

    def fill_model_listbox(self):
        self.tmp_model_list = []
        values = []
        for model in gv.model_list:
            if model.brand == gv.CurrentBrand:
                self.tmp_model_list.append(model)
                values.append(f"{model.model_id}  {model.name}")
        self.model_listBox.configure (values = values)
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
        self.fuelTypeComboBox.configure(state="readonly")

    def save_vehicle(self):
        self.vc.create_vehicle(
            self.Vehicle_ID.get(),
            gv.CurrentModel,
            self.Year.get(),
            self.Color.get(),
            self.current_fuel_type,
            self.isAvailableTick.get(),
            self.Kilometers.get(),
            self.NumberPlate.get(),
            self.Price.get()
        )
        messagebox.showinfo("Successo", "Veicolo creato correttamente!")
        self.clear_fields()
        self.controller.frames["VehicleSection"].fill_vehicle_listbox(gv.vehicle_list)

    def clear_fields(self):
        #sblocco i campi
        self.brand_listBox.set("")
        self.model_listBox.set("")

        self.Vehicle_ID.configure(state="normal")
        self.Model.configure(state="normal")
        self.Brand.configure(state="normal")
        self.Kilometers.configure(state="normal")
        self.Year.configure(state="normal")
        self.Color.configure(state="normal")
        self.NumberPlate.configure(state="normal")
        self.Price.configure(state="normal")
        self.Displacement.configure(state="normal")
        self.HP.configure(state="normal")
        self.isAvailableTickBox.configure(state="normal")

        #svuoto i campi
        self.Vehicle_ID.delete(0, tk.END)
        self.Brand.delete(0, tk.END)
        self.Model.delete(0, tk.END)
        self.Year.delete(0, tk.END)
        self.Color.delete(0, tk.END)
        self.Kilometers.delete(0, tk.END)
        self.NumberPlate.delete(0, tk.END)
        self.Price.delete(0, tk.END)
        self.Displacement.delete(0, tk.END)
        self.HP.delete(0, tk.END)
        self.isAvailableTick.set(False)
        self.fuelTypeComboBox.set("")

        #riblocco i campi
        self.Vehicle_ID.configure(state="readonly")
        self.Model.configure(state="readonly")
        self.Brand.configure(state="readonly")
        self.Kilometers.configure(state="readonly")
        self.Year.configure(state="readonly")
        self.Color.configure(state="readonly")
        self.NumberPlate.configure(state="readonly")
        self.Price.configure(state="readonly")
        self.HP.configure(state="readonly")
        self.Displacement.configure(state="readonly")
        self.isAvailableTickBox.configure(state="disabled")
        self.fuelTypeComboBox.configure(state="disabled")




    def check_brand_selected(self):
        if not gv.CurrentBrand:
            messagebox.showwarning("Errorino", "Non hai selezionato alcun brand!")
            return
        self.controller.frames["CreateModel"].loadModel()
        self.controller.mostra_frame("CreateModel")
        for model in gv.model_list:
            print(model.brand, model.name)


    # eventi On_pressed
    def on_select_brand(self, event=None):
        # Get selected brand from combobox
        value = self.brand_listBox.get()
        if value:
            gv.CurrentBrand = value
            self.fill_model_listbox()
            print(f"Brand selezionato: {value}")

    def on_selected_model(self, event= None):
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
        value = self.fuelTypeComboBox.get()
        if value:
            self.current_fuel_type = value
            print(f"Fuel type selected: {value}")



