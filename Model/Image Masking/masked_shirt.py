import cv2
import numpy as np

# Load the image (ensure the path is correct)
image = cv2.imread('replacement_tshirt.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and improve edge detection
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Use binary thresholding to create a binary image
# You may need to adjust the threshold value (127) based on your shirt's brightness
_, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# If contours are found, assume the largest one is the shirt
if contours:
    # Find the largest contour
    largest_contour = max(contours, key=cv2.contourArea)

    # Create a mask for the shirt (initially filled with zeros - black)
    mask = np.zeros_like(gray)

    # Draw the largest contour on the mask, filling it in
    cv2.drawContours(mask, [largest_contour], -1, 255, thickness=cv2.FILLED)

    # Create a 3-channel mask for color images
    mask_3ch = cv2.merge([mask, mask, mask])

    # Use the mask to extract the shirt from the original image
    shirt_only = cv2.bitwise_and(image, mask_3ch)

    # Create a white background
    white_background = np.full_like(image, 255)

    # Combine the shirt with the white background
    result = np.where(mask_3ch == 0, white_background, shirt_only)

    # Save the result
    cv2.imwrite('shirt_with_background_removed.png', result)

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Shirt Mask", mask)
    cv2.imshow("Shirt Only (Background Removed)", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("No contours found. Adjust threshold or check the image.")
