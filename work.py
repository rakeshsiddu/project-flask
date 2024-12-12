import cv2
import pytesseract
from plyer import notification
import time

keywords = ["ERROR", "ALERT", "WARNING"]

# Initialize the camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Unable to access the camera.")
    exit()

while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Preprocess frame for OCR
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresholded_frame = cv2.threshold(gray_frame, 128, 255, cv2.THRESH_BINARY)

    # Extract text
    text = pytesseract.image_to_string(thresholded_frame)
    print("Extracted Text:", text)

    # Check for keywords
    for keyword in keywords:
        if keyword in text.upper():
            print(f"Notification: {keyword} detected!")
            notification.notify(
                title="Alert",
                message=f"Keyword detected: {keyword}",
                timeout=5
            )
            time.sleep(5)  # Avoid spamming notifications

    # Display the live feed
    cv2.imshow("Live Camera Feed", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
