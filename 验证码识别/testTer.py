from PIL import Image
from pytesseract  import *

pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
image_file = "codeExample//1000.jpeg"
im = Image.open(image_file)
text = pytesseract.image_to_string(im,lang = 'eng')

print ("=====output=======\n")
print (text)
