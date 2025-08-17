import pandas as pd
import os
import Src.GlobalVariables.GlobalVariables as gv
from Src.Class.Client import Client
from Src.Class.User import User
from Src.Class.Vehicle import Model, Vehicle
from Src.Class.Appointment import Appointment
from datetime import datetime
from Src.Class.User import User
from Src.GlobalVariables.GlobalVariables import api_controller, appointment_list


class APIController:
    def __init__(self):
        if os.path.exists(gv.User_file_path):
            self.df = pd.read_csv(gv.User_file_path)
            self.refresh_user_list()

        else:
            self.df = pd.DataFrame()

        if os.path.exists(gv.Clients_file_path):
            self.df = pd.read_csv(gv.Clients_file_path)
            self.refresh_client_list()
        else:
            self.df = pd.DataFrame()

        if os.path.exists(gv.Brand_file_path):
            self.df = pd.read_csv(gv.Brand_file_path)
            self.refresh_brand_list()
        else:
            self.df = pd.DataFrame()

        if os.path.exists(gv.Model_file_path):
            self.df = pd.read_csv(gv.Model_file_path)
            self.refresh_model_list()
        else:
            self.df = pd.DataFrame()

        if os.path.exists(gv.Vehicle_file_path):
            self.df = pd.read_csv(gv.Vehicle_file_path)
            self.refresh_vehicle_list()
        else:
            self.df = pd.DataFrame()
        if os.path.exists(gv.Appointment_file_path):
            self.df = pd.read_csv(gv.Appointment_file_path)
            self.refresh_appointment_list()
        else:
            self.df = pd.DataFrame()

    @staticmethod
    def refresh_user_list():
        if os.path.exists(gv.User_file_path):
            df = pd.read_csv(gv.User_file_path)
            #svuoto la lista prima di ricaricarla sennò ottengo delle copie
            gv.user_list.clear()

            for _, row in df.iterrows():
                gv.user_list.append(User(
                    user_id=int(row["ID"]),
                    email=str(row["Email"]),
                    first_name=str(row["Name"]),
                    username=str(row["UserName"]),
                    is_admin=bool(row["IsAdmin"]),
                    last_name=str(row["LastName"]),
                    password=str(row["Password"]),
                ))

    @staticmethod
    def write_user_on_csv():
        data = []
        for user in gv.user_list:
            data.append({
                "ID" : user.user_id,
                "Name": user.firstName,
                "LastName" : user.LastName,
                "Email": user.email,
                "UserName" : user.username,
                "Password" : user.Password,
                "IsAdmin" : user.isAdmin,
            })
        df = pd.DataFrame(data)
        df.to_csv(gv.User_file_path, index = False)
        APIController.refresh_user_list()


    @staticmethod
    def refresh_client_list():
        if os.path.exists(gv.Clients_file_path):
            df = pd.read_csv(gv.Clients_file_path)

            #svuoto la lista
            gv.client_list.clear()

            for _, row in df.iterrows():
                gv.client_list.append(Client(
                    client_id = int(row["Client_ID"]),
                    first_name=str(row["First_Name"]),
                    last_name=str(row["Last_Name"]),
                    email=str(row["Email"]),
                    phone_number= int(row["PhoneNumber"]),
                    city=str(row["Address"]),
                    postal_code=int(row["PostalCode"]),

                ))

    @staticmethod
    def write_client_on_csv():
        data = []
        for client in gv.client_list:
            data.append({
                "Client_ID": client.ID,
                "First_Name": client.FirstName,
                "Last_Name": client.LastName,
                "Email": client.email,
                "PhoneNumber": client.PhoneNumber,
                "Address": client.city,
                "PostalCode": client.PostalCode,
            })
        df = pd.DataFrame(data)
        df.to_csv(gv.Clients_file_path, index=False)
        APIController.refresh_client_list()


    @staticmethod
    def refresh_brand_list():
        if os.path.exists(gv.Brand_file_path):
            df = pd.read_csv(gv.Brand_file_path)

            #svuoto la lista
            gv.brand_list.clear()
            for _, row in df.iterrows():
                gv.brand_list.append(str(row["Brand"]))

    @staticmethod
    def write_brand_on_csv():
        data = []
        for brand in gv.brand_list:
            data.append({
                "Brand": brand
            })
        df = pd.DataFrame(data)
        df.to_csv(gv.Brand_file_path, index = False)
        APIController.refresh_brand_list()


    @staticmethod
    def refresh_model_list():
        if os.path.exists(gv.Model_file_path):
            df = pd.read_csv(gv.Model_file_path)
            gv.model_list.clear()
            for _, row in df.iterrows():
                gv.model_list.append(
                    Model(
                        model_id=int(row["Model_ID"]),
                        brand=str(row["Brand"]),
                        name=str(row["Model"]),
                        displacement=float(row["Displacement"]),
                        hp=int(row["HP"])
                    )
                )

    @staticmethod
    def write_model_on_csv():
        data = []
        for model in gv.model_list:
            data.append({
                "Model_ID": model.model_id,
                "Brand": model.brand,
                "Model": model.name,
                "Displacement": model.displacement,
                "HP": model.hp
            })
        df = pd.DataFrame(data)
        df.to_csv(gv.Model_file_path,index=False)
        APIController.refresh_model_list()


    @staticmethod
    def refresh_vehicle_list():
        if os.path.exists(gv.Vehicle_file_path):
            df = pd.read_csv(gv.Vehicle_file_path)
            gv.vehicle_list.clear()
            for _, row in df.iterrows():
                image_path = None
                if "Image" in df.columns:
                    try:
                        val = row["Image"]
                        if isinstance(val, str) and val.strip():
                            image_path = val.strip()
                    except Exception:
                        image_path = None
                gv.vehicle_list.append(
                    Vehicle(
                        model=gv.model_recovery(int(row["Model ID"])),
                        registration_year=int(row["Year"]),
                        color=str(row["Color"]),
                        fuel_type=str(row["Fuel Type"]),
                        vehicle_id=int(row["Vehicle ID"]),
                        is_available=bool(row["Is Available"]),
                        km=float(row["Km"]),
                        number_plate=str(row["Number Plate"]),
                        price=float(row["Price"]),
                        image=image_path
                    )
                )

    @staticmethod
    def write_vehicle_on_csv():
        data = []
        for vehicle in gv.vehicle_list:
            data.append({
                "Vehicle ID": vehicle.vehicle_id,
                "Model ID": vehicle.model.model_id,
                "Year": vehicle.registration_year,
                "Color": vehicle.color,
                "Fuel Type": vehicle.fuel_type,
                "Is Available": vehicle.is_available,
                "Km": vehicle.km,
                "Number Plate": vehicle.number_plate,
                "Price": vehicle.price,
                "Image": vehicle.image if vehicle.image else ""
            })
        df = pd.DataFrame(data)
        df.to_csv(gv.Vehicle_file_path, index = False)
        APIController.refresh_vehicle_list()


    @staticmethod
    def refresh_appointment_list():
        if os.path.exists(gv.Appointment_file_path):
            df = pd.read_csv(gv.Appointment_file_path)
            gv.appointment_list.clear()
            for _, row in df.iterrows():
                date_time_str = row["DateTime"]  # esempio: '2025-08-15 08:00:00'
                gv.appointment_list.append(
                    Appointment(description=str(row["Description"]),
                                date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S'),
                                user = gv.user_recovery(int(row["User ID"]))
                    )
                )



    @staticmethod
    def write_appointment_on_csv():
        data = []
        for appointment in gv.appointment_list:
            data.append({
                "DateTime": appointment.date_time,
                "User ID": appointment.user.user_id,
                "Description": appointment.description
            })
        df = pd.DataFrame(data)
        df.to_csv(gv.Appointment_file_path, index=False)
        APIController.refresh_appointment_list()

