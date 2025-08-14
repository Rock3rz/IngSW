import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv
from Src.GlobalVariables.GlobalVariables import model_list, api_controller
from Src.Controllers.APIController import APIController
import os
import customtkinter as ctk
from tkinter import PhotoImage

class CreateModel(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")
        self.controller = controller
        self.vc = gv.vehicle_controller

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
                                 command=lambda: self.back_function()
                                 )
        back_btn.pack(side="left", padx=(20, 0))

        title_frame = tk.Frame(self, bg="#cfd7dc", height=40)
        title_frame.pack(side="top", fill="x")
        title_frame.pack_propagate(False)

        label_title = tk.Label(title_frame,
                               text="Crea Modello",
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

        info_frame = tk.Frame(self, bg="#cfd7dc", height=670, width=1000)
        info_frame.pack(anchor="center")
        info_frame.pack_propagate(False)


        data_label = tk.Label(info_frame,
                              text="Dati Nuovo Modello Auto",
                              font=("Calisto MT", 18, "bold"),
                              bg="#cfd7dc",
                              fg="#000534")
        data_label.pack(anchor="center")
        data_label.pack_propagate(False)

        border_frame = tk.Frame(info_frame, bg="#bfc9cf", height=2, width=940)
        border_frame.pack(anchor="center")
        border_frame.pack_propagate(False)

        final_border = tk.Frame(self, bg="#dee4e9", height=30)
        final_border.pack(side="top", fill="x")
        final_border.pack_propagate(False)

        form_section = tk.Frame(info_frame, bg="#cfd7dc")
        form_section.pack(fill="both", expand=True)


        form_section.grid_columnconfigure(2, minsize=100)

        Brand_Label = tk.Label(form_section,
                               text="Brand",
                               font=("Calisto MT", 15, "bold"),
                               bg="#cfd7dc",
                               fg="#000534"
                               )
        Brand_Label.grid(row=0, column=0, padx=(220, 50), pady=(50, 0))
        self.brand = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=240, corner_radius=10,
                                      fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.brand.grid(row=1, column=0, padx=(170, 5), pady=5)


        Name_Label = tk.Label(form_section,
                              text="Nome",
                              font = ("Calisto MT", 15, "bold"),
                              bg = "#cfd7dc",
                              fg = "#000534"
        )
        Name_Label.grid(row=0, column=3, padx=(70, 50), pady=(50, 0))
        self.name = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=240, corner_radius=10,
                                      fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.name.grid(row=1, column=3, padx=(70, 50), pady=5)


        displacement_Label = tk.Label(form_section,
                                      text="Cilindrata",
                                      font = ("Calisto MT", 15, "bold"),
                                      bg = "#cfd7dc",
                                      fg = "#000534")
        displacement_Label.grid(row=2, column=0, padx=(220, 50), pady=(50, 0))
        self.displacement = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=240, corner_radius=10,
                                      fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.displacement.grid(row=3, column=0, padx=(170, 5), pady=5)


        HP_Label = tk.Label(form_section,
                            text="Cavalli",
                            font=("Calisto MT", 15, "bold"),
                            bg="#cfd7dc",
                            fg="#000534"
                            )
        HP_Label.grid(row=2, column=3, padx=(70, 50), pady=(50, 0))
        self.hp = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=240, corner_radius=10,
                                      fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.hp.grid(row=3, column=3, padx=(70, 50), pady=5)


        IDLabel = tk.Label(form_section,
                           text="ID",
                           font=("Calisto MT", 15, "bold"),
                           bg="#cfd7dc",
                           fg="#000534"
                           )
        IDLabel.grid(row=4, column=0, padx=(220, 50), pady=(50, 0))
        self.model_ID = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=240, corner_radius=10,
                                      fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.model_ID.grid(row=5, column=0, padx=(170, 5), pady=5)


        save_btn = ctk.CTkButton(form_section, text="Salva",font=("Calisto MT", 16, "bold"),
                                 width=150, height=36,
                                 corner_radius=10,
                                 fg_color="white",
                                 border_color="#000534",
                                 border_width=2,
                                 text_color="#000534",command= lambda: self.saveModel())
        save_btn.grid(row=9, column=3, padx=(150, 10), pady=(70, 20))


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
        APIController.write_model_on_csv()
        self.controller.frames["CreateVehicle"].fill_model_listbox()
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



