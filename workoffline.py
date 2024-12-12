import cv2
import pytesseract

# Replace 'video_path.mp4' with your actual video file path
video_path = "ElephantsDream.mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("End of video")
        break

    # Preprocess frame for OCR
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray_frame)

    print("Extracted Text:", text)

    # Display the video frame
    cv2.imshow("Video Frame", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
