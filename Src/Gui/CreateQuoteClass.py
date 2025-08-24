import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv
import datetime as dt
from dateutil.relativedelta import relativedelta
import customtkinter as ctk
import os
from PIL import Image
costanteKW = 0.7355


class QuoteCreate(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")

        self.controller = controller
        self.qc = gv.quote_controller
        self.vc = gv.vehicle_controller
        self.cc = gv.client_controller

        base_path = os.path.dirname(__file__)
        icon_dir = os.path.join(base_path, "..", "Images", "Icone")
        logout_icon = ctk.CTkImage(light_image=Image.open(os.path.join(icon_dir, "Logout.png")), size=(30, 30))
        search_img = Image.open(os.path.join(icon_dir, "Ricerca.png"))

        self.search_icon = ctk.CTkImage(light_image=search_img, dark_image=search_img, size=(24, 24))

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
                               text="Crea Preventivo",
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
        info_frame.grid_columnconfigure(3, weight=1)

        ##Sinistra
        left_frame = tk.Frame(info_frame, bg="#cfd7dc")
        left_frame.grid(row=0, column=0, sticky="n", padx=20, pady=80)
        left_frame.grid_rowconfigure(2, weight=1)
        left_frame.grid_columnconfigure(0, weight=1)

        left_frame_label = tk.Label(left_frame, text="Seleziona un auto", font=("Calisto MT", 15, "bold"), bg="#cfd7dc", fg="#000534")
        left_frame_label.grid(row=0, column=0, padx=(10, 0), pady=(0, 10), sticky="ew")

        icon_holder = tk.Frame(left_frame, bg="#cfd7dc")
        icon_holder.grid(row=1, column=1, sticky="e", padx=(2, 5))
        icon_label = ctk.CTkLabel(icon_holder, image=self.search_icon, text="")
        icon_label.pack()

        self.VsearchBar = ctk.CTkEntry(left_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                    fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.VsearchBar.grid(row=1, column=0, sticky = "ew", pady=(0, 5),padx=(10,0))

        self.vehicleListBox = tk.Listbox(left_frame,
                                         font=("Calibri", 12),
                                         width=60,
                                         height=25,
                                         bg="#dee4e9"
                                         )
        self.vehicleListBox.grid(row=2, column=0, padx=(10,0), sticky = "nsew")

        scrollbar = tk.Scrollbar(left_frame,
                                 orient="vertical",
                                 command=self.vehicleListBox.yview)
        self.vehicleListBox.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row = 2, column = 1, sticky = "ns", padx=(0, 5))

        ##Colonna 2
        second_frame = tk.Frame(info_frame, bg="#cfd7dc")
        second_frame.grid(row=0, column=1, sticky="n", padx=(20, 0), pady=80)
        second_frame.grid_rowconfigure(2, weight=1)
        second_frame.grid_columnconfigure(0, weight=1)

        second_frame_label = tk.Label(second_frame, text="Seleziona un cliente", font=("Calisto MT", 15, "bold"), bg="#cfd7dc", fg="#000534")
        second_frame_label.grid(row=0, column=0, padx=(10, 0), pady=(0, 10), sticky="ew")

        icon_holder = tk.Frame(second_frame, bg="#cfd7dc")
        icon_holder.grid(row=1, column=1, sticky="e", padx=(2, 0))
        icon_label = ctk.CTkLabel(icon_holder, image=self.search_icon, text="")
        icon_label.pack()

        self.CsearchBar = ctk.CTkEntry(second_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                       fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.CsearchBar.grid(row=1, column=0, sticky="ew", pady=(0, 5), padx=(10,0))

        self.clientListBox = tk.Listbox(second_frame,
                                        font=("Calibri", 12),
                                         width=60,
                                         height=25,
                                         bg="#dee4e9")
        self.clientListBox.grid(row=2, column=0, padx=(10,0), sticky = "nsew")

        scrollbar = tk.Scrollbar(second_frame,
                                 orient="vertical",
                                 command=self.clientListBox.yview)
        self.clientListBox.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=2, column=1, padx=(0,5), sticky = "ns")

        ##Colonna 3
        third_frame = tk.Frame(info_frame, bg="#cfd7dc")
        third_frame.grid(row=0, column=2, sticky="n", padx=20, pady=80)

        self.clientLabel = tk.Label(third_frame, text="Cliente", font=("Calisto MT", 15, "bold"), bg="#cfd7dc",
                                     fg="#000534")
        self.clientLabel.grid(row = 0, column = 0, padx=(15, 90),pady=(15,0))
        self.clientInfo = ctk.CTkEntry(third_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                       fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.clientInfo.grid(row= 1, column= 0, padx=(15, 90), pady=(3,15))

        self.vehicleLabel = tk.Label(third_frame, text="Auto", font=("Calisto MT", 15, "bold"), bg="#cfd7dc",
                                     fg="#000534")
        self.vehicleLabel.grid(row = 2, column = 0, padx=(15, 90))
        self.vehicleInfo = ctk.CTkEntry(third_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                       fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.vehicleInfo.grid(row = 3, column = 0, padx=(15, 90), pady=(3,15))

        self.startDataLabel = tk.Label(third_frame, text="Data inizio", font=("Calisto MT", 15, "bold"), bg="#cfd7dc",
                                     fg="#000534")
        self.startDataLabel.grid(row = 4, column = 0, padx=(15, 90))
        self.startDate = ctk.CTkEntry(third_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                       fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.startDate.grid(row= 5, column = 0, padx=(15, 90), pady=(3,15))

        self.endDateLabel = tk.Label(third_frame, text="Data fine", font=("Calisto MT", 15, "bold"), bg="#cfd7dc",
                                     fg="#000534")
        self.endDateLabel.grid(row = 6, column = 0, padx=(15, 90))
        self.endDate = ctk.CTkEntry(third_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                       fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.endDate.grid(row = 7, column= 0, padx=(15, 90), pady=(3,15))

        ##colonna 4
        fourth_frame = tk.Frame(info_frame, bg="#cfd7dc")
        fourth_frame.grid(row=0, column=3, sticky="n", padx=20, pady=80)

        self.priceLabel = tk.Label(fourth_frame,text = "Prezzo", font=("Calisto MT", 15, "bold"), bg="#cfd7dc",
                                     fg="#000534")
        self.priceLabel.grid(row = 0, column = 0, padx=(15,90), pady=(15,0))
        self.price = ctk.CTkEntry(fourth_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                       fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.price.grid(row = 1, column = 0, padx=(15, 90), pady=(3,15))

        self.quoteID_Label = tk.Label(fourth_frame, text="ID", font=("Calisto MT", 15, "bold"), bg="#cfd7dc",
                                     fg="#000534")
        self.quoteID_Label.grid(row = 2, column = 0, padx=(15, 90))
        self.quoteID = ctk.CTkEntry(fourth_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                       fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.quoteID.grid(row = 3, column = 0, padx=(15, 90), pady=(3,15))

        self.userInfoLabel = tk.Label(fourth_frame, text="Utente", font=("Calisto MT", 15, "bold"), bg="#cfd7dc",
                                     fg="#000534")
        self.userInfoLabel.grid(row=4, column = 0, padx=(15,90))
        self.userInfo = ctk.CTkEntry(fourth_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                       fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.userInfo.grid(row = 5, column= 0, padx=(15, 90), pady=(3,15))

        create_btn = ctk.CTkButton(fourth_frame,
                                   text="Crea Preventivo",
                                   font=("Calisto MT", 18, "bold"),
                                   width=170,
                                   corner_radius=10,
                                   fg_color="white",
                                   border_color="#000534",
                                   border_width=2,
                                   text_color="#000534",
                                   command = lambda: self.create_quote())
        create_btn.grid(row=7, column=0, padx=(18, 90), pady=(30,15))

        self.vehicleListBox.bind("<<ListboxSelect>>", self.on_vehicle_selected)
        self.clientListBox.bind("<<ListboxSelect>>",self.on_client_selected)

        self.VsearchBar.bind("<KeyRelease>", lambda e: self.search_vehicle())
        self.CsearchBar.bind("<KeyRelease>", lambda e: self.search_client())

        self.fill_vehicle_list(gv.vehicle_list)
        self.fill_client_list(gv.client_list)
        self.fill_time_fields()
        self.fill_id()


    def fill_vehicle_list(self, vehicle_list):
        self.vehicleListBox.delete(0, tk.END)
        for vehicle in vehicle_list:
            self.vehicleListBox.insert(tk.END, f"{vehicle.vehicle_id} | {vehicle.model.brand} {vehicle.model.name} {vehicle.color} - {vehicle.number_plate}")
            
            
    def fill_client_list(self, client_list):
        self.clientListBox.delete(0,tk.END)
        for client in client_list:
            self.clientListBox.insert(tk.END, f"{client.ID} | {client.FirstName} {client.LastName} - {client.email}")


    def on_vehicle_selected(self, event = None):
        if event:
            widget = event.widget
            self.selected_vehicle = widget.curselection()
        else:
            self.selected_vehicle = self.vehicleListBox.curselection()

        if self.selected_vehicle:
            self.selected_vehicle = self.selected_vehicle[0]
            value = self.vehicleListBox.get(self.selected_vehicle)
            value = value.split()[0]
            local_vehicle = gv.vehicle_recovery(int(value))
            self.fill_vehicle_fields(local_vehicle)
            self.fill_price(local_vehicle)


    def on_client_selected(self, event = None):
        if event:
            widget = event.widget
            self.selected_client = widget.curselection()
        else:
            self.selected_client = self.clientListBox.curselection()

        if self.selected_client:
            self.selected_client = self.selected_client[0]
            value = self.clientListBox.get(self.selected_client)
            value = value.split()[0]
            self.fill_client_fields(gv.client_recovery(int(value)))

    def search_vehicle(self,event = None):
        self.vehicleListBox.delete(0, tk.END)
        tmp_list = self.vc.search_vehicle(self.VsearchBar.get())
        self.fill_vehicle_list(tmp_list)

    def search_client(self,event = None):
        self.clientListBox.delete(0, tk.END)
        tmp_list = self.cc.search_client_by_string(self.CsearchBar.get())
        self.fill_client_list(tmp_list)
        
    def fill_client_fields(self,client):
        self.clientInfo.configure(state= "normal")
        self.clientInfo.delete(0, tk.END)
        self.clientInfo.insert(0, f"{client.ID} - {client.FirstName} {client.LastName}")
        self.clientInfo.configure(state= "readonly")
        
    def fill_vehicle_fields(self, vehicle):
        self.vehicleInfo.configure(state= "normal")
        self.vehicleInfo.delete(0, tk.END)
        self.vehicleInfo.insert(0, f"{vehicle.vehicle_id} - {vehicle.model.brand} {vehicle.model.name} {vehicle.color} {vehicle.number_plate}")
        self.vehicleInfo.configure(state= "readonly")

    def fill_time_fields(self):
        self.startDate.configure(state= "normal")
        self.startDate.delete(0, tk.END)
        self.startDate.insert(0, dt.datetime.now().strftime("%d/%m/%Y"))
        self.startDate.configure(state= "readonly")
        self.endDate.configure(state= "normal")
        self.endDate.delete(0, tk.END)
        self.endDate.insert(0, (dt.datetime.now() + relativedelta(days=7)).strftime("%d/%m/%Y"))
        self.endDate.configure(state= "readonly")

    def fill_price(self, vehicle):
        '''
        È applicabile l’Iva al 4%, anziché al 22%, sull’acquisto di autovetture nuove o usate, aventi cilindrata fino a:

            2.000 centimetri cubici, se con motore a benzina o ibrido
            2.800 centimetri cubici, se con motore diesel o ibrido
            di potenza non superiore a 150 kW se con motore elettrico.
        '''

        if (vehicle.model.displacement <= 2000 and (vehicle.fuel_type == 6 or vehicle.fuel_type == 4) or
            vehicle.model.displacement <= 2800 and (vehicle.fuel_type == 6 or vehicle.fuel_type == 2) or
            vehicle.fuel_type == 6):
            base_price = vehicle.price + (vehicle.price * 0.04)

        else:
            base_price = vehicle.price + (vehicle.price * 0.22)

        kw = vehicle.model.hp * costanteKW
        priceToAdd = 151 + (kw - 53) * 3.51
        finalprice = round(priceToAdd + base_price,2)
        self.price.configure(state= "normal")
        self.price.delete(0, tk.END)
        self.price.insert(0, finalprice)
        self.price.configure(state= "readonly")

    def fill_id(self):
        if gv.quote_list:
            next_id = max(int(q.id) for q in gv.quote_list)+1

        else:
            next_id = 1

        self.quoteID.configure(state="normal")
        self.quoteID.delete(0, tk.END)
        self.quoteID.insert(0, str(next_id))
        self.quoteID.configure(state="readonly")

    def fill_user(self):
        self.userInfo.configure(state="normal")
        self.userInfo.delete(0, tk.END)
        self.userInfo.insert(0, f"{gv.CurrentUser.user_id} - {gv.CurrentUser.firstName} {gv.CurrentUser.LastName}")
        self.userInfo.configure(state="readonly")

    def create_quote(self):
        self.qc.create_quote(self.quoteID.get(),
                             self.clientInfo.get(),
                             self.vehicleInfo.get(),
                             self.startDate.get(),
                             self.endDate.get(),
                             self.price.get())
        self.fill_id()
        self.back_func()

    def back_func(self):
        if self.controller.frames["QuoteSection"].switch_btn_var.get():
            self.controller.frames["QuoteSection"].fill_quote_listbox_confirmed()
        else:
            self.controller.frames["QuoteSection"].fill_quote_listbox_not_confirmed()
        self.controller.mostra_frame("QuoteSection")



        
