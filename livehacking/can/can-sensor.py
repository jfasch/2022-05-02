import can
import sensors

import sys
import time


ifacename = sys.argv[1]
can_id = int(sys.argv[2])
interval_secs = float(sys.argv[3])
sensor_type = sys.argv[4]

can_socket = can.create_can_socket(ifacename)

if sensor_type == 'cyclic':
    my_sensor = sensors.CyclicSensor([
        24000,
        24500,
        25000,
        25500,
        26000,
        26500,
    ])
elif sensor_type == 'random':
    my_sensor = sensors.RandomSensor(start=20000, end=30000)
else:
    print('error: no such sensor type:', sensor_type)
    sys.exit(1)

while True:
    mc = my_sensor.get_temperature()

    payload = can.format_temperature(mc)
    assert len(payload) == 4

    can.send_frame(can_socket, can_id, payload)
    
    time.sleep(interval_secs)
