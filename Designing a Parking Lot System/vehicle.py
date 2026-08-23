from abc import ABC, abstractmethod
from Vehicle_Size import VehicleSize

class Vehicle(ABC):
     def __init__(self, license_plate: str, size: VehicleSize):
         self.license_plate = license_plate
         self.size = size    

     def get_license_number(self) -> str:
           return self.license_plate

     def get_size(self) -> VehicleSize:
           return self.size



