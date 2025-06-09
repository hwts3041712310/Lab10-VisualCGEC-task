from paddleocr import PaddleOCR
import json
# 初始化 PaddleOCR 实例
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False)

# 本地图像路径（请替换为你自己的图片路径）
#image_path = "./input/train_img_data/2597.jpg"  # ← 替换为你的本地图片路径

# 对本地图像执行 OCR 推理
#result = ocr.predict(input=image_path)# 可视化结果并保存 json 结果


#for res in result:
#    res.save_to_json("tmp_json")

def process_recognition_result(data):

    source_text = ''.join(data['rec_texts'])  # 合并所有文本行

    # 用于存储所有字符的bounding boxes
    char_bounding_boxes = []

    for text_line, box in zip(data['rec_texts'], data['rec_boxes']):
        num_chars = len(text_line)
        if num_chars == 0:
            continue

        x1, y1, x2, y2 = box
        width = (x2 - x1) / num_chars  # 每个字符的平均宽度

        # 分配每个字符的bounding box
        for i in range(num_chars):
            char_box = {
                "start_x": int(x1 + i * width),
                "end_x": int(x1 + (i + 1) * width),
                "start_y": y1,
                "end_y": y2
            }
            char_bounding_boxes.append(char_box)

    # 构造输出JSON对象
    result = {
        "source_text": source_text,
        "bounding_box_list": char_bounding_boxes
    }
    return result

# 执行程序
#process_recognition_result('./output/2597_res.json', 'test.json')

def Paddle_OCR(image_path):
    result = ocr.predict(input=image_path)

    res_json = result[0].json  # 得到 {'res': {...}}


    data = res_json['res']  # ← 才是真正包含 rec_texts 和 rec_boxes 的部分

    src_with_box = process_recognition_result(data)
    return src_with_box


if __name__ == '__main__':
    x = Paddle_OCR('./input/train_img/2597.jpg')
    with open("./test_result.json", "w") as out_file:
        json.dump(x, out_file, ensure_ascii=False, indent=4)

