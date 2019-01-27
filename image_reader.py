import numpy as np
import pytesseract
import os, re, sys, cv2
from PIL import Image

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
	else:
		read_text(args["image"])

	# remove temporary files
	os.remove("temp1.png")

	print('\n------ Done -------')
