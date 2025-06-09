import json

# 读取原始JSON文件
with open('/Users/yangmingqian/Desktop/深度学习/lab10/input/train_data.json', 'r', encoding='utf-8') as infile:
    data = json.load(infile)

# 提取前50条数据
test_data = data[:50]

# 将前50条数据写入新的test.json文件
with open('/Users/yangmingqian/Desktop/深度学习/lab10/input/test.json', 'w', encoding='utf-8') as outfile:
    json.dump(test_data, outfile, ensure_ascii=False, indent=4)