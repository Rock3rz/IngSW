import tkinter as tk

#Classe di gestione appuntamenti
class AppointmentSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="AppointmentSection").grid(row=1, column=1)
        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=2, column=1)