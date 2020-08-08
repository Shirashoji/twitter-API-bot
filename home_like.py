import f_twitter, time

count = 100
for i in range(count):
    tweet_id = f_twitter.timelines_tweet()
    f_twitter.do_favorite(tweet_id)
    if not i==count-1:
        time.sleep(0.5)
