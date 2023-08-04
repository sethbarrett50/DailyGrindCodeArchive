# OpenCV, or Open Source Computer Vision, is a powerful and widely-used library for image and video processing in Python.
# For an example of image translation, the following code applies a gaussian blur to an image:
import cv2

# Load an image
img = cv2.imread("image.jpg")

# Apply a gaussian blur
img = cv2.GaussianBlur(img, (5, 5), 0)

# Show the image
cv2.imshow("Blurred Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Another common task in image processing is image transformation. 
# OpenCV provides a wide range of image transformation functions, including rotation, scaling, and translation. 
# For example, the following code rotates an image by 45 degrees:
import cv2
import numpy as np

# Load an image
img = cv2.imread("image.jpg")

# Get the image size
rows, cols, _ = img.shape

# Define the rotation matrix
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)

# Rotate the image
img = cv2.warpAffine(img, M, (cols, rows))

# Show the image
cv2.imshow("Rotated Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# OpenCV also provides a wide range of feature detection functions, ssuch as Harris corner detection, SIFT, and SURF. 
# These functions are useful for image registration, object recognition, and more. 
# For example, the following code detects Harris corners in an image:
import cv2

# Load an image
img = cv2.imread("image.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect Harris corners
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# Show the image
img[dst>0.01*dst.max()]=[0,0,255]
cv2.imshow('Harris Corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
