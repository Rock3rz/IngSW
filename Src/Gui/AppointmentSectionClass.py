import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime, date, time
import Src.GlobalVariables.GlobalVariables as gv
from Src.GlobalVariables.GlobalVariables import appointment_list
from dateutil.relativedelta import relativedelta


#Classe di gestione appuntamenti
class AppointmentSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.ac = gv.appointment_controller

        self.leftFrame = tk.Frame(self, bg="#dee4e9")
        self.leftFrame.pack(side="left", anchor="nw")

        self.rightFrame = tk.Frame(self, bg="#dee4e9")
        self.rightFrame.pack(side="right", anchor="ne",padx=70)
        self.rightFrame.pack_propagate(False)

        self.buttonFrame = tk.Frame(self, bg="#dee4e9")
        self.buttonFrame.pack(side="top", anchor="center")
        self.buttonFrame.pack_propagate(False)

        self.cal = Calendar(self.leftFrame, selectmode = "day", date_pattern = "dd/mm/yyyy")
        self.cal.grid(row=2, column=0, sticky="nswe")

        self.schedule = ttk.Treeview(self.rightFrame, columns= ("Ora", "Appuntamento"), show="tree")
        self.schedule.grid(row=3, column=0, sticky="nswe")
        self.schedule.heading("Ora")
        self.schedule.heading("Appuntamento")


        tk.Label(self.leftFrame, text="AppointmentSection").grid(row=1, column=1)
        tk.Button(self.buttonFrame, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=0, column=0)
        self.create = tk.Button(self.buttonFrame, text="Create", command = lambda: self.create_event_func(self.description.get()))
        self.create.grid(row=1, column=0, pady=(10,0))

        tk.Label(self.buttonFrame, text="Descrizione").grid(row=2, column=0)
        self.description = (tk.Entry(self.buttonFrame, width=50))
        self.description.grid(row=3, column=0, pady=(10,0))

        self.fill_schedule()
        self.create_event_on_calendar()
        self.cal.bind("<<CalendarSelected>>", self.on_date_selected)
        self.schedule.bind("<<TreeviewSelect>>",self.on_hour_selected)

    def fill_schedule(self):
        for i in range(8,20):
            first_half = f"{i:02d}:00"
            second_half = f"{i:02d}:30"
            self.schedule.insert("", "end", values=(first_half, ""))
            self.schedule.insert("", "end", values=(second_half, ""))

    def on_date_selected(self, event):
        cal = event.widget
        selected_date = cal.get_date()
        gv.CurrentDate = datetime.strptime(selected_date, "%d/%m/%Y").date()
        self.create_event_on_timeTable(gv.CurrentDate)


    def on_hour_selected(self, event):
        tree = event.widget
        selected_item = tree.selection()
        for item in selected_item:
            values = tree.item(item, "values")
            gv.CurrentHour = datetime.strptime(values[0], "%H:%M").time()


    def validate_date(self):
        for appointment in gv.appointment_list:
            if appointment.date_time > appointment.date_time + relativedelta(months=1):
                gv.appointment_list.remove(appointment)

    def create_event_on_calendar(self):
        for app in gv.appointment_list:
            onlyDate = app.date_time.date()
            self.cal.calevent_create(onlyDate, "Appuntamento", "appointment")
            self.cal.tag_config("appointment", background="red", foreground="white")


    def create_event_on_timeTable(self, date):
        #Resetta tutte le righe della colonna "Appuntamento"
        for item in self.schedule.get_children():
            row_time = self.schedule.item(item, "values")[0]
            self.schedule.item(item, values=(row_time, ""))

        #Inserisci gli appuntamenti del giorno selezionato
        for app in gv.appointment_list:
            if app.date_time.date() == date:
                for item in self.schedule.get_children():
                    row_time_str = self.schedule.item(item, "values")[0]
                    row_time_obj = datetime.strptime(row_time_str, "%H:%M").time()

                    if row_time_obj == app.date_time.time():
                        self.schedule.item(item, values=(row_time_str, app.description))
                        break

    def create_event_func(self, description):
        self.create_event_on_calendar()
        self.ac.create_appointment(description)
        self.create_event_on_timeTable(gv.CurrentDate)








