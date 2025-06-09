import json



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


# 将结果写入新的 JSON 文件（可选）
if __name__ == '__main__':
    # 加载 JSON 数据
    with open("./baiduOCR/out.json", "r") as f:
        data = json.load(f)
    result = integrate(data)
    with open("./baiduOCR/test_result.json", "w") as out_file:
        json.dump(result, out_file, ensure_ascii=False, indent=4)

#if __name__ == '__main__':
#    print(json.dumps(result, ensure_ascii=False, indent=4))