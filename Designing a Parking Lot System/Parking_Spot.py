import threading
from Vehicle_Size import VehicleSize
from vehicle import Vehicle


class ParkingSpot:
    def __init__(self, spot_id: str, size: VehicleSize):
        self.spot_id = spot_id
        self.size = size
        self.is_occupied = False
        self.vehicle = None
        self.lock = threading.Lock()

    def get_spot_id(self) -> str:
        return self.spot_id

    def get_size(self) -> VehicleSize:
        return self.size

    def is_available(self) -> bool:
        with self.lock:
            return not self.is_occupied

    def is_occupied_spot(self) -> bool:
        return self.is_occupied

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        with self.lock:
            if self.is_occupied:
                return False

            if not self.can_fit_vehicle(vehicle):
                return False

            self.vehicle = vehicle
            self.is_occupied = True
            return True

    def unpark_vehicle(self) -> bool:
        with self.lock:
            if not self.is_occupied:
                return False

            self.vehicle = None
            self.is_occupied = False
            return True

    def can_fit_vehicle(self, vehicle: Vehicle) -> bool:
        if self.is_occupied:
            return False

        if vehicle.get_size() == VehicleSize.SMALL:
            return True

        elif vehicle.get_size() == VehicleSize.MEDIUM:
            return self.size in (
                VehicleSize.MEDIUM,
                VehicleSize.LARGE
            )

        elif vehicle.get_size() == VehicleSize.LARGE:
            return self.size == VehicleSize.LARGE

        return False