import time
import pygame
import cv2
import numpy as np
import os
import threading
from PyQt5 import QtWidgets
import requests
import ctypes
from weightSensor import WeightSensor
class ObjectClassifier(ctypes.CDLL):
    def __init__(self, name=None, mode=ctypes.DEFAULT_MODE, handle=None, use_errno=False, use_last_error=False):
        super(ObjectClassifier, self).__init__(r"C:\Users\orqui\OneDrive\Documents\GitHub\imaiTablet\Components\UHFReader86.dll", mode,handle, use_errno, use_last_error)
        self.OpenComPort.restype = ctypes.c_int
        self.OpenComPort.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_byte), ctypes.c_byte,
                                     ctypes.POINTER(ctypes.c_int)]
        # self.SetBeepNotification.restype = ctypes.c_int
        self.SetBeepNotification.argtypes = [ctypes.POINTER(ctypes.c_byte), ctypes.c_byte, ctypes.c_int]
        self.Inventory_G2.argtypes = [
            ctypes.POINTER(ctypes.c_byte),  # byte[] ConAddr
            ctypes.c_int,  # int QValue
            ctypes.c_byte,  # byte Session
            ctypes.c_byte,  # byte MaskMem
            ctypes.POINTER(ctypes.c_byte),  # byte[] MaskAdr
            ctypes.c_int,  # int MaskLen
            ctypes.POINTER(ctypes.c_byte),  # byte[] MaskData
            ctypes.c_byte,  # byte MaskFlag
            ctypes.c_byte,  # byte AdrTID
            ctypes.c_byte,  # byte LenTID
            ctypes.c_byte,  # byte TIDFlag
            ctypes.c_byte,  # byte Target
            ctypes.c_byte,  # byte InAnt
            ctypes.c_byte,  # byte Scantime
            ctypes.c_byte,  # byte Fastflag,
            ctypes.POINTER(ctypes.c_byte),  # byte[] EPClenandEPC,
            ctypes.POINTER(ctypes.c_byte),  # byte[] Ant,
            ctypes.POINTER(ctypes.c_int),  # int[] Totallen,
            ctypes.POINTER(ctypes.c_int),  # int[] CardNum
            ctypes.c_int
        ]
        self.weight_sensor = WeightSensor()
        sample_comm = ctypes.c_byte(255)
        self.sample_handle = ctypes.c_int()
        frm_handle = ctypes.c_int(self.sample_handle.value)
        beep = ctypes.c_byte(0)
        # Simulate the native method call
        sample_recv = self.OpenComPort(3, ctypes.byref(sample_comm), 3, ctypes.byref(self.sample_handle))
        self.SetBeepNotification(ctypes.byref(sample_comm), 2, 3)
        self.SetRfPower(ctypes.byref(sample_comm), 30, 3)
        if sample_recv == 0:
            # Successful case

            print(f"Com port opened successfully. ComAddr: {sample_comm.value}, FrmHandle: {self.sample_handle.value}")
            # Additional code for when the com port is successfully opened
        else:
            # Failure case
            print(f"Failed to open com port. Recv: {sample_recv}")
        pygame.mixer.init()
        pygame.display.set_caption('')
        self.scan_sound = pygame.mixer.Sound("Assets\\scanned_item.mp3")

        self.stop_event = threading.Event()
        threading.Thread(target=self.run_classifier).start()


    def play_sound(self, sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        time.sleep(2)

    def run_classifier(self):
        # Initialize sample values
        com_addr = ctypes.c_byte(255)
        adr_tid = 0
        len_tid = 6
        tid_flag = 0
        target = 0
        in_ant = 0x80
        scan_time = 0
        fast_flag = 1
        u_in_ant = ctypes.c_byte(0)
        u_totallen = ctypes.c_int(1)
        mask_adr = ctypes.c_byte(0)
        EPClenandEPC = ctypes.c_byte(0)
        mask_data = ctypes.c_byte(100)
        mask_flag = 0
        StrBuff = (ctypes.c_byte * 5000)()
        card_num = ctypes.c_int(0)
        frm_handle = ctypes.c_int(self.sample_handle.value)

        # Simulate the native method call
        length = 0
        gg = 0
        EPC = []
        frame = 0
        prev_epcs = set()
        new_epcs = 0
        while True:
            recv = self.Inventory_G2(
                ctypes.byref(com_addr),
                5,
                0,
                1,
                ctypes.byref(mask_adr),
                0,
                ctypes.byref(mask_data),
                mask_flag,
                adr_tid,
                len_tid,
                tid_flag,
                target,
                in_ant,
                scan_time,
                fast_flag,
                StrBuff,
                ctypes.byref(u_in_ant),
                ctypes.byref(u_totallen),
                ctypes.byref(card_num),
                frm_handle
            )
            # Handling the result

            if recv in [1, 2, 3, 4]:
                if card_num.value == 0:
                    result = None
                else:
                    EPC = []
                    m = 0
                    for index in range(card_num.value):
                        epclen = StrBuff[m] & 255
                        m += 1
                        EPCstr = ""
                        epc = bytearray(epclen)
                        for n in range(epclen):
                            bbt = StrBuff[m] & 255
                            m += 1
                            epc[n] = bbt
                            hex_value = format(bbt, '02X')
                            EPCstr += hex_value
                        rssi = StrBuff[m]
                        m += 1
                        EPC.append(EPCstr.upper())
                    length = len(EPC)
                    if card_num.value > 0:
                        # Check if any new RFID values are present
                        new_epcs = set(EPC) - prev_epcs
                        gg = new_epcs
                        prev_epcs.update(new_epcs)
                     
                            # print(length)
                        
                            # Open the file in 'w' (write) mode to overwrite the file
                            # with open("predicted_class.txt", "w") as file:
                            #     # Write each element in EPC with a space in between
                            #     file.write(' '.join(EPC) + '\n')
                        EPC = []
                    # frame = 0
                    time.sleep(1)
            else:
                result = None
                length = len(EPC)
                # print(length)
            if new_epcs:
                # print('This is all', prev_epcs)
                frame = 0
            else:
                pass
            if frame == 10:
                with open("predicted_class.txt", "w") as file:
                    file.write('\n'.join(prev_epcs))
                # print('Finale frame: ',frame)
                frame = 0
            frame += 1
            # print('Frame: ',frame)
            if self.weight_sensor.remove_item:
                prev_epcs = set()
                time.sleep(1)



    def pause_scanning(self):
        self.stop_event.set()
        # print("Pausing started.")

    def resume_scanning(self):
        self.stop_event.clear()
        threading.Thread(target=self.run_classifier).start()
        # print("Scanning started.")

    def stop_classifier(self):
        try:
            self.stop_event.set()

        except Exception as e:
            error_message = f"An unexpected error occurred while stopping the classifier: {e}"
            print(error_message)
            QtWidgets.QMessageBox.critical(None, "Error", error_message)

def main():
    classifier = ObjectClassifier()
    classifier.run_classifier()

if __name__ == "__main__":
    main()