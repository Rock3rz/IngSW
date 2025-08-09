import tkinter as tk
from tkinter import messagebox, simpledialog
from Src.Controllers.VehicleController import VehicleController
import Src.GlobalVariables.GlobalVariables as gv

class CreateVehicle(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.vc = VehicleController()
        self.controller = controller

        self.brand_listBox = tk.Listbox(self)
        self.brand_listBox.grid(row=2, column=0, sticky=tk.NSEW)

        self.model_listBox = tk.Listbox(self)
        self.model_listBox.grid(row=2, column=1, sticky=tk.NSEW)

        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("VehicleSection")).grid(row=3, column=0)
        tk.Button(self, text="Crea Brand", command=lambda: (self.vc.create_brand(), self.fill_brand_listbox())).grid(row=3, column=1, padx=10)
        tk.Button(self, text="Crea Model", command=lambda: self.check_brand_selected()).grid(row=3, column=2, padx=10)

        ##aggiorniamo le tabelle
        self.fill_brand_listbox()

        # bindings
        self.brand_listBox.bind("<<ListboxSelect>>", self.on_select_brand)

    # Filling listboxes
    def fill_brand_listbox(self):
        self.brand_listBox.delete(0, tk.END)

        for brand in gv.brand_list:
            self.brand_listBox.insert(tk.END, brand)

    # Conditional Checkers
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
        if event:
            widget = event.widget
            self.selected_brand = widget.curselection()
        else:
            self.selected_brand = self.brand_listBox.curselection()

        if self.selected_brand:
            self.selected_brand = self.selected_brand[0]
            value = self.brand_listBox.get(self.selected_brand)  # Testo della riga selezionata
            gv.CurrentBrand = value
            print(f"Indice selezionato: {self.selected_brand}, Valore: {value}")


