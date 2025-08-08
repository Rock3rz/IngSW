import tkinter as tk
from tkinter import messagebox
import Src.GlobalVariables.GlobalVariables as gv
from Src.Controllers.AccountController import AccountController
import customtkinter as ctk


#Questa classe conterrà il frame con i tasti di navigazione per il menu principale
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")
        self.lc = AccountController()

        label_title = tk.Label(self, text = "Home Page", font=("Calisto MT", 32, "bold"), fg="#000534", bg="#dee4e9")
        label_title.pack(pady=(50, 20), padx=(60, 100))

        #Frame interno per poter usare pack e grid senza generare errori
        content = tk.Frame(self, bg="#dee4e9")
        content.pack(pady=(100, 70))

        user_sect_btn = ctk.CTkButton(content,
                                      text = "User Section",
                                      font=("Calisto MT", 18, "bold"),
                                      width=200,
                                      height=200,
                                      corner_radius=10,
                                      fg_color="#081f4c",
                                      border_color="#000534",
                                      border_width=2,
                                      text_color="#b2a29f",
                                      command= lambda: controller.mostra_frame("UserSection"))
        user_sect_btn.grid(row = 2, column = 1)

        vehicle_sect_btn = ctk.CTkButton(content,
                                         text = "Vehicle Section",
                                         font=("Calisto MT", 18, "bold"),
                                         width=200,
                                         height=200,
                                         corner_radius=10,
                                         fg_color="#081f4c",
                                         border_color="#000534",
                                         border_width=2,
                                         text_color="#b2a29f",
                                         command= lambda: controller.mostra_frame("VehicleSection"))

        vehicle_sect_btn.grid(row = 2, column = 3, padx=80)

        client_sect_btn = ctk.CTkButton(content,
                                    text="Client Section",
                                    font=("Calisto MT", 18, "bold"),
                                    width=200,
                                    height=200,
                                    corner_radius=10,
                                    fg_color="#081f4c",
                                    border_color="#000534",
                                    border_width=2,
                                    text_color="#b2a29f",
                                    command=lambda: controller.mostra_frame("ClientSection"))
        client_sect_btn.grid(row = 3, column = 1, padx=80, pady = 100)

        quote_sect_btn = ctk.CTkButton(content,
                               text = "Quote Section",
                               font=("Calisto MT", 18, "bold"),
                               width=200,
                               height=200,
                               corner_radius=10,
                               fg_color="#081f4c",
                               border_color="#000534",
                               border_width=2,
                               text_color="#b2a29f",
                               command= lambda: controller.mostra_frame("QuoteSection"))
        quote_sect_btn.grid(row = 3, column = 2, padx=80, pady=100)

        apt_sect_btn = ctk.CTkButton(content,
                                     text="Appointment Section",
                                     font=("Calisto MT", 18, "bold"),
                                     width=200,
                                     height=200,
                                     corner_radius=10,
                                     fg_color="#081f4c",
                                     border_color="#000534",
                                     border_width=2,
                                     text_color="#b2a29f",
                                     command=lambda: controller.mostra_frame("AppointmentSection"))
        apt_sect_btn.grid(row=3, column=3, padx=80, pady=100)

        create_us_btn = ctk.CTkButton(content,
                                      text="CreateUserSection",
                                      font=("Calisto MT", 18, "bold"),
                                      width=200,
                                      height=200,
                                      corner_radius=10,
                                      fg_color="#081f4c",
                                      border_color="#000534",
                                      border_width=2,
                                      text_color="#b2a29f",
                                      command=lambda: isAdminCheckButton())
        create_us_btn.grid(row=2, column=2, padx=80)

        logout_btn = (ctk.CTkButton(content,
                  text="Logout",
                  font=("Calisto MT", 13, "bold"),
                  width=150,
                  corner_radius=10,
                  fg_color="white",
                  border_color="#000534",
                  border_width=2,
                  text_color="#000534",
                  command=lambda: (controller.mostra_frame("LoginFrame"),self.lc.LogOut())))
        logout_btn.grid(row=3, column=5, padx=150)

        # funzione interna per la verifica e il caricamento delle funzioni da admin
        def isAdminCheckButton():
            if gv.isAdminUser:
                controller.mostra_frame("CreateUserSection")
            else:
                messagebox.showinfo("Accesso non consentito", "Non hai i permessi per accedere a questa sezione!")