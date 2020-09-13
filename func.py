import json, config
from requests_oauthlib import OAuth1Session
import time


CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理


def timelines_tweet(count):
    global timelines
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json" #タイムライン取得エンドポイント
    params ={'count' : count} #取得数
    res = twitter.get(url, params = params)
    if res.status_code == 200: #正常通信出来た場合
        timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
    else: #うまくいかなかった時
        print("Failed: %d" % res.status_code)
        print("タイムラインの取得ができませんでした。")
        print("-・"*30)
        #exit()

def favorite_tweet(count=3):
    url = "https://api.twitter.com/1.1/favorites/list.json"
    params ={'count' : count} #取得数
    res = twitter.get(url, params = params)
    if res.status_code == 200: #うまくいった時
        favorites = json.loads(res.text) #レスポンスからいいねリストを取得
        for tweet in favorites: #いいねリストをループ処理
            print(tweet['user']['name']+'::'+tweet['text'])
            print(tweet['created_at'])
            print("-・"*30)
            return tweet['id']
    else: #うまくいかなかったとき
        print("Failed: %d" % res.status_code)
        print("いいねリストを取得できませんでした。")
        print("-・"*30)
        #exit()

def do_favorite(tweet_id):
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


def unfavorite(tweet_id):
    url = "https://api.twitter.com/1.1/favorites/destroy.json"
    params = {'id' : tweet_id}
    req = twitter.post(url, params = params)
    if req.status_code == 200:
        print('↑のツイートの いいね を外しました')
        print("-・"*30)
    else:
        print("ERROR: %d" % req.status_code)
        print("終了します")
        print("-・"*30)
        #exit()


def tweet(tweet_text):
    url = "https://api.twitter.com/1.1/statuses/update.json" #JsonのURL
    params = {
        "status": tweet_text,
        }
    req = twitter.post(url, params=params) #ツイートしてる場所
    if req.status_code == 200: #うまくいった時
        print('送信完了!')
        print("-・"*30)
    else: #うまくいかなかった時
        print("Failed: %d" % req.status_code)
        print("終了します")
        print("-・"*30)

if __name__ == '__main__':
    text = ("テストテスト\n"+"Tweetを\n"+"Python3から\n"+"送信しました")
    tweet()
    print("finish")
