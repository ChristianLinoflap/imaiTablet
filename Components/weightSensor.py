import serial
import time
import re
from collections import Counter

class WeightSensor:
    def __init__(self):
        # self.port = 'COM5'
        # self.baudrate = 9600
        # self.timeout = 1
        # self.ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        self.prev_weight = 0
        self.last_print_time = time.time()
        self.put_item = False
        self.remove_item = False
        self.same_weight = False
        self.verify = False
    # def monitor_serial(self):
    def monitor_serial(self, port, baudrate, timeout):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        initial_weight = 0
        frame = 0
        filtered_weight = 0
        stored_weight = 0
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
                if abs(self.prev_weight - filtered_weight) <= 20:
                    pass
                else:
                    if filtered_weight > self.prev_weight:
                        self.put_item = True
                        self.remove_item = False
                        print("added", filtered_weight)
                        if self.same_weight:
                            pass
                        elif self.verify:
                            pass
                        else:
                            stored_weight = self.prev_weight
                            print('Stored_weight: ',stored_weight)
                    elif filtered_weight < self.prev_weight:
                        self.remove_item = True
                        self.put_item = False
                        print("removed", filtered_weight)
                        if self.verify:
                            pass
                        elif self.same_weight:
                            pass
                        else:
                            self.same_weight = True
                            stored_weight = self.prev_weight
                            print('Stored_weight: ',stored_weight)
                if abs(stored_weight - filtered_weight) <= 20 and self.same_weight:
                    print('You returned the item!')
                    self.remove_item = False
                    self.same_weight = False
                    self.put_item = False
                    self.verify = False
                elif abs(stored_weight - filtered_weight) <= 20 and self.verify:
                    print('The item was removed')
                    self.remove_item = False
                    self.verify = False
                    self.put_item = False
                    self.same_weight = False
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
