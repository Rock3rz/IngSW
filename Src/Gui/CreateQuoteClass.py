import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv
import datetime as dt
from dateutil.relativedelta import relativedelta
costanteKW = 0.7355


class QuoteCreate(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")

        self.controller = controller
        self.qc = gv.quote_controller
        self.vc = gv.vehicle_controller
        self.cc = gv.client_controller

        self.VsearchBar = tk.Entry(self)
        self.VsearchBar.grid(row=1, column=1, padx=(15,90))

        self.vehicleListBox = tk.Listbox(self)
        self.vehicleListBox.grid(row=2, column=1, columnspan=2, padx=(15, 90))

        self.CsearchBar = tk.Entry(self)
        self.CsearchBar.grid(row=1, column=3)
        self.clientListBox = tk.Listbox(self)
        self.clientListBox.grid(row=2, column=3, columnspan=2)

        back_btn = tk.Button(self, text="Back", command=lambda: self.back_func())
        back_btn.grid(row=0, column=0)
        create_btn = tk.Button(self, text="Create", command = lambda: self.create_quote())
        create_btn.grid(row=0, column=1)

        #Campi Quote
        self.clientLabel = tk.Label(self, text="Cliente")
        self.clientLabel.grid(row = 0, column = 5, padx=(15, 90),pady=5)
        self.clientInfo = tk.Entry(self)
        self.clientInfo.grid(row= 1, column= 5, padx=(15, 90), pady=5)

        self.vehicleLabel = tk.Label(self, text="Auto")
        self.vehicleLabel.grid(row = 2, column = 5, padx=(15, 90))
        self.vehicleInfo = tk.Entry(self)
        self.vehicleInfo.grid(row = 3, column = 5, padx=(15, 90), pady=5)

        self.startDataLabel = tk.Label(self, text="Data inizio")
        self.startDataLabel.grid(row = 4, column = 5, padx=(15, 90))
        self.startDate = tk.Entry(self)
        self.startDate.grid(row= 5, column = 5, padx=(15, 90), pady=5)

        self.endDateLabel = tk.Label(self, text="Data fine")
        self.endDateLabel.grid(row = 6, column = 5, padx=(15, 90))
        self.endDate = tk.Entry(self)
        self.endDate.grid(row = 7, column= 5, padx=(15, 90), pady=5)

        self.priceLabel = tk.Label(self,text = "Prezzo")
        self.priceLabel.grid(row = 8, column = 5, padx=(15,90))
        self.price = tk.Entry(self)
        self.price.grid(row = 9, column = 5, padx=(15, 90), pady=5)

        self.quoteID_Label = tk.Label(self, text="ID")
        self.quoteID_Label.grid(row = 10, column = 5, padx=(15, 90))
        self.quoteID = tk.Entry(self)
        self.quoteID.grid(row = 11, column = 5, padx=(15, 90), pady=5)

        self.userInfoLabel = tk.Label(self, text="Utente")
        self.userInfoLabel.grid(row=12, column = 5, padx=(15,90))
        self.userInfo = tk.Entry(self)
        self.userInfo.grid(row = 13, column= 5, padx=(15, 90), pady=5)

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
            self.vehicleListBox.insert(tk.END, f"{vehicle.vehicle_id} {vehicle.model.brand} {vehicle.model.name} {vehicle.color} {vehicle.number_plate}")
            
            
    def fill_client_list(self, client_list):
        self.clientListBox.delete(0,tk.END)
        for client in client_list:
            self.clientListBox.insert(tk.END, f"{client.ID} {client.FirstName} {client.LastName} {client.email}")


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



        
