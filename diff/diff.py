import json
import difflib
import re
def preprocess_source(source):
    # 替换连续英文字母为仅保留第一个字母
    def replace_word(match):
        word = match.group()
        return word[0]  # 只保留第一个字母

    # 匹配连续的英文字母（大小写+拼音）
    source = re.sub(r'[a-zA-Z]+', replace_word, source)
    return source
def find_modified_indices(source, target):
    d = difflib.SequenceMatcher(None, source, target)
    modified_indices = []

    for tag, i1, i2, j1, j2 in d.get_opcodes():
        if tag == 'replace':
            # source 被替换了
            modified_indices.extend(range(i1, i2))
        elif tag == 'delete':
            # source 被删除了
            modified_indices.extend(range(i1, i2))
        elif tag == 'insert':
            # source 中插入新内容，原位置缺失
            # 可选：记录 source 插入点之前的空缺位置
            if i1 > 0 :
                modified_indices.append(i1 )

    return sorted(modified_indices)
# 加载原始数据
#with open("./test.json", "r", encoding="utf-8") as f:
#    data = json.load(f)



def diff(item):

    fk_homework_id = item["fk_homework_id"]
    path = item["path"]
    source = item["source_text"]
    #predict = item["target_text"]
    predict = item["predict_text"]
    boxes = item["bounding_box_list"]

    # 获取被修改/删除的字符索引
    source = preprocess_source(source)
    modified_indices = find_modified_indices(source, predict)

    # 提取对应的 box 信息
    bounding_box_list = []
    for idx in modified_indices:
        if idx < len(boxes):
            bounding_box_list.append(boxes[idx])

    result={
        "fk_homework_id": fk_homework_id,
        "path": path,
        "source_text": source,
        "predict_text": predict,
        "bounding_box_list": bounding_box_list
    }
    return result

if __name__ == '__main__':
    result = []
    with open("./test.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        result.append(diff(data[0]))
    with open("./ceshidiff.json", "w") as out_file:
        json.dump(result, out_file, ensure_ascii=False, indent=4)

