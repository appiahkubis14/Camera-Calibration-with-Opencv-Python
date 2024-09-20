import plotly.express as px
from PIL import Image
import cv2
import os
import numpy as np

def display_images_with_plotly(input_folder, mtx, dist):
    # List all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    for filename in image_files:
        # Load each image
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)

        if image is not None:
            # Undistort the image
            undistorted_image = cv2.undistort(np.array(image), mtx, dist, None)

            # Create Plotly figure for distorted and undistorted images
            fig = px.imshow(image)
            fig.update_layout(title=f'Distorted Image: {filename}')
            fig.show()

            fig_undistorted = px.imshow(undistorted_image)
            fig_undistorted.update_layout(title=f'Undistorted Image: {filename}')
            fig_undistorted.show()

input_folder =  r'C:\Users\Samuel\Desktop\CODES\PYTHON\progress project\references\Basic-Augmented-reality-course-opencv\CAMERA_CALIBARTION\distorted_images' 
output_folder = r'C:\Users\Samuel\Desktop\CODES\PYTHON\progress project\references\Basic-Augmented-reality-course-opencv\CAMERA_CALIBARTION\undistoted_images'
calibration_data = np.load(r'C:\Users\Samuel\Desktop\CODES\PYTHON\progress project\references\Basic-Augmented-reality-course-opencv\calib_data\MultiMatrix.npz')

mtx = calibration_data['camMatrix']
dist = calibration_data['distCoef']


# Display images with interactive plots using Plotly
display_images_with_plotly(input_folder, mtx, dist)
