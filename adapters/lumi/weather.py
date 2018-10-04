from adapters.base_adapter import Adapter
from devices.temperature_sensor import TemperatureSensor
from devices.humidity_sensor import HumiditySensor
from devices.pressure_sensor import PressureSensor

class Weather(Adapter):
    def __init__(self, devices):
        super().__init__(devices)
        self.devices.append(TemperatureSensor(devices, 'temperature', 'temperature'))
        self.devices.append(HumiditySensor(devices, 'humidity', 'humidity'))
        self.devices.append(PressureSensor(devices, 'pressure', 'pressure'))
                