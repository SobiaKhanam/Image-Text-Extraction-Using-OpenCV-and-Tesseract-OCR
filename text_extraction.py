!apt-get update -qq
!apt-get install -y tesseract-ocr
!pip install -q pytesseract opencv-python-headless

image_path = "/content/testocr.png"

print("Uploaded file:", image_path)

import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread(image_path)

if image is None:
    raise ValueError(f"Could not read image: {image_path}")

# Display the original image
plt.figure(figsize=(12, 8))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Input Image")
plt.axis("off")
plt.show()

import pytesseract

# Extract text from the image
extracted_text = pytesseract.image_to_string(image)

# Print the recognized text
print("Extracted Text:\n")
print(extracted_text)

# Optional: Get individual words and confidence scores
# Tesseract can also return word-level results and confidence values, which can help you evaluate OCR output.
# data = pytesseract.image_to_data(
#    processed_image,
#    output_type=pytesseract.Output.DICT
#)

#for i, word in enumerate(data["text"]):
#    word = word.strip()
#    confidence = int(data["conf"][i])

#    if word and confidence >= 0:
#       print(f"{word} | Confidence: {confidence}%")
