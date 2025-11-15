# Helmet-Detection
"Better a scratched helmet than a shattered skull." Taking road safety under consideration and coming accross road accidents especially by 2 wheeler users caused by them neglecting helmets is a prominent concern that can't be overlooked.

**1. Project Overview**

A deep learning, computer vision based system to detect whether people are wearing helmets in images or videos using YOLOv8 nano model.

1. Detects 2 classes: Helmet and No Helmet.

2. Real-time detection with confidence threshold control.

3. Useful for road safety monitoring and industrial safety.

**2. Key Features:**

**Real-Time Detection on Roads:**

1. Processes live traffic video feeds or recorded footage to identify riders without helmets.

2. Provides instant alerts to traffic authorities or safety systems to prevent violations.

**Class Categories:**

i. Helmet: Rider wearing a helmet.

ii. No Helmet: Rider not wearing a helmet.

**Model Architecture:**

1. Built on YOLOv8, a fast and accurate object detection framework.

2. Uses convolutional neural networks to detect riders and their helmets simultaneously, even in busy traffic scenes.

**Training Data and Robustness:**

1. Trained on diverse datasets with riders in different lighting, weather conditions, and angles.

2. Augmentation techniques like rotation, scaling, and color adjustment improve detection accuracy under real-world road scenarios.

**Safety Impact:
**
1. Detecting riders without helmets can help reduce fatalities and head injuries in two-wheeler accidents.

2. Supports campaigns and enforcement for road safety compliance.

**Deployment:**

1. Integrates with CCTV systems, traffic monitoring cameras, and smart city dashboards.

2. Capable of generating alerts for violations and reporting statistics for policy enforcement.

**Applications:**

1. Traffic Law Enforcement: Ensures adherence to helmet laws.

2. Accident Prevention: Identifies high-risk areas where helmet non-compliance is frequent.

3. Public Awareness: Promotes helmet usage through data-driven campaigns.

**3. Project Architecture**
Helmet-detection/
│
├─ data/                # Training dataset (images + labels)
├─ results/             # Detection output and saved models
├─ train.py             # YOLO training script
├─ detect.py            # YOLO inference/detection script
├─ data.yaml            # Dataset configuration for YOLO
├─ requirements.txt     # Python dependencies
└─ README.md            # Project overview
**4. Requirements**
Python 3.10+
pip install ultralytics
pip install opencv-python

**5. Dataset**

506 images labeled for Helmet and No Helmet.

Labels are in YOLO format: class x_center y_center width height.
