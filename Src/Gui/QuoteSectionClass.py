import tkinter as tk
import Src.GlobalVariables.GlobalVariables as gv
import customtkinter as ctk
import os
from PIL import Image

#Classe di gestione preventivi
class QuoteSection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#dee4e9")

        self.qc = gv.quote_controller
        self.controller = controller

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
                               text="Preventivi",
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

        main_frame.grid_columnconfigure(0, weight=2)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(0, weight=0)
        main_frame.grid_rowconfigure(1, weight=1)


        leftFrame = tk.Frame(main_frame, bg="#dee4e9")
        leftFrame.grid(row=0, column=0, rowspan= 2, sticky="nsew")

        rightFrame = tk.Frame(main_frame, bg="#dee4e9")
        rightFrame.grid(row=0, column=1, sticky="nsew")

        listbox_frame = tk.Frame(leftFrame, bg="#cfd7dc", height=50, width=90)
        listbox_frame.grid(row=0, column=0, sticky="nsew", padx=(80, 30), pady=(7, 30))

        data_label = tk.Label(listbox_frame,
                              text="Registrati nel sistema",
                              font=("Calisto MT", 18, "bold"),
                              bg="#cfd7dc",
                              fg="#000534")
        data_label.grid(sticky= "we", padx=(70, 25), pady=(10,5))

        self.quoteList = tk.Listbox(listbox_frame,
                                    font=("Calibri", 14),
                                    width=60,
                                    height=25,
                                    bg="#dee4e9",
                                    )
        self.quoteList.grid(row = 1, column = 0, sticky="nsew", padx=(30,0), pady=(0, 30))

        scrollbar = tk.Scrollbar(listbox_frame,
                                 orient= "vertical",
                                 command=self.quoteList.yview)
        self.quoteList.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row = 1, column = 1, sticky="nsew", pady=(0, 30), padx=(0, 30))


        self.CreateButton = ctk.CTkButton(rightFrame,
                                          text = "Crea Nuovo",
                                          font=("Calisto MT", 20, "bold"),
                                          width=250,
                                          corner_radius=10,
                                          fg_color="white",
                                          border_color="#000534",
                                          border_width=2,
                                          text_color="#000534",
                                          command = lambda: (controller.mostra_frame("QuoteCreate"), controller.frames["QuoteCreate"].fill_user()))
        self.CreateButton.grid(row = 2, column = 0, pady = (200, 50), sticky="ns")

        self.ViewButton = ctk.CTkButton(rightFrame,
                                    text = "Visualizza Preventivo",
                                    font=("Calisto MT", 20, "bold"),
                                    width=250,
                                    corner_radius=10,
                                    fg_color="white",
                                    border_color="#000534",
                                    border_width=2,
                                    text_color="#000534",
                                    command = lambda: self.view_func())
        self.ViewButton.grid(row = 4, column = 0, pady = (20, 50), sticky="ns")

        self.switch_btn_var = tk.BooleanVar()
        self.switch_btn_var.set(False)
        self.ViewConfirmedButton = ctk.CTkSwitch(rightFrame, text = "Visualizza Confermati", font=("Calisto MT", 18, "bold"),  text_color= "#000534" , variable = self.switch_btn_var, command = lambda: self.switch_list_quote_view())
        self.ViewConfirmedButton.grid(row = 1, column = 2, padx = (15, 0), pady = 5)


        self.fill_quote_listbox_not_confirmed()

        self.quoteList.bind("<<ListboxSelect>>", self.on_quote_selected)

    def fill_quote_listbox_confirmed(self):
        self.quoteList.delete(0, tk.END)
        for quote in gv.quote_list:


            if quote.Confirmed:
                self.quoteList.insert(tk.END, f"{quote.id} | {quote.Client.FirstName} {quote.Client.LastName} - {quote.Vehicle.model.brand} {quote.Vehicle.model.name}")

    def fill_quote_listbox_not_confirmed(self):
        self.quoteList.delete(0, tk.END)
        for quote in gv.quote_list:
            if not quote.Confirmed:
                self.quoteList.insert(tk.END,f"{quote.id} | {quote.Client.FirstName} {quote.Client.LastName} - {quote.Vehicle.model.brand} {quote.Vehicle.model.name}")




    def on_quote_selected(self, event = None):
        if event:
            widget = event.widget
            self.selected_quote_index = widget.curselection()
        else:
            self.selected_quote_index = self.quoteList.curselection()

        if self.selected_quote_index:
            self.selected_quote_index = self.selected_quote_index[0]
            value = self.quoteList.get(self.selected_quote_index)
            gv.CurrentQuote = gv.quote_recovery(value.split()[0])
            #self.controller.frames["QuoteView"].fill_quote_info()

    def view_func(self):
        self.controller.frames["QuoteView"].fill_quote_info()
        if gv.CurrentQuote:
            self.controller.mostra_frame("QuoteView")


    def switch_list_quote_view(self):
        value = self.switch_btn_var.get()
        if value:
            self.fill_quote_listbox_confirmed()
        else:
            self.fill_quote_listbox_not_confirmed()
