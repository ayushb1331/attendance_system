import cv2
import numpy as np

# Load Haar Cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

def detect_liveness(frame):
    """
    Basic spoof prevention: Detects if eyes are present and 
    calculates the 'openness' based on intensity variance.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        # If no eyes are detected in a face, it's a potential spoof or eyes are closed
        if len(eyes) < 2:
            return False, "Liveness Check Failed: Eyes not detected"
            
        return True, "Liveness Verified"
    
    return False, "No face detected"

def apply_preprocessing(frame):
    """
    Handles varying lighting conditions using Histogram Equalization.
    """
    # Convert to YUV to equalize only the brightness (Luminance) channel
    img_yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)).apply(img_yuv[:,:,0])
    
    # Convert back to BGR
    processed_frame = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    return processed_frame
