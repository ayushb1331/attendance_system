import cv2
import os

def register_user(user_id):
    cap = cv2.VideoCapture(0)
    path = f"data/{user_id}"
    os.makedirs(path, exist_ok=True)
    
    print(f"Registering {user_id}. Press 's' to capture 3 photos.")
    count = 0
    while count < 3:
        ret, frame = cap.read()
        cv2.imshow("Registering", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            img_name = f"{path}/{user_id}_{count}.jpg"
            cv2.imwrite(img_name, frame)
            print(f"Captured {img_name}")
            count += 1
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    uid = input("Enter unique User ID: ")
    register_user(uid)