from datetime import datetime
from User import User
#from Client import Client

class Appointment:
    def __init__(
        self,
        client: str,
        date_time: datetime,
        user: User
    ):
        self.client = client
        self.date_time = date_time
        self.user = user
