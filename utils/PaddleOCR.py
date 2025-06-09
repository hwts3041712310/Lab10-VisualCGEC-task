from paddleocr import PaddleOCR
# 初始化 PaddleOCR 实例
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False)

# 本地图像路径（请替换为你自己的图片路径）
image_path = "./input/train_img_data/2597.jpg"  # ← 替换为你的本地图片路径

# 对本地图像执行 OCR 推理
result = ocr.predict(input=image_path)# 可视化结果并保存 json 结果

for res in result:
    res.print()
    res.save_to_img("output")
    res.save_to_json("output")

