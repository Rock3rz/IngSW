from Src.Class.Client import Client
from Src.Class.Vehicle import Vehicle
from Src.Class.User import User
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
        vehicle: Vehicle,
        price: float
    ):
        self.Client = client
        self.Confirmed = confirmed
        self.EndDate = end_date
        self.id = quote_id
        self.StartDate = start_date
        self.User = user
        self.Vehicle = vehicle
        self.Price = price