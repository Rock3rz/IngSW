import tkinter as tk
from tkinter import ttk
import Src.GlobalVariables.GlobalVariables as gv


#Classe di gestione preventivi
class QuoteSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.qc = gv.quote_controller

        self.leftFrame = tk.Frame(self)
        self.leftFrame.pack(side = "left", anchor="nw")

        self.rightFrame = tk.Frame(self)
        self.rightFrame.pack(side = "right", anchor="ne", padx=(0, 100))

        self.quoteList = tk.Listbox(self.leftFrame)
        self.quoteList.grid(row = 1, column = 0)

        self.CreateButton = tk.Button(self.rightFrame, text = "Crea", command = lambda: controller.mostra_frame("QuoteCreate"))
        self.CreateButton.grid(row = 0, column = 0, padx = (15, 0), pady = 5)

        self.ViewButton = tk.Button(self.rightFrame, text = "Visualizza", command = lambda: controller.mostra_frame("QuoteView"))
        self.ViewButton.grid(row = 0, column = 1, padx = (15, 0), pady = 5)

        tk.Label(self.leftFrame, text="QuoteSection").grid(row=0, column=0)
        tk.Button(self.rightFrame,text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row= 0, column= 2, padx=(15, 0))