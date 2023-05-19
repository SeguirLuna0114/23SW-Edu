import snscrape.modules.twitter as sntwitter
import pandas as pd
# Twitter에서 특정 기간 동안 트윗을 스크래핑하여 리스트에 저장하고, 그 결과를 데이터프레임으로 변환

# 트윗을 긁어와서 넣어놓을 리스트 생성
tweets_list = []

# TwitterSearchScraper를 이용하여 해당 트윗을 긁어와서 리스트에 넣기
#since는 시작 날짜, until은 끝 날짜를 입력
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('코로나 since:2020-12-20 until:2020-12-31').get_items()):
    if i>5000:
        break
    tweets_list.append([tweet.date, tweet.content, tweet.likeCount])
    
# 다 긁어왔다면 데이터 프레임으로 저장시키기
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Text', 'Like'])
tweets_df
print(tweets_df)