# encoding:utf-8
import json
import requests

with open("hua.json") as f:
    step = json.load(f)

url1 = "http://106.14.57.14:30496/api/newgame/"
url2 = "http://106.14.57.14:30496/api/submit/"

res = requests.get(url1)
res = json.loads(res.text)
gameId = res['gameId']  #获取开始游戏对应gameId

#上下左右分别对应1342，红块定位点为左上角，只爆破红橙
res = requests.post(url = url2 + str(gameId),data = step)
print (res.text)