import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

#Classe di gestione appuntamenti
class AppointmentSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.leftFrame = tk.Frame(self, bg="#dee4e9")
        self.leftFrame.pack(side="left", anchor="nw")

        self.rightFrame = tk.Frame(self, bg="#dee4e9")
        self.rightFrame.pack(side="right", anchor="ne")

        self.cal = Calendar(self.leftFrame, selectmode = "day", date_pattern = "dd/mm/yyyy")
        self.cal.grid(row=2, column=0, sticky="nswe")

        self.schedule = ttk.Treeview(self.rightFrame, columns= ("Ora", "Appuntamento"), show="tree")
        self.schedule.grid(row=1, column=0, sticky="nswe")
        self.schedule.heading("Ora")
        self.schedule.heading("Appuntamento")


        tk.Label(self.leftFrame, text="AppointmentSection").grid(row=1, column=1)
        tk.Button(self.rightFrame, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=0, column=0)

        self.fill_schedule()

    def fill_schedule(self):
        for i in range(8,20):
            first_half = f"{i:02d}:00"
            second_half = f"{i:02d}:30"
            self.schedule.insert("", "end", values=(first_half, ""))
            self.schedule.insert("", "end", values=(second_half, ""))

