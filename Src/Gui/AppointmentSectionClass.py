import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime, date, time
import Src.GlobalVariables.GlobalVariables as gv
from Src.GlobalVariables.GlobalVariables import appointment_list
from dateutil.relativedelta import relativedelta
from tkinter import messagebox
import os
import customtkinter as ctk
from PIL import Image


#Classe di gestione appuntamenti
class AppointmentSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")
        self.ac = gv.appointment_controller

        base_path = os.path.dirname(__file__)
        icon_dir = os.path.join(base_path, "..", "Images", "Icone")
        logout_img = Image.open(os.path.join(icon_dir, "Logout.png"))

        logout_icon = ctk.CTkImage(light_image=logout_img, dark_image=logout_img, size=(30, 30))

        header_frame = tk.Frame(self, bg="#000534", height=50)
        header_frame.pack(side="top", fill="x")
        header_frame.pack_propagate(False)

        back_btn = ctk.CTkButton(header_frame,
                                 text="Back",
                                 font=("Calisto MT", 18, "bold"),
                                 image=logout_icon,
                                 compound="left",
                                 width=150,
                                 corner_radius=10,
                                 fg_color="white",
                                 border_color="#000534",
                                 border_width=2,
                                 text_color="#000534",
                                 command=lambda: controller.mostra_frame("MainMenu"))
        back_btn.pack(side="left", padx=(20, 0))

        title_frame = tk.Frame(self, bg="#cfd7dc", height=40)
        title_frame.pack(side="top", fill="x")
        title_frame.pack_propagate(False)

        label_title = tk.Label(title_frame,
                               text="Calendario Appuntamenti",
                               font=("Calisto MT", 20, "bold"),
                               bg="#cfd7dc",
                               fg="#000534")
        label_title.pack(side="left", padx=(10, 0))
        label_title.pack_propagate(False)

        header_border = tk.Frame(self, bg="#bfc9cf", height=2)
        header_border.pack(side="top", fill="x")
        header_border.pack_propagate(False)

        btw_border = tk.Frame(self, bg="#dee4e9", height=30)
        btw_border.pack(side="top", fill="x")
        btw_border.pack_propagate(False)

        main_frame = tk.Frame(self, bg="#dee4e9")
        main_frame.pack(side="top", fill="both", expand=True)

        self.leftFrame = tk.Frame(main_frame, bg="#dee4e9")
        self.leftFrame.pack(side="left", anchor="nw")

        self.rightFrame = tk.Frame(main_frame, bg="#dee4e9")
        self.rightFrame.pack(side="right", anchor="ne", padx=70)
        self.rightFrame.pack_propagate(False)

        self.buttonFrame = tk.Frame(main_frame, bg="#dee4e9")
        self.buttonFrame.pack(side="bottom", anchor="center")
        self.buttonFrame.pack_propagate(False)

        self.cal = Calendar(
            self.leftFrame,
            selectmode="day",
            date_pattern="dd/mm/yyyy",
            font=("Calisto MT", 24),
            weekendbackground="#dee4e9",
            weekendforeground="#641c34",
            headersbackground="#dee4e9",
            selectbackground="#b2a29f",  # sfondo del giorno selezionato
            selectforeground="#dee4e9"
        )
        self.cal.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

        # forza il frame ad avere più spazio
        self.leftFrame.grid_rowconfigure(0, weight=2)
        self.leftFrame.grid_columnconfigure(0, weight=2)

        # Treeview: time slots as parent nodes (tree column text), children show Appuntamento/Utente
        self.schedule = ttk.Treeview(self.rightFrame, columns=("Appuntamento", "Utente"), show="tree headings")
        self.schedule.grid(row=3, column=0, sticky="nswe")
        self.schedule.heading("Appuntamento", text="Appuntamento")
        self.schedule.heading("Utente", text="Utente")

        self.create = tk.Button(self.buttonFrame, text="Crea", command=lambda: self.create_event_func(self.description.get()))
        self.create.grid(row=1, column=0, pady=(10, 0))
        tk.Button(self.buttonFrame, text = "Modifica", command= lambda: self.open_popup()).grid(row = 4, column = 0, pady = (10, 0))
        tk.Button(self.buttonFrame, text="Elimina", command=lambda: self.delete_func()).grid(row=5, column=0, pady=(10, 0))

        tk.Label(self.buttonFrame, text="Descrizione").grid(row=2, column=0)
        self.description = (tk.Entry(self.buttonFrame, width=50))
        self.description.grid(row=3, column=0, pady=(10, 0))

        self.time_nodes = {}
        self.fill_schedule()

        #Verifico che tutti gli appuntamenti non siano scaduti
        self.validate_date()

        # self.create_event_on_calendar()
        self.cal.bind("<<CalendarSelected>>", self.on_date_selected)
        self.schedule.bind("<<TreeviewSelect>>", self.on_hour_selected)


    #riempie il calendario del giorno con i vari orari
    def fill_schedule(self):
        # Clear any existing nodes
        for item in self.schedule.get_children():
            self.schedule.delete(item)
        self.time_nodes.clear()
        for i in range(8, 20):
            for minute in (0, 30):
                time_str = f"{i:02d}:{minute:02d}"
                iid = self.schedule.insert("", "end", text=time_str, values=("", ""))
                self.time_nodes[time_str] = iid

    #callBack per la selezione del giorno
    def on_date_selected(self, event):
        cal = event.widget
        selected_date = cal.get_date()
        gv.CurrentDate = datetime.strptime(selected_date, "%d/%m/%Y").date()
        self.create_event_on_timeTable(gv.CurrentDate)

    #callback per la selezione dell'orario
    def on_hour_selected(self, event):
        tree = event.widget
        selected = tree.selection()
        if not selected:
            return
        item = selected[0]
        # If a child is selected, get its parent to read the time text
        parent = tree.parent(item) if tree.parent(item) else item
        time_text = tree.item(parent, "text")
        try:
            gv.CurrentHour = datetime.strptime(time_text, "%H:%M").time()
        except Exception:
            pass

    #cancella gli appuntamento che sono scaduti
    def validate_date(self):
        for appointment in gv.appointment_list:
            if appointment.date_time > appointment.date_time + relativedelta(months=1):
                gv.appointment_list.remove(appointment)

    #evidenzia il giorno sul calendario in cui vi è un appuntamento
    def create_event_on_calendar(self):
        self.cal.calevent_remove('all')
        for app in gv.appointment_list:
            if gv.CurrentUser.isAdmin:
                onlyDate = app.date_time.date()
                self.cal.calevent_create(onlyDate, "Appuntamento", "appointment")
                self.cal.tag_config("appointment", background="#641c34", foreground="white")
            else:
                if app.user.user_id == gv.CurrentUser.user_id:
                    onlyDate = app.date_time.date()
                    self.cal.calevent_create(onlyDate, "Appuntamento", "appointment")
                    self.cal.tag_config("appointment", background="#641c34", foreground="white")

    #Funzione che crea un evento sulla TimeTable
    def create_event_on_timeTable(self, date):
        # Clear children under each time node
        for time_iid in self.time_nodes.values():
            for child in self.schedule.get_children(time_iid):
                self.schedule.delete(child)

        #Inserisci gli appuntamenti del giorno selezionato
        for app in gv.appointment_list:
            if app.date_time.date() == date:
                row_time_str = app.date_time.strftime("%H:%M")
                parent_iid = self.time_nodes.get(row_time_str)
                if not parent_iid:
                    continue

                show_this = False
                display_user = ""
                display_desc = ""
                if gv.CurrentUser.isAdmin:
                    show_this = True
                    display_user = f"{app.user.firstName} {app.user.LastName}"
                    display_desc = app.description
                else:
                    if app.user.user_id == gv.CurrentUser.user_id:
                        show_this = True
                        display_user = f"{app.user.firstName} {app.user.LastName}"
                        display_desc = app.description

                if show_this:
                    # Insert a child entry under the time slot
                    self.schedule.insert(parent_iid, "end", text="", values=(display_desc, display_user))



    def create_event_func(self, description):
        self.ac.create_appointment(description)
        self.create_event_on_timeTable(gv.CurrentDate)
        self.create_event_on_calendar()
        self.description.delete(0, tk.END)


    def open_popup(self):
        index = self.ac.find_appointment()
        if index is not None:

            self.popup = tk.Toplevel(self)
            self.popup.title("popup")
            self.popup.geometry("400x300")

            hour_list = []
            for i in range(8, 20):
                for minute in (0, 30):
                    time_str = f"{i:02d}:{minute:02d}"
                    hour_list.append(time_str)


            self.orari = ttk.Combobox(self.popup, values = hour_list)
            self.orari.set(gv.appointment_list[index].date_time.strftime("%H:%M"))
            self.orari.grid(row = 0, column = 1)

            self.descr = tk.Entry(self.popup, width = 50)
            self.descr.grid(row = 1, column = 1)
            self.descr.insert(0, gv.appointment_list[index].description)

            self.save = tk.Button(self.popup, text = "Save", command = lambda: save_new_data())
            self.save.grid(row = 2, column= 1)

        def save_new_data():
            new_time = self.orari.get()
            new_time =  datetime.strptime(new_time, "%H:%M").time()
            new_description = self.descr.get()
            self.ac.update_appointment(index, new_time, new_description)
            self.create_event_on_timeTable(gv.CurrentDate)
            self.create_event_on_calendar()
            self.popup.destroy()

    def delete_func(self):
        self.ac.delete_appointment()
        self.create_event_on_calendar()
        self.create_event_on_timeTable(gv.CurrentDate)









