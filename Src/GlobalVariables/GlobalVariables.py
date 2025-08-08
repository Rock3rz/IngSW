import pandas as pd
import os
from tkinter import PhotoImage

isAdminUser = False
canEnter = False

CurrentUser = None
User_file_path = "DB/user.csv"
Clients_file_path = "DB/clients.csv"
user_list = []
client_list = []
CurrentClient = None
