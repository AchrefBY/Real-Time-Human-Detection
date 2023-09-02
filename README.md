# Human Detection

Human Detection is a computer vision project that uses YOLOv3 (You Only Look Once version 3) to detect and draw bounding boxes around humans in real-time video feeds. This repository provides the code and instructions for setting up the environment to perform human detection.

## Installation

Before running the Human Detection system, make sure you have the required dependencies installed:

1. **OpenCV**: Install using `pip install opencv-python`
2. **numpy**: Install using `pip install numpy`

Additionally, you need to download the YOLOv3 weights and configuration files from [https://pjreddie.com/darknet/yolo/](https://pjreddie.com/darknet/yolo/). Place the downloaded "yolov3-spp.weights" and "yolov3-spp.cfg" files in the directory where the Python script exists.

## How It Works

The Human Detection system uses YOLOv3 to perform real-time object detection in video feeds. Here's how it works:

- Load the YOLOv3 weights and configuration files using OpenCV.
- Capture video from the webcam.
- Resize the video frames to match the YOLOv3 input size.
- Prepare the resized frames for detection by converting them into a blob.
- Set the blob as input to the YOLOv3 model.
- Run a forward pass through the model to get the detections.
- Loop through the detections and draw bounding boxes around detected humans.
- Display the output video feed with bounding boxes drawn around humans.

## Usage

To use the Human Detection system, follow these steps:

1. Ensure you have installed the required dependencies and downloaded the YOLOv3 files as described in the "Installation" section.

2. Run the Python script for human detection:

- python human-detection.py

3. The script will start capturing video from your webcam and display it with bounding boxes around detected humans.

4. To quit the application, press "q."

## Folder Structure

- `yolov3-spp.cfg`: YOLOv3 configuration file.
- `yolov3-spp.weights`: YOLOv3 pre-trained weights file.
- `README.md`: This documentation file.
- `human-detection.py`: The main Python script for real-time human detection. It uses YOLOv3 for object detection and OpenCV for video capture and display.

The Human Detection system can be used for various applications, such as security surveillance an
