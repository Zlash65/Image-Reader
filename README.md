# Image-Reader
Read text from Image and convert it to json

### How to use
```bash
# the name or path of the image can be provided by using --image
python image_reader.py --image report1.jpg

# different enhancements

# blend same image on itself to increase whiteness
python image_reader.py --image report1.jpg --preprocess blend

python image_reader.py --image report1.jpg --preprocess enhance

# kill all colours and convert image in b&w form
python image_reader.py --image report1.jpg --preprocess grayscale

python image_reader.py --image report1.jpg --preprocess grayscale_enhance

# apply all the enhancements
python image_reader.py --image report1.jpg --preprocess all
```

*Note: Make sure you run `pip install -r requirements.txt` before running the project
