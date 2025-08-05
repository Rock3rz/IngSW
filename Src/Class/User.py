from typing import List
from Src.Class.Vehicle import Vehicle


class User:
    def __init__(
        self,
        user_id: int,
        email: str,
        first_name: str,
        username: str,
        is_admin: bool,
        last_name: str,
        password:str,
        searched_vehicles: List[Vehicle] = None,
    ):

        self.user_id: int = user_id
        self.email = email
        self.firstName = first_name
        self.username = username
        self.isAdmin = is_admin
        self.LastName = last_name
        self.Password = password
        self.SearchedVehicles = searched_vehicles

