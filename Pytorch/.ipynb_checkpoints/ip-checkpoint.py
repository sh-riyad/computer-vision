import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load and process the image
img = Image.open("iiuc.png").convert('L')  # Convert to grayscale
img = img.resize((16, 16), Image.Resampling.NEAREST)  # Resize to 16x16
pixel_array = np.array(img)

# Print the pixel values in the resized array
for array in pixel_array:
    print(array)

# Flatten the 2D pixel array into 1D
flatten_pixel_array = pixel_array.flatten()

# Initialize an empty list to store [value, frequency] pairs
frequency_array = []

# Count the frequency of each pixel intensity (0-255) and store as [value, frequency]
for i in range(256):
    frequency = np.sum(flatten_pixel_array == i)  
    frequency_array.append([i, frequency])

# Print the frequency array as [value, frequency] pairs
print(frequency_array)

# Optionally: Convert frequency_array to a numpy array for easier processing (optional)
frequency_array_np = np.array(frequency_array)

# Optionally: Plot the frequency distribution (histogram)
# values, frequencies = zip(*frequency_array)  # Unpack values and frequencies

