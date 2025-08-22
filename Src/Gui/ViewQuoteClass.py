import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv
from tkinter import messagebox

from Src.Controllers.APIController import APIController
from Src.Controllers.QuoteController import QuoteController


class QuoteView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")
        self.controller = controller
        self.qc = gv.quote_controller

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

        self.confirmed_var = tk.BooleanVar()
        self.confirmed_tick = tk.Checkbutton(self, text="Confermato", variable=self.confirmed_var)
        self.confirmed_tick.grid(row = 14, column = 5, sticky = tk.NSEW)
        self.confirmed_var.set(False)

        back_btn = (tk.Button(self, text="Back", command=lambda: self.back_func()))
        back_btn.grid(row = 0, column = 0)

        confirm_btn = tk.Button(self, text="Conferma", command = lambda: self.confirm_func()).grid(row= 0, column= 1)
        delete_btn = tk.Button(self, text="Elimina", command = lambda: self.delete_func()).grid(row = 0, column= 2)

    def fill_quote_info(self):
        if gv.CurrentQuote is  None:
            messagebox.showwarning("Errore", "Selezionare un preventivo per visualizzarlo")
            return

        self.clientInfo.configure(state= "normal")
        self.clientInfo.delete(0, tk.END)
        self.clientInfo.insert(0, f"{gv.CurrentQuote.Client.FirstName} {gv.CurrentQuote.Client.LastName}")
        self.clientInfo.configure(state= "readonly")

        self.vehicleInfo.configure(state= "normal")
        self.vehicleInfo.delete(0, tk.END)
        self.vehicleInfo.insert(0, f"{gv.CurrentQuote.Vehicle.model.brand} {gv.CurrentQuote.Vehicle.model.name} {gv.CurrentQuote.Vehicle.color} {gv.CurrentQuote.Vehicle.number_plate} {gv.CurrentQuote.Vehicle.price}")
        self.vehicleInfo.configure(state= "readonly")

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
        self.userInfo.insert(0, f"{gv.CurrentQuote.User.user_id} - {gv.CurrentQuote.User.firstName} {gv.CurrentQuote.User.LastName}")
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

    def delete_func(self):
                self.qc.delete_quote()
                self.controller.frames["QuoteSection"].fill_quote_listbox_confirmed()
                self.back_func()

    def confirm_func(self):
        self.qc.confirm_quote()
        self.controller.frames["QuoteSection"].fill_quote_listbox_confirmed()
        self.controller.frames["VehicleSection"].fill_vehicle_listbox(gv.vehicle_list)


