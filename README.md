# Camera Calibration with OpenCV and Python

## Overview

This project demonstrates how to perform camera calibration using OpenCV and Python. Camera calibration is essential for correcting lens distortion and improving the accuracy of computer vision applications. This repository contains code and instructions for calibrating a camera using checkerboard images, allowing for accurate 3D measurements and improved image quality.

## Table of Contents

1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Technologies Used](#technologies-used)
4. [Features](#features)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Results](#results)
8. [Screenshots](#screenshots)
9. [Contributing](#contributing)
10. [License](#license)

## Introduction

Camera calibration is a process used to estimate the parameters of a camera, including its intrinsic (focal length, optical center) and extrinsic (rotation, translation) parameters. This project utilizes OpenCV's calibration functions to determine these parameters using images of a checkerboard pattern.

## Dataset

To perform camera calibration, you will need a series of images featuring a checkerboard pattern. The checkerboard should have a known number of squares and dimensions. The images should be taken from different angles and distances to provide a comprehensive calibration.

## Technologies Used

- **Python**: The programming language used for implementing the calibration process.
- **OpenCV**: A powerful computer vision library for image processing and camera calibration.
- **NumPy**: A library for numerical computations in Python.

## Features

- **Camera Intrinsics and Extrinsics Calculation**: Calculates and displays the intrinsic and extrinsic parameters of the camera.
- **Distortion Correction**: Applies the calibration parameters to correct lens distortion in images.
- **Visual Feedback**: Displays the original and corrected images for comparison.
- **Checkerboard Detection**: Automatically detects checkerboard corners from the calibration images.

## Installation

1. **Install Python**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **Install Required Libraries**:
   ```bash
   pip install opencv-python numpy
![download](https://github.com/user-attachments/assets/73d52384-f7fe-46ec-89d1-e398b59a73bf){: width="400" height="300"}
