import tkinter as tk
import customtkinter as ctk
from tkinter import PhotoImage
import os
from Src.Controllers.AccountController import AccountController
import pandas as pd
import Src.GlobalVariables.GlobalVariables as gv
from tkinter import messagebox
from Src.Controllers.APIController import APIController


class CreateUserSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")

        self.Api = APIController()
        self.lc = AccountController()
        self.selected_index = None

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
                                 command=lambda: controller.mostra_frame("MainMenu"))
        back_btn.pack(side="left", padx=(20, 0))

        title_frame = tk.Frame(self, bg="#cfd7dc", height=40)
        title_frame.pack(side="top", fill="x")
        title_frame.pack_propagate(False)

        label_title = tk.Label(title_frame,
                               text="Crea Utente",
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

        # Spazio sinistro
        spazio_sinistro = tk.Frame(main_frame, bg="#dee4e9", width=30)
        spazio_sinistro.grid(row=0, column=0, sticky="ns")

        info_frame = tk.Frame(main_frame, bg="#cfd7dc", height=970, width=650)
        info_frame.grid(row=0, column=3, sticky="n", pady=(55, 0))
        info_frame.grid_propagate(False)

        data_label = tk.Label(info_frame,
                              text="Utenti  Registrati",
                              font=("Calisto MT", 18, "bold"),
                              bg="#cfd7dc",
                              fg="#000534")
        data_label.pack(anchor="center")

        border_frame = tk.Frame(info_frame, bg="#bfc9cf", height=2, width=400)
        border_frame.pack(anchor="center")
        border_frame.pack_propagate(False)

        listbox_frame = tk.Frame(info_frame, bg="#cfd7dc")
        listbox_frame.pack(anchor="center", pady=(15, 0), padx=15)
        listbox_frame.grid_propagate(False)

        self.useListBox = tk.Listbox(
            listbox_frame,
            font=("Calibri", 14),
            width=50,
            height=20,
            bg = "#dee4e9"
        )
        self.useListBox.pack(side="left", fill="y")

        scrollbar = tk.Scrollbar(listbox_frame, orient="vertical", command=self.useListBox.yview)
        scrollbar.pack(side="left", fill="y")
        self.useListBox.config(yscrollcommand=scrollbar.set)

        self.fill_listbox()
        self.useListBox.bind("<<ListboxSelect>>", self.on_select)

        # Spazio centrale
        spazio_centrale = tk.Frame(main_frame, bg="#dee4e9", width=30)
        spazio_centrale.grid(row=0, column=2, sticky="ns")

        # Frame Dati Nuovo Cliente
        entryinfo_frame = tk.Frame(main_frame, bg="#cfd7dc", height=970, width=650)
        entryinfo_frame.grid(row=0, column=1, sticky="n")
        entryinfo_frame.grid_propagate(False)

        right_data_label = tk.Label(entryinfo_frame,
                                    text="Dati Nuovo Utente",
                                    font=("Calisto MT", 18, "bold"),
                                    bg="#cfd7dc",
                                    fg="#000534")
        right_data_label.grid(row=0, column=0, columnspan=2, pady=(10, 10))

        right_border_frame = tk.Frame(entryinfo_frame, bg="#bfc9cf", height=2, width=590)
        right_border_frame.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        right_border_frame.grid_propagate(False)

        FirstNameLabel = tk.Label(entryinfo_frame,
                                  text="Nome",
                                  font=("Calisto MT", 15, "bold"),
                                  bg="#cfd7dc",
                                  fg="#000534")
        FirstNameLabel.grid(row=2, column=0, sticky="e", padx=(130,30) , pady=(40, 30))
        self.FirstName = ctk.CTkEntry(entryinfo_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                      fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.FirstName.grid(row=2, column=1, padx=(0, 150), pady=(20, 30))

        LastNameLabel = tk.Label(entryinfo_frame,
                                  text="Cognome",
                                  font=("Calisto MT", 15, "bold"),
                                  bg="#cfd7dc",
                                  fg="#000534")
        LastNameLabel.grid(row=3, column=0, sticky="e", padx=(130, 30), pady=(0, 30))
        self.LastName = ctk.CTkEntry(entryinfo_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                      fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.LastName.grid(row=3, column=1, padx=(0, 150), pady=(0, 30))

        EmailLabel = tk.Label(entryinfo_frame,
                                 text="Email",
                                 font=("Calisto MT", 15, "bold"),
                                 bg="#cfd7dc",
                                 fg="#000534")
        EmailLabel.grid(row=4, column=0, sticky="e", padx=(130, 30), pady=(0, 30))
        self.Email = ctk.CTkEntry(entryinfo_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                     fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.Email.grid(row=4, column=1, padx=(0, 150), pady=(0, 30))

        UsernameLabel = tk.Label(entryinfo_frame,
                                 text="Username",
                                 font=("Calisto MT", 15, "bold"),
                                 bg="#cfd7dc",
                                 fg="#000534")
        UsernameLabel.grid(row=5, column=0, sticky="e", padx=(130, 30), pady=(0, 30))
        self.Username = ctk.CTkEntry(entryinfo_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                     fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.Username.grid(row=5, column=1, padx=(0, 150), pady=(0, 30))


        PasswordLabel = tk.Label(entryinfo_frame,
                                 text="Password",
                                 font=("Calisto MT", 15, "bold"),
                                 bg="#cfd7dc",
                                 fg="#000534")
        PasswordLabel.grid(row=6, column=0, sticky="e", padx=(130, 30), pady=(0, 30))
        self.Password = ctk.CTkEntry(entryinfo_frame, show="*", font=("Calisto MT", 15), width=200, corner_radius=10,
                                     fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.Password.grid(row=6, column=1, padx=(0, 150), pady=(0, 30))

        self.is_admin = tk.BooleanVar()
        is_admin_button = ctk.CTkCheckBox(entryinfo_frame,
                                          text="is_admin",
                                          font=("Calisto MT", 18, "bold"),
                                          width=150,
                                          corner_radius=10,
                                          fg_color="#000534",
                                          border_color="#000534",
                                          border_width=2,
                                          text_color="#000534",
                                          variable=self.is_admin)
        is_admin_button.grid(row=7, column=0, columnspan=2, padx=(110, 30), pady=(0, 20))


        confirm_btn = ctk.CTkButton(entryinfo_frame,
                                 text = "Conferma",
                                 font=("Calisto MT", 18, "bold"),
                                 width= 150,
                                 corner_radius=10,
                                 fg_color="white",
                                 border_color="#000534",
                                 border_width=2,
                                 text_color="#000534",
                                 command=self.create_user_and_clear)

        confirm_btn.grid(row=9, column=0, padx=(120, 10), pady=(90, 50))

        delete_btn = ctk.CTkButton(entryinfo_frame,
                                 text = "Elimina",
                                 font=("Calisto MT", 18, "bold"),
                                 width= 150,
                                 corner_radius=10,
                                 fg_color="white",
                                 border_color="#000534",
                                 border_width=2,
                                 text_color="#000534",
                                 command=lambda: self.elimina_utente())

        delete_btn.grid(row=9, column=1, padx=(10, 0), pady=(90, 50))
       

        entryinfo_frame.grid_columnconfigure(0, weight=0)
        entryinfo_frame.grid_columnconfigure(1, weight=1)


        #spazio destro
        spazio_destro = tk.Frame(main_frame, bg="#dee4e9", width=30)
        spazio_destro.grid(row=0, column=4, sticky="ns")

        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=0)
        main_frame.grid_columnconfigure(2, weight=1)
        main_frame.grid_columnconfigure(3, weight=0)
        main_frame.grid_columnconfigure(4, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)

        main_frame.grid_rowconfigure(1, minsize=40)


    def create_user_and_clear(self):
        self.lc.create_user(
            self.FirstName.get(),
            self.LastName.get(),
            self.Email.get(),
            self.Username.get(),
            self.Password.get(),
            self.is_admin.get()
        )
        self.clear_fields()
        self.fill_listbox()

    def clear_fields(self):
        self.FirstName.delete(0, tk.END)
        self.LastName.delete(0, tk.END)
        self.Email.delete(0, tk.END)
        self.Username.delete(0, tk.END)
        self.Password.delete(0, tk.END)
        self.is_admin.set(False)

    def fill_listbox(self):
        self.useListBox.delete(0, tk.END)

        for user in gv.user_list:
            self.useListBox.insert(tk.END, f"{user.firstName} {user.LastName} - {user.email}")



    #Questa funzione serve per eliminare l'utente desiderato ed aggiornare di conseguenza il file usato come DB e la listbox
    def elimina_utente(self):

        if self.selected_index is None:
            messagebox.showwarning("Attenzione", "Seleziona un utente prima di premere 'Elimina'")
            return

        utente = gv.user_list[self.selected_index]

        conferma = messagebox.askyesno(
            "Conferma eliminazione",
            f"Eliminare {utente.firstName} {utente.LastName}?"
        )
        if not conferma:
            return

        gv.user_list.pop(self.selected_index)

        APIController.write_user_on_csv()
        self.selected_index = None

        self.fill_listbox()
        #self.Api.refresh_user_list()

    #evento per permettere la selezione di un nome dalla lista
    def on_select(self, event = None):
        if event:
            widget = event.widget
            self.selected_index = widget.curselection()
        else:
            self.selected_index = self.useListBox.curselection()

        if self.selected_index:
            self.selected_index = self.selected_index[0]
            value = self.useListBox.get( self.selected_index)

