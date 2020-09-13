import json, config
from requests_oauthlib import OAuth1Session
import time


CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理


url = "https://api.twitter.com/1.1/statuses/user_timeline.json" #タイムライン取得エンドポイント
params ={'count':100} #取得数
res = twitter.get(url, params = params)
if res.status_code == 200: #正常通信出来た場合
    timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
else: #うまくいかなかった時
    print("Failed: %d" % res.status_code)
    print("タイムラインの取得ができませんでした。")
    print("-・"*30)
    #exit()

for tweet in timelines: #タイムラインリストをループ処理
    print(tweet['user']['name']+'::'+tweet['text'])
    print(tweet['created_at'])
    print("-・"*30)
    tweet_id = tweet['id']
    try:
        url = "https://api.twitter.com/1.1/favorites/create.json"
        params = {'id' : tweet_id}
        req = twitter.post(url, params = params)
        if req.status_code == 200:
            print('↑のツイートを いいね しました')
            print("-・"*30)
        else:
            print("ERROR: %d" % req.status_code)
            print("いいねに失敗しました。")
            print("-・"*30)
            #exit()
    except Exception as e:
        print()
