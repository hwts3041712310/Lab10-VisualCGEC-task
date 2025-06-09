import os
from openai import OpenAI

client = OpenAI(
    api_key='sk-fa75328fdcd545f7a1668b1423d2f218', 
    base_url="https://chat.ecnu.edu.cn/open/api/v1",
)
def GEC_llm(gt):

    completion = client.chat.completions.create(
        model="ecnu-plus", # 模型列表：https://developer.ecnu.edu.cn/vitepress/llm/api/models.html
        messages=[
            {'role': 'system', 'content': '你是一位专业的文字校对助手，需要处理外国留学生手写作文的OCR识别文本'},
            {'role': 'user', 'content': '下面是一段手写ocr中文文章，请帮我清理OCR识别的手写作文文本：删除标题、姓名、学号、题干等非作文正文内容，仅保留正文；修正明显的错别字和缺失字符（如上下文可推断），保持最小改动，不确定处保留原文。输出正文修改后的纯文本，不添加额外说明。文本如下："\n' +  gt  }],
        )
    
    # 提取 content 内容
    content = completion.choices[0].message.content.strip()

    # 去除开头结尾的换行符和引号（如果有的话）
    if content.startswith('\n\n"') and content.endswith('"'):
        content = content[3:-1].strip()
    #print(content)
    return content

#print(correct_llm("学号122/2/20420韩国D所人我觉得我淘用手机买东西、看电日影、玩游戏等手机在我的人生是不有离的洪承铉从208年到现在新黎型冠状抽毒改变了很多日常生活.在公共场所与人们保持距离基本上成为了应该遵守的礼仪，尽量避免外出，呆在家里的好越来越多.随着在家中度过的时间代替力外活动土增加，家人一起吃饭的次数也土增加了，正在努力寻钱找可以在室内进行的解“新兴越活动。另外，K时问每看电视或只玩智能手等坏惯也发生了.我们的家人也不例外，随着逐赋渐适应新型型冠状病毒的日常生活的同时，随着外出时间的减少，使用智能手机的时间也明显增加了。我认为新型冠状病毒路从金融业务到兴趣爱妈，不仅使智能手魏机，而风上开学后为了我的学业日程，使用智能机器的时间W以前大幅增加。280多能我一无中十个小时左右用手机我资得手机有优点和缺点所以人们应该正确使用智能手机.大现很数字的的现代我觉得在数学时代智能手机是最具代表性的。桃为大部分人都有，而且接触起方使。"))
