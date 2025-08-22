import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv
import customtkinter as ctk


#Classe di gestione preventivi
class QuoteSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.qc = gv.quote_controller
        self.controller = controller

        self.leftFrame = tk.Frame(self)
        self.leftFrame.pack(side = "left", anchor="nw")

        self.rightFrame = tk.Frame(self)
        self.rightFrame.pack(side = "right", anchor="ne", padx=(0, 100))

        self.quoteList = tk.Listbox(self.leftFrame)
        self.quoteList.grid(row = 1, column = 0)

        self.CreateButton = tk.Button(self.rightFrame, text = "Crea", command = lambda: (controller.mostra_frame("QuoteCreate"), controller.frames["QuoteCreate"].fill_user()))
        self.CreateButton.grid(row = 0, column = 0, padx = (15, 0), pady = 5)

        self.ViewButton = tk.Button(self.rightFrame, text = "Visualizza", command = lambda: self.view_func())
        self.ViewButton.grid(row = 0, column = 1, padx = (15, 0), pady = 5)

        self.switch_btn_var = tk.BooleanVar()
        self.switch_btn_var.set(False)
        self.ViewConfirmedButton = ctk.CTkSwitch(self.rightFrame, text = "Visualizza Confermati", variable = self.switch_btn_var, command = lambda: self.switch_list_quote_view())
        self.ViewConfirmedButton.grid(row = 1, column = 2, padx = (15, 0), pady = 5)

        tk.Label(self.leftFrame, text="QuoteSection").grid(row=0, column=0)
        tk.Button(self.rightFrame,text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row= 0, column= 2, padx=(15, 0))

        self.fill_quote_listbox_not_confirmed()

        self.quoteList.bind("<<ListboxSelect>>", self.on_quote_selected)

    def fill_quote_listbox_confirmed(self):
        self.quoteList.delete(0, tk.END)
        for quote in gv.quote_list:


            if quote.Confirmed:
                self.quoteList.insert(tk.END, f"{quote.id} {quote.Client.FirstName} {quote.Client.LastName} - {quote.Vehicle.model.brand} {quote.Vehicle.model.name}")

    def fill_quote_listbox_not_confirmed(self):
        self.quoteList.delete(0, tk.END)
        for quote in gv.quote_list:
            if not quote.Confirmed:
                self.quoteList.insert(tk.END,f"{quote.id} {quote.Client.FirstName} {quote.Client.LastName} - {quote.Vehicle.model.brand} {quote.Vehicle.model.name}")




    def on_quote_selected(self, event = None):
        if event:
            widget = event.widget
            self.selected_quote_index = widget.curselection()
        else:
            self.selected_quote_index = self.quoteList.curselection()

        if self.selected_quote_index:
            self.selected_quote_index = self.selected_quote_index[0]
            value = self.quoteList.get(self.selected_quote_index)
            gv.CurrentQuote = gv.quote_recovery(value.split()[0])
            #self.controller.frames["QuoteView"].fill_quote_info()

    def view_func(self):
        self.controller.frames["QuoteView"].fill_quote_info()
        if gv.CurrentQuote:
            self.controller.mostra_frame("QuoteView")


    def switch_list_quote_view(self):
        value = self.switch_btn_var.get()
        if value:
            self.fill_quote_listbox_confirmed()
        else:
            self.fill_quote_listbox_not_confirmed()
