import pandas as pd

isAdminUser = False
canEnter = False

CurrentUser = None
User_file_path = "DB/user.csv"
Clients_file_path = "DB/clients.csv"
user_list = []
client_list = []
CurrentClient = None