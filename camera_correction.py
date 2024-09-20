import numpy as np
import cv2 as cv

calibration_data = np.load(r'C:\Users\Samuel\Desktop\CODES\PYTHON\progress project\references\Basic-Augmented-reality-course-opencv\calib_data\MultiMatrix.npz')

mtx = calibration_data['camMatrix']
dist = calibration_data['distCoef']

import os

def undistort_images_in_folder(input_folder, output_folder, mtx, dist):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    for filename in image_files:
        image_path = os.path.join(input_folder, filename)
        image = cv.imread(image_path)

        if image is not None:
            undistorted_image = cv.undistort(image, mtx, dist, None)

            output_path = os.path.join(output_folder, filename)
            cv.imwrite(output_path, undistorted_image)
            print(f"Undistorted image saved: {output_path}")
        else:
            print(f"Failed to load image: {image_path}")

input_folder =  r'C:\Users\Samuel\Desktop\CODES\PYTHON\progress project\references\Basic-Augmented-reality-course-opencv\CAMERA_CALIBARTION\distorted_images' 
output_folder = r'C:\Users\Samuel\Desktop\CODES\PYTHON\progress project\references\Basic-Augmented-reality-course-opencv\CAMERA_CALIBARTION\undistoted_images'

undistort_images_in_folder(input_folder, output_folder, mtx, dist)
