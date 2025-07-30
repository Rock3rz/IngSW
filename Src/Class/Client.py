

class Client:
    def __init__(
        self,
        city: str,
        email: str ,
        first_name: str,
        last_name: str,
        client_id: int,
        phone_number: int,
        postal_code: int
     ):

        self.city = city
        self.email = email
        self.FirstName = first_name
        self.LastName = last_name
        self.ID = client_id
        self.PhoneNumber = phone_number
        self.PostalCode = postal_code