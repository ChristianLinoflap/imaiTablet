import serial
import time
import re
from collections import Counter

class WeightSensor:
    def __init__(self):
        self.prev_weight = 0
        self.last_print_time = time.time()
        self.put_item = False
        self.remove_item = False
  
    def monitor_serial(self, port, baudrate, timeout):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        initial_weight = 0
        weight = []
        frame = 0
        filtered_weight = 0
        while True:
            try:  
                if self.ser.in_waiting > 0:
                    line = self.ser.readline().decode('utf-8').rstrip()
                    filtered_line = re.sub(r'Weight: ', '', line)
                    initial_weight = int(filtered_line)
                    frame = 0
                    
                time.sleep(0.1)
                if frame == 10:
                    filtered_weight = initial_weight
                    frame = 0
                else:    
                    frame += 1
                if filtered_weight > self.prev_weight:
                    self.put_item = True
                    self.remove_item = False
                    print("added", filtered_weight)
                    
                elif filtered_weight < self.prev_weight:
                    self.remove_item = True
                    self.put_item = False
                    print("removed", filtered_weight)
                self.prev_weight = filtered_weight
            except Exception as e:
                print("Calibrating")
           

    def is_item_added(self):
        return self.put_item

    def is_item_removed(self):
        return self.remove_item


if __name__ == '__main__':
    weight_sensor = WeightSensor()
    weight_sensor.monitor_serial()
