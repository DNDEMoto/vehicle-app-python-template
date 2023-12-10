
from sdv.vehicle_app import VehicleApp
from vehicle import Vehicle, vehicle
from sdv.vdb.reply import DataPointReply

class SpeedApp(VehicleApp):
    """Array Datatype example Vehicle App"""
    speed = 0
    def __init__(self, vehicle: Vehicle):
        super().__init__()
        self.Vehicle = vehicle

    def get_speed(self) -> float:
        return self.speed
    
    def print_values(self, data: DataPointReply):
        self.speed = data.get(self.Vehicle.Speed).value
        print("velocitas: Vehicle Speed: {}".format(self.speed))
        
    async def on_start(self):
        """Run when the vehicle app starts"""
        await self.Vehicle.Speed.subscribe(self.print_values)


def instantiate() -> SpeedApp:
    print("velocitas: instantiate SpeedApp")
    return SpeedApp(vehicle)