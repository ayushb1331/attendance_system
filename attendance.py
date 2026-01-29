import cv2
import pandas as pd
from datetime import datetime
from deepface import DeepFace
import os

# Configuration
DB_PATH = "data/"
LOG_FILE = "logs/attendance.csv"

def log_attendance(user_id, status):
    """Logs punch-in/out to CSV."""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    
    if not os.path.exists(LOG_FILE):
        df = pd.DataFrame(columns=["Date", "User_ID", "Time", "Status"])
    else:
        df = pd.read_csv(LOG_FILE)
    
    new_entry = {"Date": date_str, "User_ID": user_id, "Time": time_str, "Status": status}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(LOG_FILE, index=False)
    print(f"Logged {status} for {user_id}")

def run_attendance():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret: break
        
        # UI Overlay
        cv2.putText(frame, "Press 'i' to Punch-In | 'o' to Punch-Out | 'q' to Quit", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        cv2.imshow("Attendance System", frame)
        key = cv2.waitKey(1) & 0xFF
        
        if key in [ord('i'), ord('o')]:
            status = "IN" if key == ord('i') else "OUT"
            try:
                # Recognition logic
                results = DeepFace.find(img_path=frame, db_path=DB_PATH, 
                                        model_name="VGG-Face", enforce_detection=False)
                
                if len(results) > 0 and not results[0].empty:
                    # Get ID from the folder name of the matched image
                    matched_path = results[0]['identity'][0]
                    user_id = matched_path.split(os.sep)[1] 
                    log_attendance(user_id, status)
                    cv2.putText(frame, f"Success: {user_id}", (10, 70), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    print("User not recognized.")
            except Exception as e:
                print(f"Error: {e}")

        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    run_attendance()