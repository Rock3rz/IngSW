from enum import Enum
from typing import Optional


class FuelType(Enum):
    CNG = 1
    DIESEL = 2
    ELECTRIC = 3
    GASOLINE = 4
    GPL = 5
    HYBRID = 6


class Brand:
    def __init__(self, brand_id: int, name: str):
        self.brand_id = brand_id
        self.name = name


class Model:
    def __init__(self, displacement: float, hp: int, model_id: int):
        self.displacement = displacement
        self.hp = hp
        self.model_id = model_id


class Vehicle:
    def __init__(
        self,
        brand: Brand,
        registration_year: int,
        color: str,
        fuel_type: FuelType,
        vehicle_id: int,
        image: Optional[str],  # URL o path locale?
        is_available: bool,
        km: float,
        model: Model,
        price: float
    ):
        self.brand = brand
        self.registration_year = registration_year
        self.color = color
        self.fuel_type = fuel_type
        self.vehicle_id = vehicle_id
        self.image = image
        self.is_available = is_available
        self.km = km
        self.model = model
        self.price = price
