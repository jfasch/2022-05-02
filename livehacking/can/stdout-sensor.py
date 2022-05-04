import sensors
import time


interval = 3
my_sensor = sensors.RandomSensor(0, 100000)

while True:
    print(my_sensor.get_temperature())
    time.sleep(interval)
