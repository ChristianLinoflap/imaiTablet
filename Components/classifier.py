import time
import pygame
import cv2
import numpy as np
import os
import threading
from PyQt5 import QtWidgets
import requests

class ObjectClassifier:
    def __init__(self):
        pygame.mixer.init()
        pygame.display.set_caption('')
        self.fgbg = cv2.createBackgroundSubtractorMOG2()
        self.image_directory = "capture"
        self.frame_count = 0
        self.cap = cv2.VideoCapture(0)
        self.create_directory(self.image_directory)
        self.stop_event = threading.Event()
        threading.Thread(target=self.run_classifier).start()

    def create_directory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def saturate_image(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv[:, :, 1] = np.clip(hsv[:, :, 1] * 1.5, 0, 255).astype(np.uint8)
        saturated_frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        return saturated_frame

    def is_intersect(self, rect1, rect2):
        return not (rect1[2] < rect2[0] or rect1[0] > rect2[2] or rect1[3] < rect2[1] or rect1[1] > rect2[3])

    def play_sound(self, sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
        time.sleep(2)

    def run_classifier(self):
        self.predicted_classes = []
        while not self.stop_event.is_set():
            ret, frame = self.cap.read()
            cropped_frame = frame[150:1000, 90:500]
            fgmask = self.fgbg.apply(cropped_frame)
            _, fgmask = cv2.threshold(fgmask, 120, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            files = []

            saturated_frame = self.saturate_image(cropped_frame)
            cv2.imwrite(f"capture/frame.png", saturated_frame)
            url = 'http://192.168.254.102:5000/upload2'
            image_paths = [os.path.join("capture", filename) for filename in os.listdir("capture")]
            for image_file in image_paths:

                if os.path.exists(image_file):
                    with open(image_file, 'rb') as f:
                        file_data = f.read()
                        files.append(('files[]', (os.path.basename(image_file), file_data, 'image/png')))
                else:
                    print(f"File not found: {image_file}")
            start_time = time.perf_counter()

            if not os.path.exists("predicted_class.txt"):
                if files:
                    try:
                        response = requests.post(url, files=files)
                        print(response.text)
                        if '<' in response.text or 'pass' in response.text:
                            print("'< found in response text.")
                        else:
                            with open("predicted_class.txt", "w") as file:
                                file.write(response.text)
                    except Exception as e:
                        print(f"Error occurred: {e}")
                else:
                    print("No files to upload.")
                end_time = time.perf_counter()
                elapsed_time = end_time - start_time
                print("Elapsed time: ", elapsed_time)

            cv2.imshow('Original Frame', frame)
            cv2.imshow('Motion Detection', fgmask)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop_classifier()
                break

    def pause_scanning(self):
        self.stop_event.set()
        print("Pausing started.")

    def resume_scanning(self):
        self.stop_event.clear()
        threading.Thread(target=self.run_classifier).start()
        print("Scanning started.")

    def stop_classifier(self):
        try:
            self.stop_event.set()
            if hasattr(self, 'cap') and self.cap.isOpened():
                self.cap.release()
            cv2.destroyAllWindows()
        except Exception as e:
            error_message = f"An unexpected error occurred while stopping the classifier: {e}"
            print(error_message)
            QtWidgets.QMessageBox.critical(None, "Error", error_message)

def main():
    classifier = ObjectClassifier()
    classifier.run_classifier()

if __name__ == "__main__":
    main()