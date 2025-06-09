#  Lab10-VisualCGEC task
## 杨鸣谦 10225102459 2025.6.9

### 工程结构说明：
```
# 主要文件功能说明
.
├── baseline.ipynb      #  原基准文件，现不使用
├── diff 
│   └── diff.py         #  用以定位修改
├── evaluation.py       #  评价函数
├── GEC
│   ├── GEC_llm.py      #  大语言GEC
│   └── GEC_loc.py      #  本地GEC
├── input
│   ├── test_data.json  #  最终测试集，用以生成predict.json  
│   ├── test_img        #  测试集图片
│   ├── test.json       #  原训练集中的部分样本，用以快速验证
│   ├── train_data.json #  原训练集，现为验证集
│   └── train_img       #  训练集图片
├── main.py *           #  主函数，运行其以进行处理，生成预测
├── OCR               
│   ├── baiduOCR        #  百度OCR功能目录
│   └── PaddleOCR       #  Paddle飞浆OCR功能目录
├── output
│   ├── predict.json    #  预测结果
│   ├── prediction.zip  #  预测结果压缩包，用以提交
├── README.md
├── requirements.txt    #  依赖包目录
├── tmp                 #  临时文件目录，用以存储中间结果
└── utils               #  辅助函数目录，大多在测试期间用以实现验证以及可视化等功能

```

### 环境依赖：
```
pip install requirements.txt
```
// 可能依然存在需要主动安装其他依赖的可能

// 如若如此望见谅ε=ε=┌( >_<)┘

### 运行：
```
python main.py
```
默认路径：读取./input/test_data.json，写入./output/predict.json

---
#### 若遇到任何问题请联系 3041712310@qq.com

__φ(．．;) zZ

