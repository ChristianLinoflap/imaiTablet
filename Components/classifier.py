import cv2
import numpy as np
import os
from keras.preprocessing import image
import tensorflow as tf

class ObjectClassifier:
    def __init__(self, model_path='Components\\model.tflite', label_path='Components\\label.txt'):
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.classify_lite = self.interpreter.get_signature_runner('serving_default')
        self.fgbg = cv2.createBackgroundSubtractorMOG2()
        self.image_directory = "capture"
        self.label_path = label_path

        with open(self.label_path, 'r') as file:
            self.class_names = [line.strip() for line in file.readlines()]

    def create_directory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def load_and_preprocess_image(self, image_path):
        img = tf.keras.preprocessing.image.load_img(image_path, target_size=(180, 180))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        return img_array
    
    def classify_objects(self, frame):
        fgmask = self.fgbg.apply(frame)
        contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)

            if area >= 50000:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                if self.frame_count <= 4:
                    roi = frame[y:y + h, x:x + w]
                    roi_resized = cv2.resize(roi, (180, 180))
                    self.frame_count += 1
                    cv2.imwrite(f"{self.image_directory}/frame_{self.frame_count}.png", roi_resized)
                else:
                    image_paths = [os.path.join(self.image_directory, filename) for filename in os.listdir(self.image_directory)]

                    preprocessed_images = [self.load_and_preprocess_image(image_path) for image_path in image_paths]
                    preprocessed_images_array = np.vstack(preprocessed_images)

                    predictions_lite = self.classify_lite(sequential_1_input=preprocessed_images_array)['outputs']
                    scores_lite = tf.nn.softmax(predictions_lite)

                    for i, image_path in enumerate(image_paths):
                        if 100 * np.max(scores_lite[i]) >= 99:
                            predicted_class = self.class_names[np.argmax(scores_lite[i])]
                            print("Predicted class:", predicted_class)
                            print("Confidence:", 100 * np.max(scores_lite[i]))

                            # After obtaining the predicted_class
                            with open("predicted_class.txt", "w") as file:
                                file.write(predicted_class)

                    self.frame_count = 0

    def run_classifier(self):
        cap = cv2.VideoCapture(1)
        
        desired_width = 640 
        desired_height = 480
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

        self.create_directory(self.image_directory)

        self.frame_count = 0

        while True:
            ret, frame = cap.read()
            self.classify_objects(frame)

            cv2.imshow('Webcam', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

def main():
    classifier = ObjectClassifier()
    classifier.run_classifier()

if __name__ == "__main__":
    main()
