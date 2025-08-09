import pandas as pd
import os
from tkinter import PhotoImage

isAdminUser = False
canEnter = False

CurrentUser = None

#Indirizzi database
User_file_path = "DB/user.csv"
Clients_file_path = "DB/clients.csv"
Brand_file_path = "DB/brand.csv"

user_list = []
client_list = []
brand_list = []
model_list = []

CurrentClient = None

CurrentBrand = None

