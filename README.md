# Garbage_Detection_Recognition

# Overview

This project is a Garbage Detection and Recognition System that utilizes YOLO (You Only Look Once) object detection and image segmentation techniques to classify and identify waste materials in images and videos. The system is built using Python, OpenCV, and Tkinter for an interactive graphical interface.

# Features

Real-Time Detection: Detect and classify garbage types using the YOLO model.

Image Segmentation: Extract region-based descriptors for better classification.

Video Processing: Analyze and detect waste materials in uploaded videos.

Live Camera Detection: Identify waste materials using a webcam.

Interactive GUI: Built with Tkinter for easy user interaction.

Region-Based Descriptor Extraction: Highlights detected waste regions.

# Technologies Used

Python

Tkinter (GUI Library)

OpenCV (Computer Vision Library)

YOLO (Deep Learning Model for Object Detection)

Supervision (for object detection analysis)

Scikit-Image (for region-based descriptors)

PIL (Image Processing)

# Installation

Clone the repository:

git clone https://github.com/yourusername/garbage-detection.git
cd garbage-detection

Install dependencies:

pip install -r requirements.txt

Ensure you have the YOLO model (best_29cls.pt) in the project directory.

# Run the application:

python main.py

# Usage

Click Live Detection to detect garbage through a webcam.

Click Upload Video to analyze a video for garbage classification.

Click About to learn more about the project.

Click Exit to close the application.

# Model Details

The project uses a pre-trained YOLO model (best_29cls.pt) to classify garbage into different types.

Image segmentation is applied using Gaussian blur and Otsu’s thresholding.

Region-based descriptors are extracted to enhance detection accuracy.

# Screenshots

![Image](https://github.com/user-attachments/assets/2ef81aff-bdd9-4be3-8ca7-df7d154e529a)


# Future Improvements

Train a custom YOLO model for improved accuracy.

Integrate a database to store detection results.

Deploy as a web application.

Add mobile support for real-time waste classification.

# Contributors

Krish Khandelwal(project developer)

Open for contributions! Feel free to submit pull requests.
