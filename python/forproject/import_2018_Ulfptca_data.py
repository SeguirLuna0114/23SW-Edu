import json
import math

#json 파일 열기
with open('xx2018_UlfptcaAlarmInfo.json', 'r', encoding='utf-8') as file:
    data2018 = json.load(file)

# itemCode가 'PM25'인 항목 중 'issueVal' 데이터 가져오기
issue_vals_2018_PM25 = []
issue_vals_2018_PM10 = []

for item in data2018:
    if item['itemCode'] == 'PM25':
        issue_vals_2018_PM25.append(int(item['issueVal']))
    elif item['itemCode'] == 'PM10':
        issue_vals_2018_PM10.append(int(item['issueVal']))

#결과 출력
print('\n 2018_PM25')
#print(issue_vals_2018_PM25)

average_2018_PM25 = sum(issue_vals_2018_PM25) / len(issue_vals_2018_PM25)

#올림하여 정수로 표현
print('# 2018_PM25 평균 : ', math.ceil(average_2018_PM25))

print('\n 2018_PM10')
#print(issue_vals_2018_PM10)

average_2018_PM10 = sum(issue_vals_2018_PM10) / len(issue_vals_2018_PM10)

#올림하여 정수로 표현
print('# 2018_PM10 평균 : ', math.ceil(average_2018_PM10))