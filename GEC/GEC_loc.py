#from pycorrector import MacBertCorrector
#m = MacBertCorrector("shibing624/bert4csc-base-chinese")
#print(m.correct_batch(['学号122/2/20420韩国D所人我觉得我淘用手机买东西、看电日影、玩游戏等手机在我的人生是不有离的洪承铉从208年到现在新黎型冠状抽毒改变了很多日常生活.']))

from transformers import BertTokenizerFast
from textgen import BartSeq2SeqModel

tokenizer = BertTokenizerFast.from_pretrained('shibing624/bart4csc-base-chinese')
model = BartSeq2SeqModel(
    encoder_type='bart',
    encoder_decoder_type='bart',
    encoder_decoder_name='shibing624/bart4csc-base-chinese',
    tokenizer=tokenizer,
    args={"max_length": 128, "eval_batch_size": 128})
#sentences = ["学号122/2/20420韩国D所人我觉得我淘用手机买东西、看电日影、玩游戏等手机在我的人生是不有离的洪承铉从208年到现在新黎型冠状抽毒改变了很多日常生活."]
#print(model.predict(sentences))
# ['少先队员应该为老人让座']
