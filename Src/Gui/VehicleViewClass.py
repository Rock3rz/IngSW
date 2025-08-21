import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv
import os
import customtkinter as ctk
from PIL import Image

class VehicleView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")

        base_path = os.path.dirname(__file__)
        icon_dir = os.path.join(base_path, "..", "Images", "Icone")
        logout_icon = ctk.CTkImage(light_image=Image.open(os.path.join(icon_dir, "Logout.png")), size=(30, 30))

        no_image_dir = os.path.join(base_path, "..", "Images", "Cars")

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
                                 command=lambda: controller.mostra_frame("VehicleSection"))
        back_btn.pack(side="left", padx=(20, 0))

        title_frame = tk.Frame(self, bg="#cfd7dc", height=40)
        title_frame.pack(side="top", fill="x")
        title_frame.pack_propagate(False)

        label_title = tk.Label(title_frame,
                               text="Scheda Veicolo",
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

        self.isAvailableVar = tk.BooleanVar()

        content_frame = tk.Frame(self, bg="#cfd7dc")
        content_frame.pack(anchor="center", pady=20, padx=20)

        image_frame = tk.Frame(content_frame, bg="#000534", width=270, height=270)
        image_frame.pack(side="left", anchor="n", padx=(100, 30), pady=(20, 50))
        image_frame.pack_propagate(False)

        self.cars_image_dir = os.path.join(base_path, "..", "Images", "Cars")
        self.no_image_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(self.cars_image_dir, "NoImage.png")),
            size=(250, 250)
        )
        self.image_label = ctk.CTkLabel(image_frame, image=self.no_image_icon, text="")
        self.image_label.pack(padx=10, pady=10)
        self._current_ctk_image = self.no_image_icon


        info_frame = tk.Frame(content_frame, bg="#cfd7dc")
        info_frame.pack(side="left", fill="both", expand=True)
        info_frame.pack_propagate(False)

        BrandLabel = tk.Label(info_frame, text="Brand", font=("Calisto MT", 15, "bold"),
                              bg="#cfd7dc", fg="#000534")
        BrandLabel.grid(row=0, column=0, padx=(70, 50), pady=(30, 0))
        self.brand = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                  corner_radius=10, fg_color="white", text_color="#000534",
                                  border_color="#000534", border_width=2)
        self.brand.grid(row=1, column=0, padx=(70, 50), pady=5)

        ModelLabel = tk.Label(info_frame, text="Modello", font=("Calisto MT", 15, "bold"),
                              bg="#cfd7dc", fg="#000534")
        ModelLabel.grid(row=0, column=1, padx=(70, 50), pady=(30, 0))
        self.model = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                  corner_radius=10, fg_color="white", text_color="#000534",
                                  border_color="#000534", border_width=2)
        self.model.grid(row=1, column=1, padx=(70, 50), pady=5)

        DisplacementLabel = tk.Label(info_frame, text="Cilindrata", font=("Calisto MT", 15, "bold"),
                                     bg="#cfd7dc", fg="#000534")
        DisplacementLabel.grid(row=2, column=0, padx=(70, 50), pady=(30, 0))
        self.displacement = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                         corner_radius=10, fg_color="white", text_color="#000534",
                                         border_color="#000534", border_width=2)
        self.displacement.grid(row=3, column=0, padx=(70, 50), pady=5)

        HP_Label = tk.Label(info_frame, text="Cavalli", font=("Calisto MT", 15, "bold"),
                            bg="#cfd7dc", fg="#000534")
        HP_Label.grid(row=2, column=1, padx=(70, 50), pady=(30, 0))
        self.hp = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                               corner_radius=10, fg_color="white", text_color="#000534",
                               border_color="#000534", border_width=2)
        self.hp.grid(row=3, column=1, padx=(70, 50), pady=5)

        plateLabel = tk.Label(info_frame, text="Targa", font=("Calisto MT", 15, "bold"),
                              bg="#cfd7dc", fg="#000534")
        plateLabel.grid(row=4, column=0, padx=(70, 50), pady=(30, 0))
        self.number_plate = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                         corner_radius=10, fg_color="white", text_color="#000534",
                                         border_color="#000534", border_width=2)
        self.number_plate.grid(row=5, column=0, padx=(70, 50), pady=5)

        YearLabel = tk.Label(info_frame, text="Anno Registrazione", font=("Calisto MT", 15, "bold"),
                             bg="#cfd7dc", fg="#000534")
        YearLabel.grid(row=4, column=1, padx=(70, 50), pady=(30, 0))
        self.year = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                 corner_radius=10, fg_color="white", text_color="#000534",
                                 border_color="#000534", border_width=2)
        self.year.grid(row=5, column=1, padx=(70, 50), pady=5)

        fueltypeLabel = tk.Label(info_frame, text="Tipo Carburante", font=("Calisto MT", 15, "bold"),
                                 bg="#cfd7dc", fg="#000534")
        fueltypeLabel.grid(row=6, column=0, padx=(70, 50), pady=(30, 0))
        self.fuel_type = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                      corner_radius=10, fg_color="white", text_color="#000534",
                                      border_color="#000534", border_width=2)
        self.fuel_type.grid(row=7, column=0, padx=(70, 50), pady=5)

        KM_Label = tk.Label(info_frame, text="Km", font=("Calisto MT", 15, "bold"),
                            bg="#cfd7dc", fg="#000534")
        KM_Label.grid(row=6, column=1, padx=(70, 50), pady=(30, 0))
        self.kilometers = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                       corner_radius=10, fg_color="white", text_color="#000534",
                                       border_color="#000534", border_width=2)
        self.kilometers.grid(row=7, column=1, padx=(70, 50), pady=5)

        ColorLabel = tk.Label(info_frame, text="Colore", font=("Calisto MT", 15, "bold"),
                              bg="#cfd7dc", fg="#000534")
        ColorLabel.grid(row=8, column=0, padx=(70, 50), pady=(30, 0))
        self.color = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                  corner_radius=10, fg_color="white", text_color="#000534",
                                  border_color="#000534", border_width=2)
        self.color.grid(row=9, column=0, padx=(70, 50), pady=5)

        ID_Label = tk.Label(info_frame, text="ID", font=("Calisto MT", 15, "bold"),
                            bg="#cfd7dc", fg="#000534")
        ID_Label.grid(row=8, column=1, padx=(70, 50), pady=(30, 0))
        self.vehicle_id = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                       corner_radius=10, fg_color="white", text_color="#000534",
                                       border_color="#000534", border_width=2)
        self.vehicle_id.grid(row=9, column=1, padx=(70, 50), pady=5)

        price_Label = tk.Label(info_frame, text="Prezzo", font=("Calisto MT", 15, "bold"),
                               bg="#cfd7dc", fg="#000534")
        price_Label.grid(row=10, column=0, padx=(70, 50), pady=(30, 0))
        self.price = ctk.CTkEntry(info_frame, font=("Calisto MT", 15), width=200,
                                  corner_radius=10, fg_color="white", text_color="#000534",
                                  border_color="#000534", border_width=2)
        self.price.grid(row=11, column=0, padx=(70, 50), pady=5)

        self.isAvailableTickBox = ctk.CTkCheckBox(info_frame,
                                                  text="Disponibile",
                                                  font=("Calisto MT", 18, "bold"),
                                                  width=150, corner_radius=10,
                                                  fg_color="#000534", border_color="#000534",
                                                  border_width=2, text_color="#000534",
                                                  variable=self.isAvailableVar)
        self.isAvailableTickBox.grid(row=10, column=1, columnspan=2, padx=(70, 50), pady=(30,0))

        content_frame.pack(anchor="center", pady=20, padx=20)



    def load_model_infos(self):
        if gv.CurrentVehicle is not None:
            self.unlock_fields()
            self.clear_fields()
            # Update image
            img_path = gv.CurrentVehicle.image
            to_use = None
            if isinstance(img_path, str) and img_path.strip():
                candidate = img_path.strip()
                if not os.path.isabs(candidate):
                    # if relative, make it relative to project root
                    candidate = os.path.abspath(candidate)
                if os.path.exists(candidate):
                    to_use = candidate
            if to_use is None:
                to_use = os.path.join(self.cars_image_dir, "NoImage.png")
            try:
                self._current_ctk_image = ctk.CTkImage(light_image=Image.open(to_use), size=(250, 250))
                self.image_label.configure(image=self._current_ctk_image)
            except Exception:
                # fallback hard
                self.image_label.configure(image=self.no_image_icon)
                self._current_ctk_image = self.no_image_icon

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




