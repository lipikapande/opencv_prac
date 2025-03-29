import cv2 as cv

# img = cv.imread('photos/cat.jpg')
# cv.imshow('Cat',img)

# cv.waitKey(0)
 
# capture = cv.VideoCapture('photos/video_opencv.mp4')
# Open the video file
cap = cv.VideoCapture("photos/video_opencv.mp4")  # Change to your video file

while True:
    ret, frame = cap.read()
    if not ret:  # If video ends, restart it
        cap.set(cv.CAP_PROP_POS_FRAMES, 0)
        continue
  
    cv.imshow("Video", frame)
    # Check if 'q' is pressed OR window is closed manually
    if cv.waitKey(30) & 0xFF == ord('q') or cv.getWindowProperty("Video", cv.WND_PROP_VISIBLE) < 1:
        break  # Exit the loop
    
cap.release()
cv.destroyAllWindows()