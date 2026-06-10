# 👓 VisionTrack — AI-Powered Night Vision Assistance System

---

<div align="center">

### 🌙 Intelligent Night Vision Enhancement • 🚗 Real-Time Driving Assistance • 🎯 YOLOv8 Object Detection • 💡 Glare Reduction

<br>

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![AI](https://img.shields.io/badge/AI-Powered-purple)
![Night Vision](https://img.shields.io/badge/Night-Vision-black)
![CLAHE](https://img.shields.io/badge/CLAHE-Enhancement-yellow)
![Glare Reduction](https://img.shields.io/badge/Glare-Reduction-lightgrey)
![Real Time](https://img.shields.io/badge/Real-Time%20Processing-success)
![Computer Vision](https://img.shields.io/badge/Computer-Vision-blueviolet)
![Hackathon](https://img.shields.io/badge/Project-Pitch%20Perfect-brightgreen)
![Status](https://img.shields.io/badge/Status-Completed-success)

</div>

---

## 🚀 Overview

VisionTrack is an AI-powered night vision assistance system designed to improve visibility and safety during night driving. Using advanced computer vision and deep learning techniques, the system enhances low-light footage, reduces headlight glare, and detects pedestrians, animals, and obstacles in real-time.

The project combines OpenCV image enhancement, YOLOv8 object detection, and Streamlit-based visualization to provide drivers with better situational awareness in challenging nighttime environments.

---

## ✨ Features

### 🌙 Night Vision Enhancement
- Enhances visibility in low-light environments
- Improves road and object clarity during night driving
- AI-assisted image processing for better perception

### 🎨 Contrast Enhancement
- Uses CLAHE (Contrast Limited Adaptive Histogram Equalization)
- Highlights dark regions without overexposure
- Improves scene visibility in real time

### 💡 Glare Reduction
- Minimizes headlight glare from oncoming vehicles
- Preserves important road details
- Adaptive thresholding and image correction

### 🎯 AI Object Detection
- Powered by YOLOv8
- Detects pedestrians, animals, vehicles, and obstacles
- Real-time bounding boxes and alerts

### 🎥 Live Video Processing
- Real-time frame enhancement
- Side-by-side original vs enhanced comparison
- Continuous video stream analysis

### 🖥 Interactive Dashboard
- Built using Streamlit
- Enable/disable AI features dynamically
- User-friendly visualization interface

### 📹 Video Recording
- Save processed video output
- Record enhanced footage for later analysis

### 👓 Future Smart Glasses Integration
- ESP32-S3 AI Module Support
- Infrared Night Vision Sensors
- OLED/HUD Display Integration
- Adaptive Brightness Control
- Wearable AI Vision Assistance

---
## 🛠 Tech Stack

### Programming Languages
- Python

### Computer Vision
- OpenCV
- NumPy

### Deep Learning
- YOLOv8 (Ultralytics)

### Web Framework
- Streamlit

### AI Techniques
- Object Detection
- Image Enhancement
- Contrast Optimization
- Glare Reduction

### Hardware Vision (Future Integration)
- ESP32-S3 AI Module
- ESP32-CAM
- MLX90640 Thermal Sensor
- AMG8833 Infrared Sensor
- OLED/HUD Display

---

## 🏗 System Architecture

```text
Video Input / Camera Feed
           │
           ▼
 ┌───────────────────┐
 │ Image Enhancement │
 │      (CLAHE)      │
 └───────────────────┘
           │
           ▼
 ┌───────────────────┐
 │  Glare Reduction  │
 │ Adaptive Threshold│
 └───────────────────┘
           │
           ▼
 ┌───────────────────┐
 │ YOLOv8 Detection  │
 │ Pedestrians       │
 │ Animals           │
 │ Obstacles         │
 └───────────────────┘
           │
           ▼
 ┌───────────────────┐
 │ Real-Time Alerts  │
 │ Bounding Boxes    │
 └───────────────────┘
           │
           ▼
 ┌───────────────────┐
 │ Streamlit UI      │
 │ Live Visualization│
 └───────────────────┘
```

---

## 🔬 Methodology

### Step 1: Video Acquisition
The system captures live video streams from a camera source and processes each frame individually.

### Step 2: Image Enhancement
Contrast Limited Adaptive Histogram Equalization (CLAHE) is applied to improve visibility in dark environments without causing overexposure.

### Step 3: Glare Reduction
Adaptive thresholding and image processing techniques are used to minimize headlight glare while preserving critical road information.

### Step 4: Object Detection
YOLOv8 detects pedestrians, animals, vehicles, and obstacles in real-time, improving situational awareness.

### Step 5: Visual Feedback
Detected objects are highlighted using bounding boxes and displayed through an interactive Streamlit dashboard.

### Step 6: User Interaction
Users can dynamically enable or disable enhancement features and compare original and processed frames side-by-side.

---

## 📊 Competitive Advantages

| Feature | VisionTrack | Traditional Night Vision Glasses | Adaptive Car Headlights |
|----------|------------|---------------------------------|------------------------|
| AI-Powered Vision Enhancement | ✅ | ❌ | ❌ |
| Real-Time Object Detection | ✅ | ❌ | ❌ |
| Glare Reduction | ✅ | ✅ | ✅ |
| Personalized AI Adaptation | ✅ | ❌ | ❌ |
| Wearable & Portable | ✅ | ✅ | ❌ |
| Night Vision Optimization | ✅ | ✅ | ✅ |
| Affordable Solution | ✅ | ✅ | ❌ |
| Open Source Potential | ✅ | ❌ | ❌ |

---

## 📂 Project Structure

```text
Vision-Track/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   └── YOLOv8 Model Files
│
├── assets/
│   ├── Images
│   └── Demo Videos
│
├── utils/
│   ├── Image Enhancement
│   ├── Glare Reduction
│   └── Object Detection
│
└── outputs/
    ├── Enhanced Videos
    └── Detection Results
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/shreyaaa26-codes/Vision-Track.git
```

### Navigate to Project Directory

```bash
cd Vision-Track
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🚀 Future Scope

### 👓 Smart Wearable Integration
- AI-powered smart glasses for night driving assistance
- Lightweight and portable wearable system

### 🌡 Infrared & Thermal Vision
- Thermal imaging for improved pedestrian detection
- Enhanced performance in foggy and low-visibility conditions

### 🧠 Personalized AI Adaptation
- User-specific brightness and contrast adjustments
- Adaptive visibility enhancement based on vision conditions

### 🛰 Vehicle Integration
- Integration with vehicle safety systems
- Driver assistance and hazard alerts

### 🥽 AR-Based Navigation
- Augmented Reality overlays
- Lane guidance and navigation assistance

### ☁ Cloud Connectivity
- Remote diagnostics
- Firmware updates
- AI model improvements

---

## 👨‍💻 Team Members

### Shreya
**Role:** Team Lead, Pitching & Business Strategy

Responsibilities:
- Project ideation and vision
- Problem identification and market research
- Business model design
- Revenue strategy and pricing model
- Investor pitch preparation
- Presentation and demonstration

### Rida
**Role:** Pitching & Market Analysis

Responsibilities:
- Market validation
- Competitive analysis
- Business planning
- Go-to-market strategy
- Presentation and pitching

### Anirudh
**Role:** Prototype Developer & AI Engineer

Responsibilities:
- Python development
- OpenCV implementation
- YOLOv8 integration
- Streamlit application development
- Prototype architecture
- AI model deployment

---

## 🏆 Competition & Presentation

### Pitch Perfect Competition 2025 - Falak, MIT Bangalore

VisionTrack was developed and presented as part of the **Pitch Perfect Competition**, where the team showcased:

- Problem Statement
- AI-Powered Solution
- Working Prototype
- Business Model
- Revenue Projections
- Go-To-Market Strategy
- Funding Requirements
- Future Vision

The project received appreciation for combining Artificial Intelligence, Computer Vision, Wearable Technology, and Driver Safety into a scalable and impactful solution.

---



---
