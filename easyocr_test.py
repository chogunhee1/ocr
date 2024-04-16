import os
import easyocr
from PIL import Image, ImageDraw, ImageFont

reader = easyocr.Reader(['en', 'ko'], gpu=False)

DATAPATH = "C:/ocr-store/"

font_size = 30
font_path = "C:/test/나눔 글꼴/나눔고딕/NanumFontSetup_TTF_GOTHIC/NanumGothic.ttf"
font = ImageFont.truetype(font_path, font_size, encoding="UTF-8")

for file_name in os.listdir(DATAPATH):
    file_path = os.path.join(DATAPATH, file_name)
    
    if os.path.isfile(file_path):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            result = reader.readtext(file_path)
            
            img = Image.open(file_path)
            
            draw = ImageDraw.Draw(img)
            for r in result:
                x, y = min(list(_[0] for _ in r[0])), min(list(_[1] for _ in r[0]))
                text_data = r[1]
                draw.text((x-10, y-10), text_data, font=font, fill=(255, 0, 0))
            
            result_path = os.path.splitext(file_path)[0] + "-result.png"
            img.save(result_path)



'''
import easyocr

# GPU를 사용하여 EasyOCR 초기화
reader = easyocr.Reader(['ko', 'en'], gpu=True)

# OCR 수행할 이미지 파일 경로
image_path = 'recog_test.PNG'

# OCR 수행 및 결과 추출
results = reader.readtext(image_path)

# 결과값을 텍스트 파일에 저장
output_file = 'easyocr_output.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    for result in results:
        file.write(result[1] + '\n')
'''


'''
from easyocr import Reader

langs = ['ko', 'en']
filename = 'recog_test.PNG'

print("[INFO] OCR'ing input image...")
reader = Reader(lang_list=langs)
results = reader.readtext(filename)

print("Detected Text:")
output_text = ""
for result in results:
    output_text += result[1] + "\n"  # 각 텍스트를 줄 바꿈과 함께 문자열에 추가

output_filename = 'easyocr_output.txt'
with open(output_filename, 'w', encoding='utf-8') as file:
    file.write(output_text)

print("Output saved to '{}'".format(output_filename))
'''
