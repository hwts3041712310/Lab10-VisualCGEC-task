import cv2
import numpy as np
from paddleocr import PaddleOCR
from openai import OpenAI

client = OpenAI(
    api_key='sk-fa75328fdcd545f7a1668b1423d2f218', 
    base_url="https://chat.ecnu.edu.cn/open/api/v1",
)
def correct_llm(gt):

    completion = client.chat.completions.create(
        model="ecnu-plus", # 模型列表：https://developer.ecnu.edu.cn/vitepress/llm/api/models.html
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': '下面是一段中文文章，其中开头可能包含了个人信息、题干、或者其他与正文无关的东西，去除这些信息以及可能存在的标题的同时，纠正这段话中的语法错误。只允许做最小且必要的改动，基本不改动标点符号，不换行，禁止改变原意，只返回给我结果:"\n' +  gt  }],
        )
    
    # 提取 content 内容
    content = completion.choices[0].message.content.strip()

    # 去除开头结尾的换行符和引号（如果有的话）
    if content.startswith('\n\n"') and content.endswith('"'):
        content = content[3:-1].strip()
    #print(content)
    return content
# 初始化 OCR 模型
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
)

# 图像路径（请替换为你自己的图片路径）
image_path = "./input/train_img/2597.jpg"

# 读取原始图像
original_image = cv2.imread(image_path)

# 定义锐化核
sharpen_kernel = np.array([[-1, -1, -1],
                           [-1,  9, -1],
                           [-1, -1, -1]])

# 应用锐化滤波器
sharpened_image = cv2.filter2D(original_image, -1, sharpen_kernel)

# 临时保存锐化后的图像
sharpened_path = "./temp_sharpened.jpg"
cv2.imwrite(sharpened_path, sharpened_image)

# 使用 PaddleOCR 对原始图像进行识别
result_original = ocr.predict(input=image_path)
res_json = result_original[0].json
data = res_json['res']
source_text = ''.join(data['rec_texts'])  # 合并所有文本行

print("✅ 原始图像 OCR 结果：")
print(source_text)
pred = correct_llm(source_text)
print("✅ LLM 矫正结果：")
print(pred)

# 使用 PaddleOCR 对锐化后图像进行识别
result_sharpened = ocr.predict(input=sharpened_path)
res_json = result_sharpened[0].json
data = res_json['res']
source_text = ''.join(data['rec_texts'])  # 合并所有文本行
print("\n✅ 锐化后图像 OCR 结果：")
print(source_text)
pred = correct_llm(source_text)
print("✅ LLM 矫正结果：")
print(pred)

# 显示图像对比（可选）
cv2.imwrite("./original.jpg", original_image)
cv2.imwrite("./sharpened.jpg", sharpened_image)