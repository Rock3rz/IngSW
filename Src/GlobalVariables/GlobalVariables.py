import pandas as pd

isAdminUser = False
canEnter = False

CurrentUser = pd.Series(dtype = object)
User_file_path = "DB/user.csv"