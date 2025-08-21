import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv
from Src.Controllers.ClientController import ClientController
from Src.Class.Client import Client
from tkinter import messagebox, PhotoImage
import os
import customtkinter as ctk
from PIL import Image

#Classe di gestione Schede clienti
class ClientSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")
        self.cc = gv.client_controller

        self.controller = controller

        #indice cliente selezionato NELLA LISTBOX
        self.selected_client = None

        #Lista di supporto
        self.support_list = []
        
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
                               text="Lista Clienti",
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

        spazio_sinistro = tk.Frame(main_frame, bg="#dee4e9", width=30)
        spazio_sinistro.grid(row=0, column=0, sticky="ns")

        info_frame = tk.Frame(main_frame, bg="#cfd7dc", height=970, width=650)
        info_frame.grid(row=0, column=1, sticky="n")
        info_frame.grid_propagate(False)

        data_label = tk.Label(info_frame,
                              text="Clienti  Registrati",
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

        self.list_client = tk.Listbox(
            listbox_frame,
            font=("Calibri", 14),
            width=50,
            height=20,
            bg="#dee4e9"
        )
        self.list_client.pack(side="left", fill="y")

        scrollbar = tk.Scrollbar(listbox_frame, orient="vertical", command=self.list_client.yview)
        scrollbar.pack(side="left", fill="y")
        self.list_client.config(yscrollcommand=scrollbar.set)

        underListbox_frame = tk.Frame(info_frame, bg="#cfd7dc", height=200, width=400)
        underListbox_frame.pack(anchor="center", pady=(10, 0), padx=15)
        underListbox_frame.pack_propagate(False)

        # Spazio centrale
        spazio_centrale = tk.Frame(main_frame, bg="#dee4e9", width=30)
        spazio_centrale.grid(row=0, column=2, sticky="ns")

        # Frame Dati Ricerca Cliente
        entryinfo_frame = tk.Frame(main_frame, bg="#cfd7dc", height=500, width=650)
        entryinfo_frame.grid(row=0, column=3, sticky="n", pady=(50, 0))
        entryinfo_frame.grid_propagate(False)

        right_data_label = tk.Label(entryinfo_frame,
                                    text="Dati Cliente Da Cercare",
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
        FirstNameLabel.grid(row=2, column=0, sticky="e", padx=(130, 30), pady=30)
        self.first_nameSrc = ctk.CTkEntry(entryinfo_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                      fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.first_nameSrc.grid(row=2, column=1, padx=(0, 150), pady=30)

        LastNameLabel = tk.Label(entryinfo_frame,
                                 text="Cognome",
                                 font=("Calisto MT", 15, "bold"),
                                 bg="#cfd7dc",
                                 fg="#000534")
        LastNameLabel.grid(row=3, column=0, sticky="e", padx=(130, 30), pady=(0, 30))
        self.last_nameSrc = ctk.CTkEntry(entryinfo_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                     fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.last_nameSrc.grid(row=3, column=1, padx=(0, 150), pady=(0, 30))

        EmailLabel = tk.Label(entryinfo_frame,
                              text="Email",
                              font=("Calisto MT", 15, "bold"),
                              bg="#cfd7dc",
                              fg="#000534")
        EmailLabel.grid(row=4, column=0, sticky="e", padx=(130, 30), pady=(0, 30))
        self.emailSrc = ctk.CTkEntry(entryinfo_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                  fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.emailSrc.grid(row=4, column=1, padx=(0, 150), pady=(0, 30))

        PhoneLabel = tk.Label(entryinfo_frame,
                              text="Numero di Telefono",
                              font=("Calisto MT", 15, "bold"),
                              bg="#cfd7dc",
                              fg="#000534")
        PhoneLabel.grid(row=5, column=0, sticky="e", padx=(130, 30), pady=(0, 30))
        self.phone_numberSrc = ctk.CTkEntry(entryinfo_frame, font=("Calisto MT", 15), width=200, corner_radius=10,
                                     fg_color="white", text_color="#000534", border_color="#000534", border_width=2)
        self.phone_numberSrc.grid(row=5, column=1, padx=(0, 150), pady=(0, 30))

        cerca_btn = ctk.CTkButton(entryinfo_frame,
                                    text="Cerca",
                                    font=("Calisto MT", 18, "bold"),
                                    width=150,
                                    corner_radius=10,
                                    fg_color="white",
                                    border_color="#000534",
                                    border_width=2,
                                    text_color="#000534",
                                    command = lambda:self.call_search())

        cerca_btn.grid(row=9, column=1, padx=(0, 150), pady=(70, 0))

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

        #Riempio la listbox con TUTTI gli utenti
        self.fill_listbox()

        #Tasti Selezione
        create_btn = ctk.CTkButton(underListbox_frame,
                                  text="Crea Cliente",
                                  font=("Calisto MT", 18, "bold"),
                                  width=150,
                                  corner_radius=10,
                                  fg_color="white",
                                  border_color="#000534",
                                  border_width=2,
                                  text_color="#000534",
                                  command = lambda: controller.mostra_frame("CreateClientSectionClass"))

        create_btn.grid(row=3, column=1, padx= 20, pady=(10, 20))


        visualizza_btn = ctk.CTkButton(underListbox_frame,
                                  text="Visualizza Cliente",
                                  font=("Calisto MT", 18, "bold"),
                                  width=150,
                                  corner_radius=10,
                                  fg_color="white",
                                  border_color="#000534",
                                  border_width=2,
                                  text_color="#000534",
                                  command= lambda: self.open_view_conditional())
        visualizza_btn.grid(row=3, column=2, padx= 20, pady=(10, 20))

        self.list_client.bind("<<ListboxSelect>>", self.on_select)


    def fill_listbox(self):
        self.list_client.delete(0, tk.END)
        self.support_list = []
        for client in gv.client_list:
            self.list_client.insert(tk.END, f"{client.ID} {client.FirstName} {client.LastName}")
            self.support_list.append(client)




    def open_view_conditional(self):
        if self.selected_client is None:
            messagebox.showwarning("ERRORE", "Nessun cliente selezionato!")
            return
        gv.CurrentClient = self.support_list[self.selected_client]
        self.controller.frames["ViewClient"].load_client_infos()
        self.controller.mostra_frame("ViewClient")



    def on_select(self, event = None):
        if event:
            widget = event.widget
            self.selected_client = widget.curselection()
        else:
            self.selected_client = self.list_client.curselection()

        if self.selected_client:
            self.selected_client = self.selected_client[0]
            value = self.list_client.get(self.selected_client)  # Testo della riga selezionata
            print(f"Indice selezionato: { self.selected_client}, Valore: {value}")


    def call_search(self):
        s= ""
        if (self.first_nameSrc.get() == s and
            self.last_nameSrc.get() == s and
            self.emailSrc.get() == s and
            self.phone_numberSrc.get() == s):
            self.fill_listbox()
            return
        tmplist = self.cc.search_client(self.first_nameSrc.get(),
                              self.last_nameSrc.get(),
                              self.emailSrc.get(),
                              self.phone_numberSrc.get())
        if not tmplist:
            messagebox.showwarning("ERRORE", "Nessun cliente trovato")
            return

        self.list_client.delete(0, tk.END)
        self.support_list = []
        for client in tmplist:
            self.list_client.insert(tk.END, f"{client.ID} {client.FirstName} {client.LastName}")
            self.support_list.append(client)




