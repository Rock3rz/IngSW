from datetime import datetime
from Src.Class.User import User

class Appointment:
    def __init__(
        self,
        description: str,
        date_time: datetime,
        user: User
    ):
        self.description = description
        self.date_time = date_time
        self.user = user
