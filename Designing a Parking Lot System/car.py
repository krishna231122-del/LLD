from Vehicle_Size import VehicleSize
from vehicle import Vehicle

class Car(Vehicle):
     def __init__(self, license_plate: str):
          super().__init__(license_plate, VehicleSize.MEDIUM)