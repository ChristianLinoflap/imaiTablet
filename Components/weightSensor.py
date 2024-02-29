import serial
import time
import re

class WeightSensor:
    def __init__(self):
        # self.port = 'COM3'
        # self.baudrate = 9600
        # self.timeout = 1

        self.prev_weight = 0
        self.last_print_time = time.time()
        self.put_item = False
        self.remove_item = False

    def monitor_serial(self, port, baudrate, timeout):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        while True:
            if self.ser.in_waiting > 0:
                line = self.ser.readline().decode('utf-8').rstrip()
                filtered_line = re.sub(r'Weight: ', '', line)
                try:
                    initial_weight = int(filtered_line)
                    if initial_weight > self.prev_weight:
                        self.put_item = True
                        self.remove_item = False
                        hello = self.is_item_added()
                        print("added", hello)
                        self.last_print_time = time.time()
                    elif initial_weight < self.prev_weight:
                        self.remove_item = True
                        self.put_item = False
                        print("removed", self.remove_item)
                        hello = self.is_item_removed()
                        self.last_print_time = time.time()
                    self.prev_weight = initial_weight
                except ValueError:
                    print("Calibrating")
            else:
                if time.time() - self.last_print_time > 2:
                    time.sleep(0.1)
    def is_item_added(self):
        return self.put_item
    
    def is_item_removed(self):
        return self.remove_item

if __name__ == '__main__':
    weight_sensor = WeightSensor()
    weight_sensor.monitor_serial()
