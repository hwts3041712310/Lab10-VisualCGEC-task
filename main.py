import json
from tqdm import tqdm 
import os
from diff.diff import diff
from GEC.GEC_llm import GEC_llm
from openai import OpenAI
import time
import cv2
import numpy as np
from OCR.baiduOCR.baiduOCR import baiduOCR

#  文件路径配置
INPUT_DIR = "./input"
OUTPUT_DIR = "./output"
TEST_DATA_JSON = os.path.join(INPUT_DIR, "test_data.json")
TEST_IMG_DIR = os.path.join(INPUT_DIR, "test_img")
OUTPUT_JSON = os.path.join(OUTPUT_DIR, "predict.json")

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 加载 train.json 数据
with open(TEST_DATA_JSON, "r", encoding="utf-8") as f:
    data = json.load(f)

results = []

# 记录开始时间
start_time = time.time()
#sharpen_kernel = np.array([[-1, -1, -1],
#                           [-1,  9, -1],
#                           [-1, -1, -1]])

# 遍历数据并处理每张图片
for i, item in tqdm(enumerate(data), total=len(data), desc="处理进度"):
    image_path = os.path.join(TEST_IMG_DIR, item["path"])
    
    # 处理该图片生成 source 和 bounding box json
    tmp = baiduOCR(image_path)
    tmp["fk_homework_id"] = item["fk_homework_id"]
    tmp["path"] = item["path"]
    
    # 根据 source 生成 predict_text
    src = tmp["source_text"]
    pred = GEC_llm(src)
    tmp["predict_text"] = pred

    # 使用 diff 函数生成修改的 bounding box
    tmp = diff(tmp)

    # 最后加入总 results
    results.append(tmp)

# 记录结束时间并计算总耗时
end_time = time.time()
total_duration = (end_time - start_time) / 60

# 将结果写入输出文件
with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

# 打印总耗时信息
print(f"✅ 所有任务已完成！总处理时长: {total_duration:.2f} mins")