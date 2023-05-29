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

#연도가 2018인 경우
#print(selected_df['issueDate']).unique()
months = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
df_2018_PM25 = []
df_2018_PM10 = []

for month in months:
    #print('\n df_2018_pm25')
    df_2018_month_PM25 = df_PM25[df_PM25['issueDate'].str.contains(f'2018-{month:02d}')]
    issueVal_2018_month_PM25 = df_2018_month_PM25.describe().round()
    #print(f'#issueVal_2018_{month}_PM25')
    #print(issueVal_2018_month_PM25)
    df_2018_PM25.append(issueVal_2018_month_PM25)
    #print('-' * 40)

    #print('\n df_2018_pm10')
    df_2018_month_PM10 = df_PM10[df_PM10['issueDate'].str.contains(f'2018-{month:02d}')]
    issueVal_2018_month_PM10 = df_2018_month_PM10.describe().round()
    #print(f'#issueVal_2018_{month}_PM25')
    #print(issueVal_2018_month_PM10)
    df_2018_PM10.append(issueVal_2018_month_PM10)
    #print('-' * 40)

df_2018_PM25 = pd.concat(df_2018_PM25, axis=1)
df_2018_PM25.columns = ['2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08', '2018-09', '2018-10', '2018-11', '2018-12']
df_2018_PM25.index.name = '2018_PM25'
print(df_2018_PM25)
print('-' * 40)

df_2018_PM10 = pd.concat(df_2018_PM10, axis=1)
df_2018_PM10.columns = ['2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08', '2018-09', '2018-10', '2018-11', '2018-12']
df_2018_PM10.index.name = '2018_PM10'
print(df_2018_PM10)

#생성한 데이터프레임을 csv파일로 저장
df_2018_PM25.to_csv('df_2018_PM25.csv', index=True, encoding='utf-8')
print('df_2018_PM25.csv saved....')

df_2018_PM10.to_csv('df_2018_PM10.csv', index=True, encoding='utf-8')
print('df_2018_PM10.csv saved....')

#total
totalframe_2018 = pd.concat([df_2018_PM25, df_2018_PM10], keys=['df_2018_PM25', 'df_2018_PM10'])
totalframe_2018.index.name = '2018_totalData'
print(totalframe_2018)
totalframe_2018.to_csv('df_total_2018.csv', index=True, encoding='utf-8')
print('df_total_2018.csv saved....')
print('-'*50)
print(totalframe_2018.index.name)
print('-'*50)

df_2018_Trans = pd.concat([df_2018_PM25.T, df_2018_PM10.T], keys=['df_2018_PM25', 'df_2018_PM10'])
print(df_2018_Trans)
print('-' * 50)

#연도가 2019~2022인 경우
data_year = {}
for year in range(2019, 2023):
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    data_year[f'df_{year}_PM25'] = []
    data_year[f'df_{year}_PM10'] = []

    for month in months:
        # print('\n df_2018_pm25')
        df_year_month_PM25 = df_PM25[df_PM25['issueDate'].str.contains(f'{year}-{month:02d}')]
        issueVal_year_month_PM25 = df_year_month_PM25.describe().round()
        # print(f'#issueVal_{year}_{month}_PM25')
        # print(issueVal_year_month_PM25)
        data_year[f'df_{year}_PM25'].append(issueVal_year_month_PM25)
        # print('-' * 40)

        # print('\n df_2018_pm10')
        df_year_month_PM10 = df_PM10[df_PM10['issueDate'].str.contains(f'{year}-{month:02d}')]
        issueVal_year_month_PM10 = df_year_month_PM10.describe().round()
        # print(f'#issueVal_{year}_{month}_PM10')
        # print(issueVal_year_month_PM10)
        data_year[f'df_{year}_PM10'].append(issueVal_year_month_PM10)
        # print('-' * 40)

    df_year_PM25 = pd.concat(data_year[f'df_{year}_PM25'], axis=1)
    df_year_PM25.columns = [f'{year}-{month:02d}' for month in months]
    df_year_PM25.index.name = f'{year}_PM25'
    print(df_year_PM25)
    print('-' * 40)

    df_year_PM10 = pd.concat(data_year[f'df_{year}_PM10'], axis=1)
    df_year_PM10.columns = [f'{year}-{month:02d}' for month in months]
    df_year_PM10.index.name = f'{year}_PM10'
    print(df_year_PM10)
    print('-' * 40)

    # 생성한 데이터프레임을 csv파일로 저장
    df_year_PM25.to_csv(f'df_{year}_PM25.csv', index=True, encoding='utf-8')
    print(f'df_{year}_PM25.csv saved....')

    df_year_PM10.to_csv(f'df_{year}_PM10.csv', index=True, encoding='utf-8')
    print(f'df_{year}_PM10.csv saved....')

    #total
    totalframe_year = pd.concat([df_year_PM25, df_year_PM10], keys=[f'df_{year}_PM25', f'df_{year}_PM10'])
    totalframe_year.index.name = f'{year}_totalData'
    print(totalframe_year)
    totalframe_year.to_csv(f'df_total_{year}.csv', index=True, encoding='utf-8')
    print(f'df_total_{year}.csv saved....')
    print('-' * 50)
    #print(totalframe_year.index.name)
    #print('-' * 50)

    df_year_Trans = pd.concat([df_year_PM25.T, df_year_PM10.T], keys=[f'df_{year}_PM25', f'df_{year}_PM10'])
    print(df_year_Trans)
    print('-' * 50)

#연도가 2023인 경우
#print(selected_df['issueDate']).unique()
months = [1, 2, 3, 4, 5]
df_2023_PM25 = []
df_2023_PM10 = []

for month in months:
    #print('\n df_2023_pm25')
    df_2023_month_PM25 = df_PM25[df_PM25['issueDate'].str.contains(f'2023-{month:02d}')]
    issueVal_2023_month_PM25 = df_2023_month_PM25.describe().round()
    #print(f'#issueVal_2023_{month}_PM25')
    #print(issueVal_2023_month_PM25)
    df_2023_PM25.append(issueVal_2023_month_PM25)
    #print('-' * 40)

    #print('\n df_2023_pm10')
    df_2023_month_PM10 = df_PM10[df_PM10['issueDate'].str.contains(f'2023-{month:02d}')]
    issueVal_2023_month_PM10 = df_2023_month_PM10.describe().round()
    #print(f'#issueVal_2023_{month}_PM25')
    #print(issueVal_2023_month_PM10)
    df_2023_PM10.append(issueVal_2023_month_PM10)
    #print('-' * 40)

df_2023_PM25 = pd.concat(df_2023_PM25, axis=1)
df_2023_PM25.columns = [f'2023-{month:02d}' for month in months]
df_2023_PM25.index.name = '2023_PM25'
print(df_2023_PM25)
print('-' * 40)

df_2023_PM10 = pd.concat(df_2023_PM10, axis=1)
df_2023_PM10.columns = [f'2023-{month:02d}' for month in months]
df_2023_PM10.index.name = '2023_PM10'
print(df_2023_PM10)

#생성한 데이터프레임을 csv파일로 저장
df_2023_PM25.to_csv('df_2023_PM25.csv', index=True, encoding='utf-8')
print('df_2023_PM25.csv saved....')

df_2023_PM10.to_csv('df_2023_PM10.csv', index=True, encoding='utf-8')
print('df_2023_PM10.csv saved....')
print('-'*50)

#makePlot
totalframe_2023 = pd.concat([df_2023_PM25, df_2023_PM10], keys=['df_2023_PM25', 'df_2023_PM10'])
totalframe_2023.index.name = '2023_totalData'
print(totalframe_2023)
totalframe_2023.to_csv('df_total_2023.csv', index=True, encoding='utf-8')
print('df_total_2023.csv saved....')
print('-'*50)
print(totalframe_2023.index.name)
print('-'*50)

df_2023_Trans = pd.concat([df_2023_PM25.T, df_2023_PM10.T], keys=['df_2023_PM25', 'df_2023_PM10'])
print(df_2023_Trans)
print('-' * 50)