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

#수도권 별 인 데이터프레임 생성
citylist = selected_df['districtName'].unique()
listData = ['PM25', 'PM10']

for city in citylist:
    result_data = [] #데이터 초기화
    for PMdata in listData:
        print(f'{city}의 {PMdata} 농도 추세')
        df_PMdata = selected_df.loc[(selected_df['districtName'] == city) & (selected_df['itemCode'] == PMdata), ['itemCode', 'issueDate', 'issueVal']]
        for year in range(2018, 2024):
            print(f'{year}년도 데이터')
            df_YearPMdata = df_PMdata[df_PMdata['issueDate'].dt.year == year]
            avg_issueVal_year = np.round(df_YearPMdata['issueVal'].mean(skipna=True))
            print(avg_issueVal_year)
            print('-' * 40)
            result_data.append([city, PMdata, year, avg_issueVal_year])
    Df_Result = pd.DataFrame(result_data, columns=['발령 지역 명', '미세먼지 항목 구분', '발령 연도', '평균 미세먼지 농도'])
    print(Df_Result)

    df_PM25 = Df_Result[Df_Result['미세먼지 항목 구분'] == 'PM25']
    df_PM10 = Df_Result[Df_Result['미세먼지 항목 구분'] == 'PM10']
    #kind='line'
    plt.plot(df_PM25['발령 연도'], df_PM25['평균 미세먼지 농도'], color='r', label='PM25')
    plt.plot(df_PM10['발령 연도'], df_PM10['평균 미세먼지 농도'], color='b', label='PM10')
    plt.xlabel('발령 연도')
    plt.ylabel('평균 미세먼지 농도')
    plt.title(f'{city}의 연도별 미세먼지 농도 추세')
    plt.legend()
    plt.savefig(f'{city}연도별_미세먼지 추세.png')
    print(f'{city}_연도별_미세먼지 추세.png file saved~!!')
    # plt.show()
    plt.clf()
