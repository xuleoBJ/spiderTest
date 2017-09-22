from PIL import Image
from pytesseract  import *

pytesseract.tesseract_cmd  = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
image_file = "codeExample\\1000.jpeg"
im = Image.open(image_file,mode='r')
text = pytesseract.image_to_string(im)

print ("=====output=======\n")
print (text)
