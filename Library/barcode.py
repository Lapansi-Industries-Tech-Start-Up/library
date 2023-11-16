import pyqrcode
from PIL import Image

# Define the URL you want to encode in the barcode
url = "https://lapansiindustries.com/Library/LibraryCBU.html"

# Generate a QR code
qr = pyqrcode.create(url)

# Specify the filename for the image
filename = "barcode.png"

# Save the QR code as an image
qr.png(filename, scale=6)

# Open and display the generated barcode image (optional)
barcode_image = Image.open(filename)
barcode_image.show()

# You can now find the generated barcode image as 'barcode.png' in your working directory
