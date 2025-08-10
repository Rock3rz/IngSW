import pandas as pd
import tkinter as tk
from tkinter import PhotoImage
import os
import Src.GlobalVariables.GlobalVariables as gv
import customtkinter as ctk
from Src.Controllers.ClientController import ClientController


class CreateClientSectionClass(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent, bg="#dee4e9")
        self.cc = gv.client_controller

        base_path = os.path.dirname(__file__)
        icon_dir = os.path.join(base_path, "..", "Images", "Icone")
        logout_icon = PhotoImage(file=os.path.join(icon_dir, "Logout.png"))

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
                                 command=lambda: (
                                     controller.frames["ClientSection"].fill_listbox(),  # aggiorna la listbox
                                     controller.mostra_frame("ClientSection")  # poi mostra il frame
                                 ))
        back_btn.pack(side="left", padx=(20, 0))

        title_frame = tk.Frame(self, bg="#cfd7dc", height=40)
        title_frame.pack(side="top", fill="x")
        title_frame.pack_propagate(False)

        label_title = tk.Label(title_frame,
                               text="Crea Cliente",
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

        info_frame = tk.Frame(self, bg="#cfd7dc", height=670, width=1000)
        info_frame.pack(anchor="center")
        info_frame.pack_propagate(False)

        data_label = tk.Label(info_frame,
                              text="Dati Cliente Nuovo",
                              font=("Calisto MT", 18, "bold"),
                              bg="#cfd7dc",
                              fg="#000534")
        data_label.pack(anchor="center")
        data_label.pack_propagate(False)

        border_frame = tk.Frame(info_frame, bg="#bfc9cf", height=2, width=940)
        border_frame.pack(anchor="center")
        border_frame.pack_propagate(False)

        final_border = tk.Frame(self, bg="#dee4e9", height=30)
        final_border.pack(side="top", fill="x")
        final_border.pack_propagate(False)

        form_section = tk.Frame(info_frame, bg="#cfd7dc")
        form_section.pack(fill="both", expand=True)

        form_section.grid_columnconfigure(2, minsize=100)

        FirstNameLabel = tk.Label(form_section,
                                  text="Nome",
                                  font=("Calisto MT", 15, "bold"),
                                  bg="#cfd7dc",
                                  fg="#000534")
        FirstNameLabel.grid(row=0, column=0, padx=(220, 50), pady=(50, 0))
        self.name = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=200, corner_radius=10,
                                      fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.name.grid(row=1, column=0, padx=(170, 5), pady=5)

        LastNameLabel = tk.Label(form_section,
                                 text="Cognome",
                                 font=("Calisto MT", 15, "bold"),
                                 bg="#cfd7dc",
                                 fg="#000534")
        LastNameLabel.grid(row=0, column=3, padx=(150, 50), pady=(50, 0))
        self.surname = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=200, corner_radius=10,
                                     fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.surname.grid(row=1, column=3, padx=(150, 50), pady=5)

        EmailLabel = tk.Label(form_section,
                                  text="Email",
                                  font=("Calisto MT", 15, "bold"),
                                  bg="#cfd7dc",
                                  fg="#000534")

        EmailLabel.grid(row=2, column=0, padx=(220, 50), pady=(50, 0))

        self.email = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=200, corner_radius=10, fg_color ="white", text_color="#000534", border_color= "#000534", border_width=2)
        self.email.grid(row=3, column=0, padx=(170, 5), pady=5)

        AddressLabel = tk.Label(form_section,
                              text="Indirizzo",
                              font=("Calisto MT", 15, "bold"),
                              bg="#cfd7dc",
                              fg="#000534")
        AddressLabel.grid(row=4, column=0, padx=(220, 50), pady=(50, 0))
        self.address = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=200, corner_radius=10, fg_color="white",
                                  text_color="#000534", border_color="#000534", border_width=2)
        self.address.grid(row=5, column=0, padx=(170, 5), pady=5)

        CAPLabel = tk.Label(form_section,
                                 text="CAP",
                                 font=("Calisto MT", 15, "bold"),
                                 bg="#cfd7dc",
                                 fg="#000534")

        CAPLabel.grid(row=4, column=3, padx=(150, 50), pady=(50, 0))
        self.cap = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=200, corner_radius=10,
                                     fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.cap.grid(row=5, column=3, padx=(150, 50), pady=5)

        PhoneLabel = (tk.Label(form_section,
                                  text="Numero di Telefono",
                                  font=("Calisto MT", 15, "bold"),
                                  bg="#cfd7dc",
                                  fg="#000534"
                                  ))
        PhoneLabel.grid(row=2, column=3, padx=(150, 50), pady=(50, 0))
        self.phone = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=200, corner_radius=10,
                                     fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.phone.grid(row=3, column=3, padx=(150, 50), pady=5)

        IDLabel = (tk.Label(form_section,
                                  text="ID Cliente",
                                  font=("Calisto MT", 15, "bold"),
                                  bg="#cfd7dc",
                                  fg="#000534"
                                  ))
        IDLabel.grid(row=6, column=0, padx=(220, 50), pady=(50, 0))
        self.id = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=200, corner_radius=10,
                                     fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.id.grid(row=7, column=0, padx=(170, 5), pady=5)


        next_id = self.calcola_prossimo_numero()
        self.id.insert(0, next_id)
        self.id.configure(state="readonly")


        createC_btn = ctk.CTkButton(form_section,
                                 text="Crea Cliente",
                                 font=("Calisto MT", 18, "bold"),
                                 width=150, height=50,
                                 corner_radius=10,
                                 fg_color="white",
                                 border_color="#000534",
                                 border_width=2,
                                 text_color="#000534", command=lambda: (self.cc.create_client(self.id.get(),
                                                                           self.name.get(),
                                                                           self.surname.get(),
                                                                           self.email.get(),
                                                                           self.address.get(),
                                                                           self.phone.get(),
                                                                           self.cap.get()), self.clear_fields()))

        createC_btn.grid(row=9, column=3, padx=(150, 10), pady=(70, 20))


    def clear_fields(self):
        self.name.delete(0, tk.END)
        self.surname.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.phone.delete(0, tk.END)
        self.cap.delete(0, tk.END)
        self.id.config(state="normal")
        self.id.delete(0, tk.END)
        self.id.insert(0, self.calcola_prossimo_numero())
        self.id.config(state = "readonly")


    def calcola_prossimo_numero(self) -> str:
        if not gv.client_list:
            return str(1)
        else:
            return  str(max(c.ID for c in gv.client_list) + 1)


