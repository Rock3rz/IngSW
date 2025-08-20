import tkinter as tk


class QuoteView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")


        
        back_btn = tk.Button(self, text="Back", command=lambda: controller.mostra_frame("QuoteSection")).grid(row = 0, column = 0)
        confirm_btn = tk.Button(self, text="Conferma").grid(row= 0, column= 1)
        delete_btn = tk.Button(self, text="Elimina").grid(row = 0, column= 2)