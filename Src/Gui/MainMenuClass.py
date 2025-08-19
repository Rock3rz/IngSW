import tkinter as tk
from tkinter import messagebox, PhotoImage
import Src.GlobalVariables.GlobalVariables as gv
from Src.Controllers.AccountController import AccountController
import customtkinter as ctk
import os


#Questa classe conterrà il frame con i tasti di navigazione per il menu principale
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")
        self.lc = gv.account_controller

        base_path = os.path.dirname(__file__)
        icon_dir = os.path.join(base_path, "..", "Images", "Icone")

        user_icon = PhotoImage(file=os.path.join(icon_dir, "Utente.png"))
        calendar_icon = PhotoImage(file=os.path.join(icon_dir, "Calendario.png"))
        car_icon = PhotoImage(file=os.path.join(icon_dir, "Auto.png"))
        client_icon = PhotoImage(file=os.path.join(icon_dir, "Clienti.png"))
        quote_icon = PhotoImage(file=os.path.join(icon_dir, "Preventivi.png"))
        add_user_icon = PhotoImage(file=os.path.join(icon_dir, "CreaUtente.png"))
        logout_icon = PhotoImage(file=os.path.join(icon_dir, "Logout.png"))

        header_frame = tk.Frame(self, bg="#dee4e9")
        header_frame.pack(fill="x", pady=(50, 20), padx=(60, 100))

        label_title = tk.Label(header_frame, text="Home Page", font=("Calisto MT", 32, "bold"), fg="#000534",
                               bg="#dee4e9")

        logout_btn = ctk.CTkButton(header_frame,
                                   text="Logout",
                                   image=logout_icon,
                                   compound="left",
                                   font=("Calisto MT", 15, "bold"),
                                   width=150,
                                   corner_radius=10,
                                   fg_color="white",
                                   border_color="#000534",
                                   border_width=2,
                                   text_color="#000534",
                                   command=lambda: (controller.mostra_frame("LoginFrame"), self.lc.LogOut()))


        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_columnconfigure(1, weight=0)
        header_frame.grid_columnconfigure(2, weight=1)

        label_title.grid(row=0, column=1, padx=(310,0))
        logout_btn.grid(row=0, column=2, sticky="e", padx=(120, 0), pady=0)


        #Frame interno per poter usare pack e grid senza generare errori
        content = tk.Frame(self, bg="#dee4e9")
        content.pack(pady=(100, 70))


        user_sect_btn = ctk.CTkButton(content,
                                      text = "Profilo Utente",
                                      image = user_icon,
                                      compound = "left",
                                      font=("Calisto MT", 20, "bold"),
                                      width=250,
                                      height=220,
                                      corner_radius=10,
                                      fg_color="#081f4c",
                                      border_color="#000534",
                                      border_width=2,
                                      text_color="#b2a29f",
                                      command= lambda: controller.mostra_frame("UserSection"))
        user_sect_btn.grid(row = 2, column = 1, padx = 80)

        vehicle_sect_btn = ctk.CTkButton(content,
                                         text = "Parco Auto",
                                         image=car_icon,
                                         compound="left",
                                         font=("Calisto MT", 20, "bold"),
                                         width=250,
                                         height=220,
                                         corner_radius=10,
                                         fg_color="#081f4c",
                                         border_color="#000534",
                                         border_width=2,
                                         text_color="#b2a29f",
                                         command= lambda: controller.mostra_frame("VehicleSection"))

        vehicle_sect_btn.grid(row = 2, column = 2, padx=80)

        client_sect_btn = ctk.CTkButton(content,
                                    text="Lista Clienti",
                                    image=client_icon,
                                    compound="left",
                                    font=("Calisto MT", 20, "bold"),
                                    width=250,
                                    height=220,
                                    corner_radius=10,
                                    fg_color="#081f4c",
                                    border_color="#000534",
                                    border_width=2,
                                    text_color="#b2a29f",
                                    command=lambda: controller.mostra_frame("ClientSection"))
        client_sect_btn.grid(row = 2, column = 3, padx=80)

        quote_sect_btn = ctk.CTkButton(content,
                                text = "Preventivi",
                                image=quote_icon,
                                compound="left",
                                font=("Calisto MT", 20, "bold"),
                                width=250,
                                height=220,
                                corner_radius=10,
                                fg_color="#081f4c",
                                border_color="#000534",
                                border_width=2,
                                text_color="#b2a29f",
                                command= lambda: controller.mostra_frame("QuoteSection"))
        quote_sect_btn.grid(row = 3, column = 1, padx=80, pady=100)

        apt_sect_btn = ctk.CTkButton(content,
                                     text="Calendario\nAppuntamenti",
                                     font=("Calisto MT", 20, "bold"),
                                     image=calendar_icon,
                                     compound="left",
                                     width=250,
                                     height=220,
                                     corner_radius=10,
                                     fg_color="#081f4c",
                                     border_color="#000534",
                                     border_width=2,
                                     text_color="#b2a29f",
                                     command=lambda: (controller.mostra_frame("AppointmentSection"), controller.frames["AppointmentSection"].create_event_on_calendar()))
        apt_sect_btn.grid(row=3, column=2, padx=80, pady=100)

        create_us_btn = ctk.CTkButton(content,
                                      text="Crea Utente",
                                      font=("Calisto MT", 20, "bold"),
                                      image=add_user_icon,
                                      compound="left",
                                      width=250,
                                      height= 220,
                                      corner_radius=10,
                                      fg_color="#081f4c",
                                      border_color="#000534",
                                      border_width=2,
                                      text_color="#b2a29f",
                                      command=lambda: isAdminCheckButton())
        create_us_btn.grid(row=3, column=3, padx=80, pady = 100)

        # funzione interna per la verifica e il caricamento delle funzioni da admin
        def isAdminCheckButton():
            if gv.isAdminUser:
                controller.mostra_frame("CreateUserSection")
            else:
                messagebox.showinfo("Accesso non consentito", "Non hai i permessi per accedere a questa sezione!")