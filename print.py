import board
import busio
import adafruit_sht31d
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c, 0x44)

class TemperatureHumidity:
    def __init__(self):
        return

    def getTemperatureData(self):
        print('Temp = {:.1f} \u00b0C'.format(sensor.temperature))
        return

    def getHumidityData(self):
        print('RH = {:.1f} %\n'.format(sensor.relative_humidity))
        return

TandH = TemperatureHumidity()

TandH.getTemperatureData()
TandH.getHumidityData()
