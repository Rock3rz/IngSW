import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv


class QuoteCreate(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")

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

        back_btn = tk.Button(self, text="Back", command=lambda: controller.mostra_frame("QuoteSection"))
        back_btn.grid(row=0, column=0)
        create_btn = tk.Button(self, text="Create")
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
            print(value)


    def on_client_selected(self, event = None):
        if event:
            widget = event.widget
            self.selected_client = widget.curselection()
        else:
            self.selected_client = self.clientListBox.curselection()

        if self.selected_client:
            self.selected_client = self.selected_client[0]
            value = self.clientListBox.get(self.selected_client)
            print(value)

    def search_vehicle(self,event = None):
        self.vehicleListBox.delete(0, tk.END)
        tmp_list = self.vc.search_vehicle(self.VsearchBar.get())
        self.fill_vehicle_list(tmp_list)

    def search_client(self,event = None):
        self.clientListBox.delete(0, tk.END)
        tmp_list = self.cc.search_client_by_string(self.CsearchBar.get())
        self.fill_client_list(tmp_list)
