import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import Src.GlobalVariables.GlobalVariables as gv
from Src.Class.Vehicle import FuelType
import os
import customtkinter as ctk
from PIL import Image


class CreateVehicle(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")
        self.vc = gv.vehicle_controller
        self.controller = controller
        self.current_fuel_type = None
        self.selected_image_path = None

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

        CB_frame = tk.Frame(content_frame, bg="#cfd7dc", width=520, height=500)
        CB_frame.pack(side="left", anchor="n", padx=(100, 30), pady=(20, 50))
        CB_frame.pack_propagate(False)


        self.cars_image_dir = os.path.join(base_path, "..", "Images", "Cars")
        try:
            default_img_path = os.path.join(self.cars_image_dir, "NoImage.png")
            self.no_image_icon = ctk.CTkImage(light_image=Image.open(default_img_path), size=(250, 250))
        except Exception:
            self.no_image_icon = None
        image_holder = tk.Frame(CB_frame, bg="#000534", width=270, height=270)
        image_holder.grid(row=0, column=0, columnspan=3, padx=(10, 10), pady=(10, 5), sticky="n")
        image_holder.grid_propagate(False)
        self.image_label = ctk.CTkLabel(image_holder, image=self.no_image_icon, text="")
        self.image_label.pack(padx=10, pady=10)
        self._current_ctk_image = self.no_image_icon

        CB_frame.grid_columnconfigure(0, weight=0)
        CB_frame.grid_columnconfigure(1, weight=1, minsize=200)
        CB_frame.grid_columnconfigure(2, weight=0)
        CB_frame.grid_rowconfigure(0, weight=0, minsize=0)
        CB_frame.grid_rowconfigure(4, weight=0, minsize=0)


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
        self.Price.grid(row=11, column=0, padx=(70, 50), pady=(5, 20))

        self.isAvailableTick = tk.BooleanVar()
        self.isAvailableTickBox = ctk.CTkCheckBox(info_frame,
                                                  text="Disponibile",
                                                  font=("Calisto MT", 18, "bold"),
                                                  width=150, corner_radius=10,
                                                  fg_color="#000534", border_color="#000534",
                                                  border_width=2, text_color="#000534",
                                                  variable=self.isAvailableTick)
        self.isAvailableTickBox.grid(row=10, column=1, columnspan=2, padx=(70, 50), pady=(30, 0))

        create_brand_Label = tk.Label(CB_frame, text="Seleziona Brand", font=("Calisto MT", 15, "bold"),
                               bg="#cfd7dc", fg="#000534")
        create_brand_Label.grid(row=3, column=0, padx=(10, 10), pady=(10, 5), sticky="w")

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
        self.brand_listBox.grid(row=3, column=1, sticky="ew", padx=(10, 20), pady=(10, 5))

        create_brand_btn = ctk.CTkButton(CB_frame,
                                 text="Aggiungi Brand",
                                 font=("Calisto MT", 18),
                                 width=170,
                                 height=36,
                                 corner_radius=10,
                                 fg_color="white",
                                 border_color="#000534",
                                 border_width=2,
                                 text_color="#000534",
                                 command=lambda: (self.vc.create_brand(), self.fill_brand_listbox()))
        create_brand_btn.grid(row=3, column=2, padx=(10, 10), pady=(10, 5), sticky="w")


        create_model_Label = tk.Label(CB_frame, text="Seleziona Modello", font=("Calisto MT", 15, "bold"),
                               bg="#cfd7dc", fg="#000534")
        create_model_Label.grid(row=4, column=0, padx=(10, 10), pady=(10, 5), sticky="w")

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
        self.model_listBox.grid(row=4, column=1, sticky="ew", padx=(10, 20), pady=(10, 5))
        self.model_listBox.set("")

        create_model_btn = ctk.CTkButton(CB_frame,
                                 text="Aggiungi Modello",
                                 font=("Calisto MT", 18),
                                 width=170,
                                 height=36,
                                 corner_radius=10,
                                 fg_color="white",
                                 border_color="#000534",
                                 border_width=2,
                                 text_color="#000534",
                                 command=lambda: self.check_brand_selected())
        create_model_btn.grid(row=4, column=2, padx=(10, 10), pady=(10, 5), sticky="w")

        # Selettore immagine
        self.image_label_text = tk.StringVar(value="Nessuna immagine selezionata")
        select_img_btn = ctk.CTkButton(CB_frame,
                                 text="Seleziona Immagine",
                                 font=("Calisto MT", 16),
                                 width=170,
                                 height=36,
                                 corner_radius=10,
                                 fg_color="white",
                                 border_color="#000534",
                                 border_width=2,
                                 text_color="#000534",
                                 command=self.select_image)
        select_img_btn.grid(row=1, column=0, columnspan=3, padx=(10,10), pady=(5,5), sticky="n")
        selected_img_lbl = tk.Label(CB_frame, textvariable=self.image_label_text, font=("Calisto MT", 12), bg="#cfd7dc", fg="#000534")
        selected_img_lbl.grid(row=2, column=0, columnspan=3, padx=(10,10), pady=(0,10), sticky="n")

        save_btn = ctk.CTkButton(CB_frame,
                                 text="Salva",
                                 font=("Calisto MT", 18, "bold"),
                                 width=200,
                                 corner_radius=10,
                                 fg_color="white",
                                 border_color="#000534",
                                 border_width=2,
                                 text_color="#000534",
                                 command=lambda: self.save_vehicle())
        save_btn.grid(row=6, column=0, columnspan=3, sticky="s", pady=(20, 10))

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
            self.Price.get(),
            image=self.selected_image_path
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
        self.selected_image_path = None
        if hasattr(self, 'image_label_text') and self.image_label_text is not None:
            self.image_label_text.set("Nessuna immagine selezionata")
        # reset anteprima immagine
        if hasattr(self, 'image_label') and self.image_label is not None:
            self.image_label.configure(image=self.no_image_icon)
        self._current_ctk_image = self.no_image_icon




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

    def select_image(self):
        filetypes = [
            ("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp"),
            ("All files", "*.*")
        ]
        initial_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Images", "Cars"))
        try:
            os.makedirs(initial_dir, exist_ok=True)
        except Exception:
            pass
        path = filedialog.askopenfilename(title="Seleziona immagine veicolo", initialdir=initial_dir, filetypes=filetypes)
        if path:
            self.selected_image_path = path
            # show only filename for brevity
            try:
                filename = os.path.basename(path)
            except Exception:
                filename = path
            self.image_label_text.set(f"Selezionata: {filename}")
            # update preview
            try:
                self._current_ctk_image = ctk.CTkImage(light_image=Image.open(path), size=(250, 250))
                if hasattr(self, 'image_label') and self.image_label is not None:
                    self.image_label.configure(image=self._current_ctk_image)
            except Exception:
                # fallback
                self._current_ctk_image = self.no_image_icon
                if hasattr(self, 'image_label') and self.image_label is not None:
                    self.image_label.configure(image=self.no_image_icon)
        else:
            self.selected_image_path = None
            self.image_label_text.set("Nessuna immagine selezionata")
            # reset preview to default
            self._current_ctk_image = self.no_image_icon
            if hasattr(self, 'image_label') and self.image_label is not None:
                self.image_label.configure(image=self.no_image_icon)

    def clear_combo_boxes(self):
        self.brand_listBox.set("")
        self.model_listBox.set("")



