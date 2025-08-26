import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv
from tkinter import messagebox
import os
from PIL import Image
import customtkinter as ctk


class QuoteView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")
        self.controller = controller
        self.qc = gv.quote_controller

        base_path = os.path.dirname(__file__)
        icon_dir = os.path.join(base_path, "..", "Images", "Icone")
        logout_icon = ctk.CTkImage(light_image=Image.open(os.path.join(icon_dir, "Logout.png")), size=(30, 30))

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
                                 command=lambda: self.back_func())
        back_btn.pack(side="left", padx=(20, 0))

        title_frame = tk.Frame(self, bg="#cfd7dc", height=40)
        title_frame.pack(side="top", fill="x")
        title_frame.pack_propagate(False)

        label_title = tk.Label(title_frame,
                               text="Preventivo",
                               font=("Calisto MT", 20, "bold"),
                               bg="#cfd7dc",
                               fg="#000534")
        label_title.pack(side="left", padx=(10, 0))

        header_border = tk.Frame(self, bg="#bfc9cf", height=2)
        header_border.pack(side="top", fill="x")

        btw_border = tk.Frame(self, bg="#dee4e9", height=30)
        btw_border.pack(side="top", fill="x")

        info_frame = tk.Frame(self, bg="#cfd7dc")
        info_frame.pack(fill="both", padx=50, pady=(20, 50), expand=True)
        info_frame.pack_propagate(False)


        info_frame.grid_rowconfigure(0, weight=1)
        info_frame.grid_columnconfigure(0, weight=1)
        info_frame.grid_columnconfigure(1, weight=1)
        info_frame.grid_columnconfigure(2, weight=1)

        ##Sinistra
        left_frame = tk.Frame(info_frame, bg="#cfd7dc")
        left_frame.grid(row=0, column=0, sticky="n", padx=20, pady=80)

        self.clientLabel = tk.Label(left_frame, text="Cliente", font=("Calisto MT", 15, "bold"), bg="#cfd7dc", fg="#000534")
        self.clientLabel.grid(row=0, column=0, pady=(0,5))
        self.clientInfo = ctk.CTkEntry(left_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                       fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.clientInfo.grid(row=1, column=0, pady=(0,20))

        self.clientPhoneLabel = tk.Label(left_frame, text="Numero di Telefono", font=("Calisto MT", 12), bg="#cfd7dc", fg="#000534")
        self.clientPhoneLabel.grid(row=2, column=0, pady=(0,5))
        self.clientPhoneInfo = ctk.CTkEntry(left_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                       fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.clientPhoneInfo.grid(row=3, column=0, pady=(0,20))

        self.clientEmailLabel = tk.Label(left_frame, text="Email", font=("Calisto MT", 12), bg="#cfd7dc", fg="#000534")
        self.clientEmailLabel.grid(row=4, column=0, pady=(0,5))
        self.clientEmailInfo = ctk.CTkEntry(left_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                       fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.clientEmailInfo.grid(row=5, column=0, pady=(0,20))

        self.priceLabel = tk.Label(left_frame, text="Prezzo (€)", font=("Calisto MT", 15, "bold"), bg="#cfd7dc", fg="#000534")
        self.priceLabel.grid(row=6, column=0, pady=(0,5))
        self.price = ctk.CTkEntry(left_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                  fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.price.grid(row=7, column=0, pady=(0,20))

        self.userInfoLabel = tk.Label(left_frame, text="Venditore di riferimento", font=("Calisto MT", 15, "bold"), bg="#cfd7dc", fg="#000534")
        self.userInfoLabel.grid(row=8, column=0, pady=(0,5))
        self.userInfo = ctk.CTkEntry(left_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                     fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.userInfo.grid(row=9, column=0, pady=(0,20))

        self.delete_btn = ctk.CTkButton(left_frame, text="Elimina Preventivo", font=("Calisto MT", 15, "bold"),
                                        width=200, corner_radius=10, fg_color="white", border_color="#000534",
                                        border_width=2, text_color="#000534", command=lambda: self.delete_func())
        self.delete_btn.grid(row=10, column=0, pady=(10,0))

        ##Centro
        vehicle_frame = tk.Frame(info_frame, bg="#cfd7dc")
        vehicle_frame.grid(row=0, column=1, sticky="n", padx=20, pady=80)

        self.vehicleLabel = tk.Label(vehicle_frame, text="Auto", font=("Calisto MT", 15, "bold"), bg="#cfd7dc", fg="#000534")
        self.vehicleLabel.grid(row=0, column=0, pady=(0,5))
        self.vehicleInfo = ctk.CTkEntry(vehicle_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                        fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.vehicleInfo.grid(row=1, column=0, pady=(0,10))

        self.targa = tk.Label(vehicle_frame, text="Targa", font=("Calisto MT", 12), bg="#cfd7dc", fg="#000534")
        self.targa.grid(row=2, column=0, pady=(0,5))
        self.vehicle_plate_info = ctk.CTkEntry(vehicle_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                               fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.vehicle_plate_info.grid(row=3, column=0, pady=(0,10))

        self.alim = tk.Label(vehicle_frame, text="Alimentazione", font=("Calisto MT", 12), bg="#cfd7dc", fg="#000534")
        self.alim.grid(row=4, column=0, pady=(0,5))
        self.vehicle_alim_info = ctk.CTkEntry(vehicle_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                              fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.vehicle_alim_info.grid(row=5, column=0, pady=(0,10))

        self.priceIn = tk.Label(vehicle_frame, text="Prezzo Iniziale (€)", font=("Calisto MT", 12), bg="#cfd7dc", fg="#000534")
        self.priceIn.grid(row=6, column=0, pady=(0,5))
        self.vehicle_price_info = ctk.CTkEntry(vehicle_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                               fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.vehicle_price_info.grid(row=7, column=0, pady=(0,10))

        self.km = tk.Label(vehicle_frame, text="Km", font=("Calisto MT", 12), bg="#cfd7dc", fg="#000534")
        self.km.grid(row=8, column=0, pady=(0,5))
        self.vehicle_km_info = ctk.CTkEntry(vehicle_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                            fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.vehicle_km_info.grid(row=9, column=0, pady=(0,10))

        ##Destra
        right_frame = tk.Frame(info_frame, bg="#cfd7dc")
        right_frame.grid(row=0, column=2, sticky="n", padx=20, pady=80)

        self.quoteID_Label = tk.Label(right_frame, text="ID", font=("Calisto MT", 15, "bold"), bg="#cfd7dc", fg="#000534")
        self.quoteID_Label.grid(row=0, column=0, padx=5, pady=(0,5))
        self.startDataLabel = tk.Label(right_frame, text="Data inizio", font=("Calisto MT", 15, "bold"), bg="#cfd7dc", fg="#000534")
        self.startDataLabel.grid(row=0, column=1, padx=5, pady=(0,5))
        self.endDateLabel = tk.Label(right_frame, text="Data fine", font=("Calisto MT", 15, "bold"), bg="#cfd7dc",
                                     fg="#000534")
        self.endDateLabel.grid(row=0, column=2, padx=5, pady=(0, 5))

        self.quoteID = ctk.CTkEntry(right_frame, font=("Calisto MT", 15), width=50, corner_radius=10,
                                    fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.quoteID.grid(row=1, column=0, padx=5, pady=(0, 10))
        self.startDate = ctk.CTkEntry(right_frame, font=("Calisto MT", 15), width=100, corner_radius=10,
                                      fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.startDate.grid(row=1, column=1, padx=5, pady=(0, 10))
        self.endDate = ctk.CTkEntry(right_frame, font=("Calisto MT", 15), width=100, corner_radius=10,
                                    fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.endDate.grid(row=1, column=2, padx=5, pady=(0, 10))

        self.confirmed_var = tk.BooleanVar()
        self.confirmed_tick = ctk.CTkCheckBox(right_frame, text="Confermato", font=("Calisto MT", 15, "bold"),
                                              width=150, corner_radius=10, fg_color="#000534", border_color="#000534",
                                              border_width=2, text_color="#000534", variable=self.confirmed_var)
        self.confirmed_tick.grid(row=2, column=0, columnspan=2, pady=(170, 10), sticky="w")

        self.confirm_btn = ctk.CTkButton(right_frame, text="Conferma Vendita", font=("Calisto MT", 14, "bold"),
                                         width=150, corner_radius=10, fg_color="white", border_color="#000534",
                                         border_width=2, text_color="#000534", command=lambda: self.confirm_func())
        self.confirm_btn.grid(row=2, column=2, pady=(170, 10), sticky="e")

    def fill_quote_info(self):
        if gv.CurrentQuote is  None:
            messagebox.showwarning("Errore", "Selezionare un preventivo per visualizzarlo")
            return

        #disabilita lo stato del tasto se confermato
        if gv.CurrentQuote.Confirmed:
            self.disable_confirm_btn(False)
        else:
            self.disable_confirm_btn(True)

        self.clientInfo.configure(state= "normal")
        self.clientInfo.delete(0, tk.END)
        self.clientInfo.insert(0, f"{gv.CurrentQuote.Client.FirstName} {gv.CurrentQuote.Client.LastName}")
        self.clientInfo.configure(state= "readonly")

        self.clientPhoneInfo.configure(state= "normal")
        self.clientPhoneInfo.delete(0, tk.END)
        self.clientPhoneInfo.insert(0, f"{gv.CurrentQuote.Client.PhoneNumber}")
        self.clientPhoneInfo.configure(state= "readonly")

        self.clientEmailInfo.configure(state= "normal")
        self.clientEmailInfo.delete(0, tk.END)
        self.clientEmailInfo.insert(0, f"{gv.CurrentQuote.Client.email}")
        self.clientEmailInfo.configure(state= "readonly")

        self.vehicleInfo.configure(state= "normal")
        self.vehicleInfo.delete(0, tk.END)
        self.vehicleInfo.insert(0, f"{gv.CurrentQuote.Vehicle.model.brand} {gv.CurrentQuote.Vehicle.model.name} {gv.CurrentQuote.Vehicle.color}")
        self.vehicleInfo.configure(state= "readonly")

        self.vehicle_plate_info.configure(state= "normal")
        self.vehicle_plate_info.delete(0, tk.END)
        self.vehicle_plate_info.insert(0, f"{gv.CurrentQuote.Vehicle.number_plate}")
        self.vehicle_plate_info.configure(state= "readonly")

        self.vehicle_alim_info.configure(state= "normal")
        self.vehicle_alim_info.delete(0, tk.END)
        self.vehicle_alim_info.insert(0, f"{gv.CurrentQuote.Vehicle.fuel_type}")
        self.vehicle_alim_info.configure(state= "readonly")

        self.vehicle_price_info.configure(state= "normal")
        self.vehicle_price_info.delete(0, tk.END)
        self.vehicle_price_info.insert(0, f"{gv.CurrentQuote.Vehicle.price}")
        self.vehicle_price_info.configure(state= "readonly")

        self.vehicle_km_info.configure(state= "normal")
        self.vehicle_km_info.delete(0, tk.END)
        self.vehicle_km_info.insert(0, f"{gv.CurrentQuote.Vehicle.km}")
        self.vehicle_km_info.configure(state= "readonly")

        self.startDate.configure(state= "normal")
        self.startDate.delete(0, tk.END)
        self.startDate.insert(0, gv.CurrentQuote.StartDate.strftime("%d/%m/%Y"))
        self.startDate.configure(state= "readonly")

        self.endDate.configure(state= "normal")
        self.endDate.delete(0, tk.END)
        self.endDate.insert(0, gv.CurrentQuote.EndDate.strftime("%d/%m/%Y"))
        self.endDate.configure(state= "readonly")

        self.price.configure(state= "normal")
        self.price.delete(0, tk.END)
        self.price.insert(0, gv.CurrentQuote.Price)
        self.price.configure(state= "readonly")

        self.quoteID.configure(state= "normal")
        self.quoteID.delete(0, tk.END)
        self.quoteID.insert(0, gv.CurrentQuote.id)
        self.quoteID.configure(state= "readonly")

        self.userInfo.configure(state= "normal")
        self.userInfo.delete(0, tk.END)
        self.userInfo.insert(0, f"{gv.CurrentQuote.User.user_id} | {gv.CurrentQuote.User.firstName} {gv.CurrentQuote.User.LastName}")
        self.userInfo.configure(state= "readonly")

        self.confirmed_tick.configure(state= "normal")
        self.confirmed_var.set(gv.CurrentQuote.Confirmed)
        self.confirmed_tick.configure(state= "disabled")

    def set_CurrentQuote_None(self):
        gv.CurrentQuote = None
        self.controller.frames["QuoteSection"].quoteList.selection_clear(0, tk.END)

    def back_func(self):
        self.controller.mostra_frame("QuoteSection")
        self.set_CurrentQuote_None()
        self.disable_confirm_btn(True)

    def delete_func(self):
                self.qc.delete_quote()
                self.controller.frames["QuoteSection"].fill_quote_listbox_not_confirmed()
                self.back_func()

    def confirm_func(self):
        self.qc.confirm_quote()
        self.confirmed_var.set(True)
        if self.controller.frames["QuoteSection"].switch_btn_var.get():
            self.controller.frames["QuoteSection"].fill_quote_listbox_confirmed()

        else:
            self.controller.frames["QuoteSection"].fill_quote_listbox_not_confirmed()
        self.controller.frames["VehicleSection"].fill_vehicle_listbox(gv.vehicle_list)
        self.confirmed_tick.configure(state="normal")

        self.confirmed_tick.configure(state="disabled")

    def disable_confirm_btn(self, value: bool):
        if value:
            self.confirm_btn.configure(state="normal")
        else:
            self.confirm_btn.configure(state="disabled")



