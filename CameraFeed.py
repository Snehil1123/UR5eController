import cv2

# Set pixel dimensions of camera (width, height)
cameraW = 0
cameraH = 0

vid = cv2.VideoCapture(0)

vid.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, cameraW)

vid.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, cameraH)

while True:

  ret, frame = vid.read()

  cv2.imshow(‘preview’,frame)
  
  # Press "q" to quit
  if cv2.waitKey(1) & 0xFF == ord(‘q’):

    break
