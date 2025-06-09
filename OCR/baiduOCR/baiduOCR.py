# encoding:utf-8
import json
import requests
import base64

def integrate(data):
    full_source_text = ''.join([item["words"] for item in data["words_result"]])

    # 提取所有字符的 bounding_box，并保持顺序
    bounding_box_list = []
    for item in data["words_result"]:
        for char_info in item["chars"]:
            location = char_info["location"]
            bounding_box = {
                "start_x": location["left"],
                "end_x": location["left"] + location["width"],
                "start_y": location["top"],
                "end_y": location["top"] + location["height"]
            }
            bounding_box_list.append(bounding_box)

    # 构建最终结果结构
    result = {
            "source_text": full_source_text,
            "bounding_box_list": bounding_box_list
        }
    return result

def baiduOCR(img_path):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"
    access_token = "24.d5786240659a4b1e8882e5b2dfa90cad.2592000.1751878470.282335-119161995"

    # 二进制方式打开图片文件
    f = open(img_path, 'rb')
    img = base64.b64encode(f.read())

    params = {
        "image":img,
        "recognize_granularity":"small", 
        "eng_granularity":"word"
        }
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    result = integrate(response.json())
    return result

if __name__ == '__main__':
    result = baiduOCR("./input/train_img/2597.jpg")
    with open("./baiduOCR/test_result.json", "w") as out_file:
        json.dump(result, out_file, ensure_ascii=False, indent=4)

