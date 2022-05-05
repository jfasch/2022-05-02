import sensors
import time
import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interval', type=float, help='interval in which to ask the sensor for samples (in seconds)')
parser.add_argument('-s', '--start', type=int, help='start of the random range')
parser.add_argument('-e', '--end', type=int, help='end of the random range')

args = parser.parse_args()

interval = args.interval
start = args.start
end = args.end

if start >= end:
    print(f'start ({start}) must be less than end ({end})', file=sys.stderr)
    sys.exit(1)

my_sensor = sensors.RandomSensor(start, end)

try:
    while True:
        print(my_sensor.get_temperature())
        time.sleep(interval)
except KeyboardInterrupt:
    pass
