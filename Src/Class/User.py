from typing import List
from Vehicle import Vehicle


class User:
    def __init__(
        self,
        email: str,
        first_name: str,
        user_id: int,
        is_admin: bool,
        last_name: str,
        password:str,
        searched_vehicles: List[Vehicle],
    ):

        self.email = email
        self.firstName = first_name
        self.ID = user_id
        self.isAdmin = is_admin
        self.LastName = last_name
        self.Password = password
        self.SearchedVehicles = searched_vehicles

