import tkinter as tk
from tkinter import PhotoImage
from Src.Controllers.AccountController import AccountController
import Src.GlobalVariables.GlobalVariables as gv
import os
import customtkinter as ctk


class UserSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")
        self.lc = AccountController()

        base_path = os.path.dirname(__file__)
        icon_dir = os.path.join(base_path, "..", "Images", "Icone")
        logout_icon = PhotoImage(file=os.path.join(icon_dir, "Logout.png"))

        header_frame = tk.Frame(self, bg="#000534", height=50)
        header_frame.pack(side= "top", fill= "x")
        header_frame.pack_propagate(False)

        back_btn = ctk.CTkButton(header_frame,
                                 text = "Back",
                                 font=("Calisto MT", 18, "bold"),
                                 image=logout_icon,
                                 compound= "left",
                                 width= 150,
                                 corner_radius=10,
                                 fg_color="white",
                                 border_color="#000534",
                                 border_width=2,
                                 text_color="#000534",
                                 command= lambda: controller.mostra_frame("MainMenu"))
        back_btn.pack(side= "left", padx=(20,0))

        title_frame = tk.Frame(self, bg="#cfd7dc", height=40)
        title_frame.pack(side="top", fill="x")
        title_frame.pack_propagate(False)

        label_title = tk.Label(title_frame,
                               text="Profilo Utente",
                               font=("Calisto MT", 20, "bold"),
                               bg="#cfd7dc",
                               fg="#000534")

        label_title.pack(side="left", padx=(10,0))
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
                              text="Dati Profilo",
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

        # EntryFields
        form_section = tk.Frame(info_frame, bg="#cfd7dc")
        form_section.pack(fill="both", expand=True)

        FirstNameLabel = tk.Label(form_section,
                                  text="Nome",
                                  font=("Calisto MT", 15, "bold"),
                                  bg="#cfd7dc",
                                  fg="#000534")
        FirstNameLabel.grid(row=0, column=0, padx=(220,50), pady=(50, 0))

        #self.FirstName = tk.Entry(form_section,)
        self.FirstName = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=200, corner_radius=10, fg_color ="white", text_color="#000534", border_color= "#000534", border_width=2)
        self.FirstName.grid(row=1, column=0, padx=(170, 5), pady=5)

        form_section.grid_columnconfigure(2, minsize=100)

        LastNameLabel = tk.Label(form_section,
                                  text="Cognome",
                                  font=("Calisto MT", 15, "bold"),
                                  bg="#cfd7dc",
                                  fg="#000534")
        LastNameLabel.grid(row=0, column=3, padx=(150, 50), pady=(50, 0))
        self.LastName = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=200, corner_radius=10, fg_color ="white", text_color="#000534", border_color= "#000534", border_width=2)
        self.LastName.grid(row=1, column=3, padx=(150, 50), pady=5)


        EmailLabel = tk.Label(form_section,
                                  text="Email",
                                  font=("Calisto MT", 15, "bold"),
                                  bg="#cfd7dc",
                                  fg="#000534")

        EmailLabel.grid(row=2, column=0, padx=(220, 50), pady=(50, 0))

        self.Email = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=200, corner_radius=10, fg_color ="white", text_color="#000534", border_color= "#000534", border_width=2)
        self.Email.grid(row=3, column=0, padx=(170, 5), pady=5)

        UsernameLabel = tk.Label(form_section,
                                      text="Username",
                                      font=("Calisto MT", 15, "bold"),
                                      bg="#cfd7dc",
                                      fg="#000534")

        UsernameLabel.grid(row=2, column=3, padx=(150, 50), pady=(50, 0))
        self.Username = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=200, corner_radius=10, fg_color ="white", text_color="#000534", border_color= "#000534", border_width=2)
        self.Username.grid(row=3, column=3, padx=(150, 50), pady=5)

        PasswordLabel = (tk.Label(form_section,
                                  text="Password",
                                  font=("Calisto MT", 15, "bold"),
                                  bg="#cfd7dc",
                                  fg="#000534"
                                  ))
        PasswordLabel.grid(row=4, column=0, padx=(220, 50), pady=(50, 0))
        self.Password = ctk.CTkEntry(form_section, font=("Calisto MT", 15), width=200, corner_radius=10, fg_color ="white", text_color="#000534", border_color= "#000534", border_width=2)
        self.Password.grid(row=5, column=0, padx=(170, 5), pady=5)

        btn_section = tk.Frame(info_frame, bg="#cfd7dc")
        btn_section.pack(fill="x", expand=True, side="top")
        #btn_section.pack_propagate(False)

        btn_section.grid_columnconfigure(0, minsize=300)
        btn_section.grid_columnconfigure(2, minsize=50)
        btn_section.grid_columnconfigure(4, minsize=300)

        edit_btn = ctk.CTkButton(btn_section,
                                 text = "Modifica",
                                 font=("Calisto MT", 18, "bold"),
                                 width= 150,
                                 corner_radius=10,
                                 fg_color="white",
                                 border_color="#000534",
                                 border_width=2,
                                 text_color="#000534",
                                 command= lambda: self.enable_field())

        edit_btn.grid(row=0, column=1, padx=(0, 10), pady=(0, 170))

        save_btn = ctk.CTkButton(btn_section,
                                 text = "Salva",
                                 font=("Calisto MT", 18, "bold"),
                                 width= 150,
                                 corner_radius=10,
                                 fg_color="white",
                                 border_color="#000534",
                                 border_width=2,
                                 text_color="#000534",
                                 command= lambda: self.edit_data())

        save_btn.grid(row=0, column=3, padx=(10, 0), pady=(0, 170))




    def load_data(self):
        print(gv.CurrentUser)
        if gv.CurrentUser:
            user = gv.CurrentUser
            self.enable_field()
            self.FirstName.delete(0, tk.END)
            self.FirstName.insert(0, user.firstName)
            self.FirstName.configure(state = "readonly")

            self.LastName.delete(0, tk.END)
            self.LastName.insert(0, user.LastName)
            self.LastName.configure(state="readonly")

            self.Email.delete(0, tk.END)
            self.Email.insert(0, user.email)
            self.Email.configure(state="readonly")

            self.Username.delete(0, tk.END)
            self.Username.insert(0, user.username)
            self.Username.configure(state="readonly")

            self.Password.delete(0, tk.END)
            self.Password.insert(0, user.Password)
            self.Password.configure(state="readonly")

    def enable_field(self):
        self.FirstName.configure(state="normal")
        self.LastName.configure(state="normal")
        self.Email.configure(state="normal")
        self.Username.configure(state="normal")
        self.Password.configure(state="normal")

    def edit_data(self):
        self.lc.edit_personal_info(self.FirstName.get(),self.LastName.get(),self.Email.get(),self.Username.get(),self.Password.get())
        self.load_data()