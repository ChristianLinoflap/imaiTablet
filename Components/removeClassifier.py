import time
import pygame
import cv2
import numpy as np
import os
from keras.preprocessing import image
import tensorflow as tf
import threading
from PyQt5 import QtWidgets
from collections import Counter

class RemoveClassifier:
    def __init__(self, model_path='Components\\model.tflite', label_path='Components\\label.txt'):
        pygame.mixer.init()
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.classify_lite = self.interpreter.get_signature_runner('serving_default')
        self.fgbg = cv2.createBackgroundSubtractorMOG2()
        self.image_directory = "captureRemove"
        self.label_path = label_path
        self.frame_count = 0
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.create_directory(self.image_directory)
        with open(self.label_path, 'r') as file:
            self.class_names = [line.strip() for line in file.readlines()]
        self.stop_event = threading.Event()

    def create_directory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def load_and_preprocess_image(self, image_path):
        try:
            img = tf.keras.preprocessing.image.load_img(image_path, target_size=(256, 256))
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            return img_array
        except Exception as e:
            print(f"Error loading image at {image_path}: {e}")
            return None

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
        while not self.stop_event.is_set():
            ret, frame = self.cap.read()
            if frame is None:
                print("Failed to capture frame from the camera.")
                break
            cropped_frame = frame[150:1000, 90:500]
            fgmask = self.fgbg.apply(cropped_frame)
            _, fgmask = cv2.threshold(fgmask, 120, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if self.frame_count > 19:
                self.frame_count = 0
            else:
                self.frame_count += 1
            for contour in contours:
                area = cv2.contourArea(contour)
                if area >= 10000:
                    if self.frame_count >= 20:
                        image_paths = [os.path.join(self.image_directory, filename) for filename in
                                        os.listdir(self.image_directory)]
                        preprocessed_images = [self.load_and_preprocess_image(image_path) for image_path in image_paths]
                        preprocessed_images_array = np.vstack(preprocessed_images)
                        predictions_lite = self.classify_lite(sequential_1_input=preprocessed_images_array)['outputs']
                        scores_lite = tf.nn.softmax(predictions_lite)
                        predicted_classes = []
                        for i, image_path in enumerate(image_paths):
                            if 100 * np.max(scores_lite[i]) >= 90:
                                predicted_class = self.class_names[np.argmax(scores_lite[i])]
                                predicted_classes.append(predicted_class)
                                # print("Predicted class:", predicted_class)
                                # print("Confidence:", 100 * np.max(scores_lite[i]))
                        class_counts = Counter(predicted_classes)
                        if any(count >= 19 for count in class_counts.values()):
                            print("Removed. It is accurate!")
                            for predicted_class, count in class_counts.items():
                                # print(f"{predicted_class}: {count} times")
                                with open("removed_class.txt", "w") as file:
                                    file.write(predicted_class)
                            predicted_classes = []
                            self.frame_count = 0
                            self.play_sound('Assets\\scanned_item.mp3')
                            # Clear all images after accurate scanning
                            for file in os.listdir(self.image_directory):
                                os.remove(os.path.join(self.image_directory, file))
                        else:
                            print("Removed. It is not accurate. Try again!")
                    else:
                        saturated_frame = self.saturate_image(cropped_frame)
                        cv2.imwrite(f"{self.image_directory}/frame_{self.frame_count}.png", saturated_frame)
            cv2.imshow('Removed Original Frames', cropped_frame)
            cv2.imshow('Removed Original Frame', fgmask)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop_classifier()
                break

    def pause_scanning(self):
        self.stop_event.set()
        print("Removed Pausing started.")
        
    def resume_scanning(self):
        self.stop_event.clear()
        threading.Thread(target=self.run_classifier).start()
        print("Removed Scanning started.")

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
    classifier = RemoveClassifier()
    classifier.run_classifier()

if __name__ == "__main__":
    main()