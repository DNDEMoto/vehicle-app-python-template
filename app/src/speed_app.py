
from sdv.vehicle_app import VehicleApp
from vehicle import Vehicle, vehicle
from sdv.vdb.reply import DataPointReply
import logging
import asyncio
import signal

class SpeedApp(VehicleApp):
    """Array Datatype example Vehicle App"""
    speed = 0
    def __init__(self, vehicle: Vehicle):
        super().__init__()
        self.Vehicle = vehicle

    def get_speed(self) -> float:
        return self.speed
    
    def print_values(self, data: DataPointReply):
        speed = data.get(self.Vehicle.Speed).value
        print("velocitas: Vehicle Speed: {}".format(speed))
        
    async def on_start(self):
        """Run when the vehicle app starts"""
        await self.Vehicle.Speed.subscribe(self.print_values)

async def main():
    print("velocitas: speed app main")
    speed_app = SpeedApp(vehicle)
    await speed_app.run()

#
# LOOP = asyncio.get_event_loop()
# LOOP.add_signal_handler(signal.SIGTERM, LOOP.stop)
# LOOP.run_until_complete(main())
# LOOP.close()
