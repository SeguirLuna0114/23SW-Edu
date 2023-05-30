import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np

plt.rcParams['font.family'] = 'Malgun Gothic' #Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정

json_file = 'XXXAll_UlfptcaAlarmInfo.json'
with open(json_file, 'r', encoding='utf-8') as file:
    dataUlfptcaAlarms = json.load(file)  ##json.loads()함수: file을 json으로 변환

selected_df = pd.DataFrame(dataUlfptcaAlarms, columns=['districtName', 'issueDate', 'issueGbn', 'issueVal', 'itemCode', 'moveName', 'sn'])
selected_df = selected_df.set_index('sn')
selected_df['issueVal'] = selected_df['issueVal'].astype(int)
selected_df['issueDate'] = pd.to_datetime(selected_df['issueDate'])
selected_df.fillna(0, inplace=True) #selected_df의 NaN 값이 모두 0으로 대체되어 원본이 변경되어 출력됨

#수도권 & 연도별 데이터프레임 생성
citylist = selected_df['districtName'].unique()
listData = ['PM25', 'PM10']
for city in citylist:
    result_data = [] #데이터 초기화
    for PMdata in listData:
        print(f'{city}의 월별 {PMdata} 농도 추세')
        df_PMdata = selected_df.loc[(selected_df['districtName'] == city) & (selected_df['itemCode'] == PMdata), ['itemCode', 'issueDate', 'issueVal']]

        for year in range(2018, 2024):
            #print(f'{year}년도 데이터')
            df_YearPMdata = df_PMdata[df_PMdata['issueDate'].dt.year == year]
            months = df_YearPMdata['issueDate'].dt.month.unique()

            for month in months:
                df_MonthPMdata = df_YearPMdata[df_YearPMdata['issueDate'].dt.month == month]
                avg_issueVal_month = np.round(df_MonthPMdata['issueVal'].mean(skipna=True))
                #print(f'{year}년 {month}월 {PMdata}')
                #print(avg_issueVal_month)
                #print('-' * 40)
                result_data.append([city, PMdata, f'{year}년 {month}월', avg_issueVal_month])
    Df_Result = pd.DataFrame(result_data, columns=['발령 지역 명', '미세먼지 항목 구분', '발령 연도별 월', '평균 미세먼지 농도'])
    print(Df_Result)

    df_PM25 = Df_Result[Df_Result['미세먼지 항목 구분'] == 'PM25']
    df_PM10 = Df_Result[Df_Result['미세먼지 항목 구분'] == 'PM10']
    #kind='line'
    plt.plot(df_PM25['발령 연도별 월'], df_PM25['평균 미세먼지 농도'], color='#FF00FF', label='PM25', marker='o')
    plt.xlabel('경보발령 연도-월')
    plt.ylabel('평균 미세먼지 농도')
    plt.title(f'{city}의 월별 초미세먼지(PM25) 농도 추세')
    plt.legend()
    plt.savefig(f'./MonthlyImage/{city}_월별_초미세먼지(PM25) 추세.png')
    print(f'{city}_월별_초미세먼지(PM25) 추세.png file saved~!!')
    plt.show()

    plt.plot(df_PM10['발령 연도별 월'], df_PM10['평균 미세먼지 농도'], color='#00FF00', label='PM10', marker='s')
    plt.xlabel('경보발령 연도-월')
    plt.ylabel('평균 미세먼지 농도')
    plt.title(f'{city}의 월별 미세먼지(PM10) 농도 추세')
    plt.legend()
    plt.savefig(f'./MonthlyImage/{city}_월별_미세먼지(PM10) 추세.png')
    print(f'{city}_월별_미세먼지(PM10) 추세.png file saved~!!')
    plt.show()

    plt.clf()
