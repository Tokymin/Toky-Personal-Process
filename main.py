import cv2
import numpy as np

# Load the image
image = cv2.imread('DataFiles/inputs/colon.png', cv2.IMREAD_COLOR)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel filter to detect edges in x and y directions
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)

# Calculate the magnitude
magnitude = cv2.magnitude(sobel_x, sobel_y)

# Normalize to 0-255
magnitude = np.uint8(255 * magnitude / np.max(magnitude))

# Save the result
cv2.imwrite('DataFiles/results/colon_edge_detected_image.png', magnitude)
