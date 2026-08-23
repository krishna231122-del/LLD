from Vehicle_Size import VehicleSize
from vehicle import Vehicle
class Truck(Vehicle):
     def __init__(self, license_plate:str):
          super().__init__(license_plate, VehicleSize.LARGE)