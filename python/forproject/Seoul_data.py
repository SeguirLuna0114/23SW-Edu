import pandas as pd
import matplotlib.pyplot as plt
import json

plt.rcParams['font.family'] = 'Malgun Gothic' #Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정

json_file = 'XXXAll_UlfptcaAlarmInfo.json'
with open(json_file, 'r', encoding='utf-8') as file:
    dataUlfptcaAlarms = json.load(file)  ##json.loads()함수: file을 json으로 변환

#print(dataUlfptcaAlarms)
#print(type(dataUlfptcaAlarms))

selected_df = pd.DataFrame(dataUlfptcaAlarms, columns=['districtName', 'issueDate', 'issueGbn', 'issueVal', 'itemCode', 'moveName', 'sn'])
selected_df = selected_df.set_index('sn')
selected_df['issueVal'] = selected_df['issueVal'].astype(int)

#우리나라 각 대도시의 PM10, PM25 농도 추세
#df_PM25 = selected_df.loc[selected_df['itemCode'] == 'PM25', ['districtName', 'issueDate', 'issueVal']]
#df_PM10 = selected_df.loc[selected_df['itemCode'] == 'PM10', ['districtName', 'issueDate', 'issueVal']]

df_Seoul = selected_df.loc[selected_df['districtName'] == '서울', ['itemCode', 'issueDate', 'issueVal']]
print(df_Seoul)
df_PM25 = df_Seoul[df_Seoul['itemCode'] == 'PM25']
df_PM10 = df_Seoul[df_Seoul['itemCode'] == 'PM10']

plt.plot(df_PM25['issueDate'], df_PM25['issueVal'], 'r', marker='o', label='PM25')
plt.plot(df_PM10['issueDate'], df_PM10['issueVal'], 'b', marker='s', label='PM10')
xlabel = ['2018', '2019', '2020', '2021', '2022', '2023']
plt.title('서울시의 미세먼지 농도 추세')
plt.xlabel(xlabel)
plt.ylabel('미세먼지 농도')
plt.legend()
plt.show()

