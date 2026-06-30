# Track Visitors Backend

A computer vision based backend system designed to track visitors across multiple camera points, process face recognition results, manage visitor movement records, and expose backend APIs for reporting and administration.

This project was developed as a Final Year Project backend module, focusing on visitor identification, camera based monitoring, path tracking, alert handling, and structured reporting.

---

## Overview

Track Visitors Backend is built to support an intelligent visitor monitoring system. The backend processes camera inputs, performs visitor recognition, stores visitor related data, and provides API modules for managing locations, floors, cameras, visitors, visits, paths, alerts, users, and reports.

The system is designed around a modular backend architecture where each major feature is separated into its own API file, making the project easier to understand, maintain, and extend.

---

## Key Features

- Visitor detection and recognition using computer vision techniques
- Face recognition support for image and video based inputs
- Camera wise visitor result processing
- Unknown person detection and storage
- Visitor path tracking across multiple camera points
- Location, floor, block, and camera management
- User and login management
- Alert generation and handling
- Reporting module for visitor related records
- Output video and image preparation utilities
- Structured backend API layer for integration with frontend applications

---

## System Modules

### API Layer

The `API/` directory contains backend modules responsible for handling the main application entities:

| Module | Purpose |
|---|---|
| `Login.py` | Handles login related backend operations |
| `User.py` | Manages user records and user related functionality |
| `Visitor.py` | Handles visitor information and visitor records |
| `Visit.py` | Manages visit related backend logic |
| `Camera.py` | Handles camera registration, configuration, and camera operations |
| `Location.py` | Manages location related data |
| `Floor.py` | Handles floor level information |
| `Block.py` | Manages block level data |
| `Path.py` | Handles visitor path and movement tracking |
| `Alert.py` | Manages system alerts |
| `Reports.py` | Generates and manages reporting data |

---

## Computer Vision and Recognition Modules

| File | Purpose |
|---|---|
| `FaceNet.py` | Core FaceNet based recognition logic |
| `FaceNet_perform_image.py` | Performs face recognition on image inputs |
| `FaceNet_perform_video.py` | Performs face recognition on video inputs |
| `FaceRecognition_perform_image.py` | Image based face recognition support |
| `FaceRecognition_perform_video.py` | Video based face recognition support |
| `PrepareOutputVideo.py` | Prepares processed output video results |
| `visitorsInFrame.py` | Handles visitor detection inside video frames |

---

## Utility Files

| File | Purpose |
|---|---|
| `main.py` | Main backend entry point for the application |
| `DB_Connection.py` | Database connection configuration |
| `Connection.py` | Additional connection handling |
| `Extras_Func.py` | Helper functions used across the system |
| `HelperFunctions.py` | Common reusable backend utilities |
| `test.py` | Testing and experimental execution file |

---

## Technology Stack

- **Programming Language:** Python
- **Computer Vision:** OpenCV based processing
- **Face Recognition:** FaceNet / face recognition pipeline
- **Backend Architecture:** Modular Python API structure
- **Data Storage:** Database connection layer with JSON based supporting records
- **Media Processing:** Image and video frame processing

---

## How the System Works

1. Visitor images and camera videos are provided to the backend.
2. The system processes camera frames and detects visitors.
3. Face recognition modules compare detected faces with stored visitor data.
4. Recognized visitors are mapped with their visit records.
5. Unknown visitors are stored separately for review.
6. Camera results and visitor paths are generated.
7. API modules provide structured access to visitors, cameras, locations, alerts, paths, and reports.

---

## Disclaimer

This project is intended for academic and demonstration purposes. For production use, additional work is required in security, privacy compliance, and deployment configuration.
