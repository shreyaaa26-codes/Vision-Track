import cv2
import numpy as np
import torch
import streamlit as st
from ultralytics import YOLO
import time

# Load the YOLO model for object detection
model = YOLO("yolov8n.pt")  # Using a pre-trained YOLOv8 model

def enhance_contrast(frame):
    """Enhance contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization)"""
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    l = clahe.apply(l)
    enhanced_lab = cv2.merge((l, a, b))
    return cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)

def reduce_glare(frame):
    """Reduce glare using adaptive thresholding"""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresholded = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
    return cv2.inpaint(frame, thresholded, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

def detect_objects(frame):
    """Detect objects using YOLO model and draw bounding boxes."""
    results = model(frame)
    alerts = []
    for result in results:
        for box in result.boxes.xyxy:  # Get bounding boxes
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            alerts.append("Object Detected!")
    return frame, alerts

# Streamlit UI
st.title("VisionTrack - Smart Glasses, Smarter Driving")
contrast_enhance = st.checkbox("Enable Contrast Enhancement", value=False)
glare_reduction = st.checkbox("Enable Glare Reduction", value=False)
object_detection = st.checkbox("Enable Object Detection", value=False)
save_video = st.checkbox("Record and Save Video", value=False)

# Open webcam feed
cap = cv2.VideoCapture(0)
stframe = st.empty()
alert_box = st.empty()
fps_box = st.empty()

# Video Writer Setup
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    start_time = time.time()
    
    original_frame = frame.copy()
    
    if contrast_enhance:
        frame = enhance_contrast(frame)
    if glare_reduction:
        frame = reduce_glare(frame)
    if object_detection:
        frame, alerts = detect_objects(frame)
        alert_box.write("\n".join(alerts))
    
    # Calculate FPS
    fps = 1.0 / (time.time() - start_time)
    fps_box.write(f"FPS: {fps:.2f}")
    
    # Side-by-side comparison
    combined_frame = np.hstack((original_frame, frame))
    combined_frame = cv2.cvtColor(combined_frame, cv2.COLOR_BGR2RGB)
    stframe.image(combined_frame, channels="RGB", use_container_width=True)
    
    # Save video if enabled
    if save_video:
        if out is None:
            out = cv2.VideoWriter("visiontrack_output.avi", fourcc, 20.0, (combined_frame.shape[1], combined_frame.shape[0]))
        out.write(combined_frame)

cap.release()
if out:
    out.release()
st.success("Processing Complete! Video saved as visiontrack_output.avi")