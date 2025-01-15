from PIL import Image

# Define image size and color
width, height = 1, 1
color = (255, 0, 0)  # Red in RGB

# Create a new image
image = Image.new("RGB", (width, height), color)

# Save the image as a JPEG file
image.save("bare_image.jpg", "JPEG")