import tkinter as tk
from tkinter import messagebox
import pandas as pd
from Src.Controllers.AccountController import AccountController
import Src.GlobalVariables.GlobalVariables as gv

from Src.Gui.VehicleSectionClass import VehicleSection
from Src.Gui.AppointmentSectionClass import AppointmentSection
from Src.Gui.QuoteSectionClass import QuoteSection
from Src.Gui.ClientSectionClass import ClientSection
from Src.Gui.ManageUserSectionClass import CreateUserSection
from Src.Gui.PersonalUserSectionClass import UserSection
from Src.Gui.LoginFrameClass import LoginFrame
from Src.Gui.MainMenuClass import MainMenu
from Src.Gui.CreateClientSectionClass import CreateClientSectionClass
from Src.Gui.ViewClientSection import ViewClient

class Gui:

    def __init__(self, root):
        self.root = root

        self.container = tk.Frame(root)
        self.container.grid(row = 0, column = 0, sticky="nsew")

        self.frames = {}

        #Ciclo che carica in memoria i vari frame
        for F in (
            MainMenu,
            UserSection,
            VehicleSection,
            ClientSection,
            QuoteSection,
            AppointmentSection,
            LoginFrame,
            CreateUserSection,
            CreateClientSectionClass,
            ViewClient
            ):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")

        self.mostra_frame("LoginFrame")

    ##Funzione che carica nella gui il frame passato come parametro
    def mostra_frame(self, nome_frame):
        frame = self.frames[nome_frame]
        frame.tkraise()


