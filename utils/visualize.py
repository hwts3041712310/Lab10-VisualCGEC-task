import cv2
import json
import  os

#  路径配置
JSON_INPUT_PATH = "./diff.json"
IMAGE_DIR = "./input/train_img"
OUTPUT_DIR = "./tmp"

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 加载 JSON 数据
with open(JSON_INPUT_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

for sample in data:
    image_path = os.path.join(IMAGE_DIR, sample["path"])
    output_path = os.path.join(OUTPUT_DIR, f"visual_{sample['fk_homework_id']}_diff.png")

    # 加载图像
    img = cv2.imread(image_path)

    # 确保图像存在
    if img is None:
        print(f"❌ 图像未找到：{image_path}")
        continue  # 改为 continue 避免直接退出整个程序

    # 获取图像尺寸
    img_height, img_width = img.shape[:2]

    # 遍历所有 bounding box 并绘制
    for box in sample["bounding_box_list"]:
        x1, x2 = box["start_x"], box["end_x"]
        y1, y2 = box["start_y"], box["end_y"]

        # 判断是否超出图像范围
        if x1 < 0 or y1 < 0 or x2 > img_width or y2 > img_height:
            print(f"⚠️ Bounding box 超出图像范围：({x1}, {y1}) - ({x2}, {y2})")
            continue

        # 绘制矩形框
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

    # 保存标注后的图像
    cv2.imwrite(output_path, img)
    print(f"✅ 图像已保存至：{output_path}")

# 显示图像（可选）
#cv2.imshow("Bounding Box Visualization", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()