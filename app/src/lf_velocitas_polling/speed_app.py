# Copyright (c) 2022 Robert Bosch GmbH and Microsoft Corporation
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0

from sdv.vdb.reply import DataPointReply
from sdv.vehicle_app import VehicleApp
from vehicle import Vehicle, vehicle  # type: ignore


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
