import cv2
import numpy as np
import os
from keras.preprocessing import image
import tensorflow as tf

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def load_and_preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(180, 180))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def main():
    cap = cv2.VideoCapture(0)

    TF_MODEL_FILE_PATH = r'Components\\model.tflite'
    interpreter = tf.lite.Interpreter(model_path=TF_MODEL_FILE_PATH)
    classify_lite = interpreter.get_signature_runner('serving_default')
    fgbg = cv2.createBackgroundSubtractorMOG2()

    create_directory("capture")

    frame_count = 0

    predictions_count = 'Components\\label.txt'
    with open(predictions_count, 'r') as file:
        class_names = [line.strip() for line in file.readlines()]

    while True:
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)
        contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)

            if area >= 50000:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                if frame_count <= 4:
                    roi = frame[y:y + h, x:x + w]
                    roi_resized = cv2.resize(roi, (180, 180))
                    frame_count += 1
                    cv2.imwrite(f"capture/frame_{frame_count}.png", roi_resized)
                else:
                    image_directory = "capture"
                    image_paths = [os.path.join(image_directory, filename) for filename in os.listdir(image_directory)]

                    preprocessed_images = [load_and_preprocess_image(image_path) for image_path in image_paths]
                    preprocessed_images_array = np.vstack(preprocessed_images)

                    predictions_lite = classify_lite(sequential_1_input=preprocessed_images_array)['outputs']
                    scores_lite = tf.nn.softmax(predictions_lite)

                    for i, image_path in enumerate(image_paths):
                        if 100 * np.max(scores_lite[i]) >= 99:
                            predicted_class = class_names[np.argmax(scores_lite[i])]
                            print("Predicted class:", predicted_class)
                            print("Confidence:", 100 * np.max(scores_lite[i]))
                            
                            # After obtaining the predicted_class
                            with open("predicted_class.txt", "w") as file:
                                file.write(predicted_class)

                    frame_count = 0

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()