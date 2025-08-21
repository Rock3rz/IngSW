import tkinter as tk


class QuoteView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")

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

        back_btn = tk.Button(self, text="Back", command=lambda: controller.mostra_frame("QuoteSection")).grid(row = 0, column = 0)
        confirm_btn = tk.Button(self, text="Conferma").grid(row= 0, column= 1)
        delete_btn = tk.Button(self, text="Elimina").grid(row = 0, column= 2)

    #def fill_quote_info(self):