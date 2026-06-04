# VisionTrack - Smart Glasses, Smarter Driving

An AI-powered computer vision application built to assist with night blindness detection and enhanced visual perception. Developed and presented at TechSolstice 2024 under the Pitch Tank event.

## About the Project

VisionTrack uses real-time object detection and image enhancement techniques to improve visibility in low-light or high-glare conditions — simulating assistive smart glasses technology.

## Features

- **Contrast Enhancement** — improves visibility in dark/low-light conditions using CLAHE
- **Glare Reduction** — reduces harsh lighting using adaptive thresholding
- **Object Detection** — detects objects in real-time using YOLOv8
- **Side-by-side Comparison** — shows original vs processed frame live
- **Video Recording** — option to save the processed output as a video file

## Built With

- Python
- OpenCV (cv2)
- YOLOv8 (Ultralytics)
- Streamlit (UI)
- PyTorch

## How to Run

1. Install dependencies: pip install -r requirements.txt
2. Download yolov8n.pt from Ultralytics and place in the root folder
3. Run: streamlit run main.py

## Note

This project was built as a proof of concept for assistive vision technology aimed at helping people with night blindness.
