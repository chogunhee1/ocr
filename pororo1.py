from pororo import Pororo

pororo_ocr = Pororo(task="ocr", lang="ko")
image_path = "test.jpeg"

result = pororo_ocr(image_path)

print(result)