import tkinter as tk
from Src.Controllers.AccountController import AccountController
import pandas as pd
import Src.GlobalVariables.GlobalVariables as gv
from tkinter import messagebox
from Src.Controllers.APIController import APIController


class CreateUserSection(tk.Frame):
    def __init__(self, parent, controller):
        self.Api = APIController()
        super().__init__(parent)
        self.lc = AccountController()  # istanzia ogni volta che apro il frame
        self.selected_index = None
        # Labels ed Entry
        tk.Label(self, text="Crea Utente").grid(row=1, column=1)

        tk.Label(self, text="First Name").grid(row=2, column=1)
        self.FirstName = tk.Entry(self)
        self.FirstName.grid(row=2, column=2)

        tk.Label(self, text="Last Name").grid(row=3, column=1)
        self.LastName = tk.Entry(self)
        self.LastName.grid(row=3, column=2)

        tk.Label(self, text="Email").grid(row=4, column=1)
        self.Email = tk.Entry(self)
        self.Email.grid(row=4, column=2)

        tk.Label(self, text="Username").grid(row=5, column=1)
        self.Username = tk.Entry(self)
        self.Username.grid(row=5, column=2)

        tk.Label(self, text="Password").grid(row=6, column=1)
        self.Password = tk.Entry(self, show="*")  # meglio nascondere password
        self.Password.grid(row=6, column=2)

        self.is_admin = tk.BooleanVar()
        is_admin_button = tk.Checkbutton(self, text="is_admin", variable=self.is_admin)
        is_admin_button.grid(row=7, column=1)

        # Buttons
        confirm = tk.Button(self, text="Crea", command=self.create_user_and_clear)
        confirm.grid(row=8, column=2)

        tk.Button(self, text="Back", command=lambda: controller.mostra_frame("MainMenu")).grid(row=8, column=1)
        tk.Button(self, text="Elimina", command= lambda: self.elimina_utente()).grid(row=10, column=10)

        # Listbox
        self.useListBox = tk.Listbox(self)
        self.useListBox.grid(row=1, column=10, rowspan=7)

        self.fill_listbox()

        self.useListBox.bind("<<ListboxSelect>>", self.on_select)

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
        self.fill_listbox()  # aggiorna la lista dopo creazione

    def clear_fields(self):
        self.FirstName.delete(0, tk.END)
        self.LastName.delete(0, tk.END)
        self.Email.delete(0, tk.END)
        self.Username.delete(0, tk.END)
        self.Password.delete(0, tk.END)
        self.is_admin.set(False)

    def fill_listbox(self):
        self.useListBox.delete(0, tk.END)
        '''
        self.df = pd.read_csv(gv.User_file_path, usecols=["ID","Name", "LastName", "Email","UserName","Password","IsAdmin"])
        #self.df = pd.read_csv(gv.User_file_path)
        print(self.df)

        #self.df.columns = self.df.columns.str.strip()

        for _, row in self.df.iterrows():
            self.useListBox.insert(tk.END, f"{row['Name']} {row['LastName']} - {row['Email']}")
        '''
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
        #self.Api.refresh_user_list()

        '''
        conferma = messagebox.askyesno(
            "Conferma eliminazione",
            f"Eliminare {utente['Name']} {utente['LastName']}?"
        )
        if not conferma:
            return

        userIndex = utente["ID"]

        self.newRead = pd.read_csv(gv.User_file_path) #creo una lista provvisioria
        self.newRead = self.df.drop(self.newRead[self.newRead["ID"] == userIndex].index) #elimino dalla riga
        print(self.newRead)

        self.newRead.to_csv(gv.User_file_path, index=False)

        self.fill_listbox()
        
        '''


        #ID, Name, LastName, Email, UserName, Password, IsAdmin
        #1, Francesco, Trapano, TP @ abruzzolandia.coma, admin, admin, True


    #evento per permettere la selezione di un nome dalla lista
    def on_select(self, event = None):
        if event:
            widget = event.widget
            self.selected_index = widget.curselection()
        else:
            self.selected_index = self.useListBox.curselection()

        if self.selected_index:
            self.selected_index = self.selected_index[0]
            value = self.useListBox.get( self.selected_index)  # Testo della riga selezionata
            print(f"Indice selezionato: { self.selected_index}, Valore: {value}")
