import numpy as np
import pytesseract
import os, re, sys, cv2
from PIL import Image

def convert_to_grayscale(img_path):
	# Read image with opencv
	img = cv2.imread(img_path)

	# Convert to gray
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# Apply dilation and erosion to remove some noise
	kernel = np.ones((1, 1), np.uint8)
	img = cv2.dilate(img, kernel, iterations=1)
	img = cv2.erode(img, kernel, iterations=1)

	# Write the image after apply opencv to do some ...
	cv2.imwrite("temp2.png", img)

def overlay_blend(image_path):
	from PIL import Image
	correctionVal = 0.05 # fraction of white to add to the main image
	img_file = Image.open(image_path)
	img_blended = Image.blend(img_file, img_file, correctionVal)

	img_blended.save("temp1.png")

def read_text(image_path, image_obj=None):
	img = Image.open(image_path) if not image_obj else image_obj
	imagetext = pytesseract.image_to_string(img)

	# x = re.findall('\Name\s([^\s]+)', imagetext)
	print(imagetext)

if __name__ == '__main__':
	from sys import argv
	import argparse

	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", required=True,
		help="path to input image to be OCR'd")
	ap.add_argument("-p", "--preprocess", type=str, default="thresh",
		help="type of preprocessing to be done")
	args = vars(ap.parse_args())

	if args["preprocess"]=="blend":
		overlay_blend(args["image"])
		read_text("temp1.png")
	elif args["preprocess"]=="grayscale":
		convert_to_grayscale(args["image"])
		read_text("temp2.png")
	else:
		read_text(args["image"])

	# remove temporary files
	for i in ["temp1.png", "temp2.png"]:
		try:
			os.remove(i)
		except Exception:
			continue

	print('\n------ Done -------')
