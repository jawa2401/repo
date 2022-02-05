from PIL import Image
import pytesseract
img = Image.open('dzg/livakovic.png')  # load image
new_img = Image.new('RGB', (400, 400), color = 'white')  # create a larger canvas
new_img.paste(im=img, box=(100,100), mask=img)  # paste original CHUBB in the large image
text = pytesseract.image_to_string(new_img, lang='eng', config='--psm 12')  # OCR
print(text)  # CHUBB