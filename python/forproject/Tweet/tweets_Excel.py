import pandas as pd
import os
if not os.path.isdir('./Tweet/코로나/'):
    os.makedirs('./Tweet/코로나/')

import snscrape.modules.twitter as sntwitter
import pandas as pd

def tweetCrawl(start_y, start_m):
    tweets_list = []

    if start_m == '01' or '03' or '05' or '07' or '08' or '10' or '12':
        all_day = 31
    elif start_m == '04' or '06' or '09' or '11':
        all_day = 30
    else:
        all_day = 28
    
    for i in range(all_day):
        start_d = 1
        start_d = start_d + i
    
        day = str(start_d)

        if len(day) == 1:
            day = "0" + day
        
        print(start_y + "년 " + start_m + "월 " + day + "일 수집중...")
        sname = '코로나 since:2019-10-01' + ' until:'+start_y+'-'+start_m+'-'+day
    
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(sname).get_items()):
            if i>2000:
                break
            tweets_list.append([tweet.date, tweet.content, tweet.likeCount])
    
    tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Text', 'Like'])
    tweets_df['Datetime'] = tweets_df['Datetime'].apply(lambda a: pd.to_datetime(a).date())
    tweets_df.to_excel('./Tweet/코로나/코로나'+start_y+'_'+start_m+'.xlsx',index=False)

#start_y = input("수집할 연도 입력 : ")
#start_m = input("수집할 월 입력 : ")

#start_y = str(start_y)

for i in range(1, 13):
    start_m = str(i)

    start_y = "2021"

    if len(start_m) == 1:
        start_m = "0"+start_m

    tweetCrawl(start_y,start_m)