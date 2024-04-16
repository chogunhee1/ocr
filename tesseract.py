from PIL import Image
import numpy as np
import pytesseract as tes

filename = 'recog_test.PNG'
config = ('-l kor+eng')
img = np.array(Image.open(filename))
text = tes.image_to_string(img, config = config)

# 터미널 출력
# print(text)

output_file = 'tesseract_output.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(text)