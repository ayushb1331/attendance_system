
# Face Authentication Attendance System 👤✅

A **Python-based attendance system** that utilizes **computer vision** to recognize faces and log **Punch-in** and **Punch-out** times in real-time.  
This project uses **DeepFace** for face recognition and **OpenCV** for camera handling.

---

## 🚀 Features

- **User Registration**: Capture face samples via webcam and store them with a unique User ID  
- **Real-time Recognition**: Matches live video feed against the registered face database  
- **Attendance Logging**: Automatically records timestamps and User IDs into a CSV file  
- **Basic Anti-Spoofing**: Includes blink/liveness detection logic (extendable)

---

## 🛠️ Tech Stack

- **Language**: Python 3.x  
- **ML Library**: DeepFace (VGG-Face model)  
- **Computer Vision**: OpenCV  
- **Data Handling**: Pandas  

---

## 📋 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/ayushb1331/attendance_system.git
cd attendance_system
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install opencv-python deepface tf-keras pandas
```

---

## 📖 How to Use

### 1. Register a Face
Run the registration script to add a new user:

```bash
python registration.py
```

- Enter a **unique User ID** when prompted  
- Look at the camera  
- Press **`s`** to capture **3 face samples**  

---

### 2. Run Attendance System
Start the real-time attendance application:

```bash
python attendance.py
```

**Controls:**
- **Punch-In** → Press `i` while facing the camera  
- **Punch-Out** → Press `o` while facing the camera  
- **Quit** → Press `q`  

---

### 3. View Attendance Logs
All attendance records are stored at:

```
logs/attendance.csv
```

**CSV Format:**
```
Date, User_ID, Time, Status
```

---

## 📌 Notes

- Ensure proper lighting for better recognition accuracy  
- Webcam must be connected and accessible  
- Anti-spoofing logic can be extended with eye-blink or head-movement detection  
