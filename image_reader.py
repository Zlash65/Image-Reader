import numpy as np
import pytesseract
import os, re, sys, cv2
from PIL import Image

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
	args = vars(ap.parse_args())

	read_text(args["image"])

	print('\n------ Done -------')
