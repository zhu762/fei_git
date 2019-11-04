import os
import json
import base64
import time
import random
import requests
from wxpy import *

s = requests.session()
s.headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}

# 获取语料库
base_dir = os.path.dirname(os.path.abspath(__file__))
chatData_path = base_dir + os.sep + 'chatData' + os.sep + 'public.json'
with open(chatData_path,'r',encoding='utf8') as f:
    chatData = f.read()
chatData = json.loads(chatData)   

# 初始化微信 
bot = Bot(cache_path=True)
bot.enable_puid('wxpy_puid.pkl')

# 初始化聊天对象
yjr = ensure_one(bot.friends().search('杨静如'))
zx = ensure_one(bot.friends().search('郑翔'))
mhf = ensure_one(bot.friends().search('红飞'))
fg = ensure_one(bot.friends().search('付',sex=MALE))
xg = ensure_one(bot.friends().search('菊毛毛',sex=MALE))
my_group_1 = ensure_one(bot.groups().search('四人之家'))
my_group_2 = ensure_one(bot.groups().search('陈钰琪粉丝群'))
my_group_3 = ensure_one(bot.groups().search('family'))
my_group_4 = ensure_one(bot.groups().search('回来吃药'))
my_group_5 = ensure_one(bot.groups().search('燕赵69日常小分队'))
# tuling = Tuling(api_key='7682020d421a455f9caeda9d0048c4a8')
# xiaoi = XiaoI('open1_FSMlucSrQzs0', 'OHmXHvLfADJWfeEydXGA')
not_bot_chat_list = ['换个话题吧','聊点别的吧','无言以对呢','这话我接不了呢','下一个话题吧']

# @bot.register([my_group_1,my_group_2,my_group_3,my_group_4])
# def auto_reply(msg):
#     print(msg)
#     # 只回复文本信息
#     if msg.type == TEXT:
#         my_reply_text = my_reply(msg)
#         msg.reply(my_reply_text)
#     else:
#         msg.reply("不听不听,王八念经")

# def my_reply(msg):
#     if msg.text in chatData:
#         my_reply_text = chatData.get(msg.text)
#     else:
#         my_reply_text = tuling.reply_text(msg,False)
#         print("图灵机器人：%s" % my_reply_text)
#         if my_reply_text in not_bot_chat_list:
#             my_reply_text = random.choice(['牛逼','舒服','你好爽','666','不错'])
#         else:
#             chatData[msg.text] = my_reply_text
#             with open(chatData_path,'w',encoding='utf8') as f:
#                 f.write(json.dumps(chatData,ensure_ascii=False))
#     return my_reply_text

@bot.register(my_group_1)
def f4_reply(msg):
    print(msg)
    resp = s.get("https://chp.shadiao.app/api.php")
    my_reply_text = resp.text
    msg.reply(my_reply_text)

@bot.register(fg)
def fg_reply(msg):
    print(msg)
    resp = s.get("https://chp.shadiao.app/api.php")
    my_reply_text = resp.text
    msg.reply(my_reply_text)

@bot.register(my_group_3)
def family_reply(msg):
    print(msg)
    my_reply_text = random.choice(['厉害','可以','不错','666'])
    msg.reply(my_reply_text)

# @bot.register(my_group_1)
# def f4_reply(msg):
#     if msg.member == zx:
#         my_reply_text = random.choice(['翔总牛逼','傻翔','你们好爽','666','憨批'])
#     elif msg.member == mhf:
#         my_reply_text = "马总牛逼"
#     else:
#         my_reply_text = "尹总牛逼"
#     print(msg)
#     msg.reply(my_reply_text)

@bot.register([my_group_2,my_group_4])
def f3_reply(msg):
    my_reply_text = random.choice(['付狗牛逼','鑫狗牛逼','你们好爽','666'])
    print(msg)
    msg.reply(my_reply_text)

# @bot.register(zx)
# def zx_to_mhf(msg):
#     msg.forward(mhf)

# @bot.register(mhf)
# def mhf_to_zx(msg):
#     msg.forward(zx)

# @bot.register([fg,xg])
# def fg_to_xg(msg):
#     print(msg)
#     if msg.sender == fg:
#         msg.forward(xg)
#     elif msg.sender == xg:
#         msg.forward(fg)

# @bot.register(xg)
# def xg_to_fg(msg):
#     msg.forward(fg)

# 进入 Python 命令行、让程序保持运行
embed()

# 或者仅仅堵塞线程
# bot.join()

# while True:
#     zx.send("在干嘛？")


