
# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import cv2

# capture frames from a video
#cap = cv2.VideoCapture('mountainCars.avi')
cap = cv2.VideoCapture(0)

# Trained XML classifiers describes some features of some object we want to detect 
car_cascade = cv2.CascadeClassifier('car.xml')

imageCount = 0
frameCount = 0

# loop runs if capturing has been initialized.
while (cap.isOpened()):
	# reads frames from a video
	ret, frames = cap.read()

	# convert to gray scale of each frames
	gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

	# Detects cars of different sizes in the input image
	cars = car_cascade.detectMultiScale(gray, 1.1, 1)
	# To draw a rectangle in each cars
	for (x,y,w,h) in cars:
		cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
		if ((frameCount % 10) == 0):
			cv2.imwrite("frame%d.jpg" %imageCount, frames)
			ret,frames = cap.read()
			print('Read a new frame: ', ret)
			imageCount +=1
		frameCount += 1
		# Display frames in a window
		cv2.imshow('video2', frames)

	# Wait for Esc key to stop
	if cv2.waitKey(33) == 27:
		break

# De-allocate any associated memory usage
cap.release()
cv2.destroyAllWindows()

