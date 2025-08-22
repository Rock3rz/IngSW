from enum import Enum
from typing import Optional



class FuelType(Enum):
    CNG = 1
    DIESEL = 2
    ELECTRIC = 3
    GASOLINE = 4
    GPL = 5
    HYBRID = 6


'''class Brand(Enum):
    TOYOTA = "Toyota"
    MERCEDES_BENZ = "Mercedes-Benz"
    BMW = "BMW"
    TESLA = "Tesla"
    HONDA = "Honda"
    HYUNDAI = "Hyundai"
    AUDI = "Audi"
    PORSCHE = "Porsche"
    VOLKSWAGEN = "Volkswagen"
    FORD = "Ford"
    NISSAN = "Nissan"
    KIA = "Kia"
    FIAT = "Fiat"
    SEAT = "Seat"
    CUPRA = "Cupra"
    OPEL = "Opel"
'''

class Model:
    def __init__(self, brand:str ,name:str,  displacement: float, hp: int, model_id: int):
        self.brand = brand
        self.name = name
        self.displacement = displacement
        self.hp = hp
        self.model_id = model_id


class Vehicle:
    def __init__(
        self,
        #brand: Brand,
        model: Model,
        registration_year: int,
        color: str,
        fuel_type: FuelType,
        vehicle_id: int,  # URL o path locale?
        is_available: bool,
        km: float,
        number_plate : str,
        price: float,
        image: Optional[str] = None,
        sold: bool = False,
    ):
        #self.brand = brand
        self.registration_year = registration_year
        self.color = color
        self.fuel_type = fuel_type
        self.vehicle_id = vehicle_id
        self.image = image
        self.is_available = is_available
        self.km = km
        self.model = model
        self.number_plate = number_plate
        self.price = price
        self.sold = sold


