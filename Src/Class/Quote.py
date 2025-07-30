from Client import Client
from Vehicle import Vehicle
from User import User
from datetime import date

class Quote:
    def __init__(
        self,
        client: Client,
        confirmed: bool,
        end_date: date ,
        quote_id: int,
        start_date: date,
        user: User,
        vehicle: Vehicle
    ):
        self.Client = client
        self.Confirmed = confirmed
        self.EndDate = end_date
        self.id = quote_id
        self.StarDate = start_date
        self.User = user
        self.Vehicle =vehicle