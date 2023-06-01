import pandas as pd
import matplotlib.pyplot as plt
import json

plt.rcParams['font.family'] = 'Malgun Gothic' #Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정

json_file = 'XXXAll_UlfptcaAlarmInfo.json'
with open(json_file, 'r', encoding='utf-8') as file:
    dataUlfptcaAlarms = json.load(file)  ##json.loads()함수: file을 json으로 변환

#print(dataUlfptcaAlarms)
#print(type(dataUlfptcaAlarms))

myframe = pd.DataFrame(dataUlfptcaAlarms)
#print('데이터프레임 myframe 출력')
#print(myframe)
myframe['issueVal'] = myframe['issueVal'].astype(int)

selected_df = pd.DataFrame(dataUlfptcaAlarms, columns=['districtName', 'issueDate', 'issueGbn', 'issueVal', 'itemCode', 'moveName', 'sn'])
selected_df = selected_df.set_index('sn')
selected_df['issueVal'] = selected_df['issueVal'].astype(int)
#print(selected_df)

# newdf_year를 활용하여 막대 그래프 작성
df_PM25 = selected_df[selected_df['itemCode'] == 'PM25']
df_PM10 = selected_df[selected_df['itemCode'] == 'PM10']

#df25의 연도별 describe
year_df25 = {}
for year in range(2018, 2024):
    year_df25[f'df_{year}_PM25'] = []
    df_YearData_PM25 = df_PM25[df_PM25['issueDate'].str.contains(f'{year}-')]
    issueVal_year_PM25 = df_YearData_PM25.describe().round().T
    issueVal_year_PM25.rename(index={'issueVal' : f'{year}'}, inplace=True)
    #issueVal_year_PM25.index.name = f'{year}_PM25'
    #print(issueVal_year_PM25)
    #year_df25[f'df_{year}_PM25'].append(issueVal_year_PM25)
    year_df25[f'df_{year}_PM25'] = issueVal_year_PM25
    print(issueVal_year_PM25)
    #print(year_df25[f'df_{year}_PM25'])
    print('-'*40)

#PM25_year = pd.concat(year_df25[f'df_{year}_PM25'], axis=1)
PM25_year = pd.concat(year_df25.values(), axis=0)
#PM25_year.index.name = 'PM25'
print(PM25_year)
print('-' * 40)

#df10의 연도별 describe
year_df10 = {}
for year in range(2018, 2024):
    year_df10[f'df_{year}_PM10'] = []
    df_YearData_PM10 = df_PM10[df_PM10['issueDate'].str.contains(f'{year}-')]
    issueVal_year_PM10 = df_YearData_PM10.describe().round().T
    issueVal_year_PM10.rename(index={'issueVal' : f'{year}'}, inplace=True)
    #issueVal_year_PM10.index.name = f'{year}_PM10'
    #print(issueVal_year_PM10)
    #year_df10[f'df_{year}_PM10'].append(issueVal_year_PM10)
    year_df10[f'df_{year}_PM10'] = issueVal_year_PM10
    print(issueVal_year_PM10)
    #print(year_df10[f'df_{year}_PM10'])
    print('-'*40)

#PM10_year = pd.concat(year_df10[f'df_{year}_PM10'], axis=1)
PM10_year = pd.concat(year_df10.values(), axis=0)
#PM10_year.index.name = 'PM10'
print(PM10_year)
print('-'*40)

totalItemCode = pd.concat([PM25_year, PM10_year], keys=['PM25', 'PM10'])
print(totalItemCode)
totalItemCode.to_csv('df_totalItemCode.csv', index=True, encoding='utf-8')
print('Dataframe saved to CSV file....')

#생성된 데이터프레임 PM25_year와 PM10_year을 활용하여 plot생성
totalItemCode_selected = totalItemCode[['count', 'mean', 'std', 'min', 'max']]
print(totalItemCode_selected)
totalItemCode_selected.plot(kind='box', marker='o', rot=0)

plt.plot(PM25_year.columns, 'b', marker='o', label='PM25')

plt.title('국내 미세먼지의 전체적인 시간변동성')
plt.xlabel('time(Year)')
plt.ylabel('기초 통계 정보')
plt.legend()
plt.show()
