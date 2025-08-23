import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv
import customtkinter as ctk

class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")
        self.lc = gv.account_controller

        # Titolo in alto centrato
        label_title = tk.Label(self, text="Benvenuti!", font=("Calisto MT", 28, "bold"), fg="#000534", bg="#dee4e9")
        label_title.pack(pady=(250, 20), padx=(215, 100))


        # Frame interno
        content = tk.Frame(self, bg="#dee4e9")
        content.pack(pady=(0, 70))

        #Username
        label_username = tk.Label(content, text="Username", bg="#dee4e9", font=("Calisto MT", 14), fg="#000534")
        label_username.grid(row=0, column=0, pady=10, sticky="e", padx=(0, 20))
        self.name = ctk.CTkEntry(content, width=200, corner_radius= 10, fg_color="white", text_color="black", border_color= "#000534", border_width= 2)
        self.name.grid(row=0, column=1, pady=10)

        # Password
        label_password = tk.Label(content, text="Password", bg="#dee4e9", font=("Calisto MT", 14), fg="#000534")
        label_password.grid(row=1, column=0, pady=10, sticky="e", padx=(0, 20))
        self.password = ctk.CTkEntry(content, width=200, show="*", corner_radius= 10, fg_color="white", text_color="black", border_color= "#000534", border_width=2)
        self.password.grid(row=1, column=1, pady=10)
        self.password.grid(row=1, column=1, pady=10)

        # Pulsanti
        btn_login = ctk.CTkButton(content,
                                  text="Login",
                                  font=("Calisto MT", 13, "bold"),
                                  width=150,
                                  corner_radius= 10,
                                  fg_color="white",
                                  border_color= "#000534",
                                  border_width=2,
                                  text_color= "#000534",
                                  command=lambda: submit_logic())
        btn_login.grid(row=2, column=1, sticky="", pady=(10, 5))

        btn_forgot = tk.Button(content, text="Password Dimenticata?", command=self.lc.reset_password, bg="#dee4e9", relief="flat", fg="blue", cursor="hand2")
        btn_forgot.grid(row=3, column=1, sticky="")

        #Se premo il tasto invio, logga direttamente
        self.name.focus_set()
        self.name.bind("<Return>", lambda e: submit_logic())
        self.password.bind("<Return>", lambda e: submit_logic())

        def submit_logic():
            self.lc.login(self.name.get(), self.password.get())
            self.name.delete(0, tk.END)
            self.password.delete(0, tk.END)
            if gv.canEnter:
                controller.frames["UserSection"].load_data()
                controller.mostra_frame("MainMenu")
