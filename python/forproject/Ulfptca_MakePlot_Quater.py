import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np

plt.rcParams['font.family'] = 'Malgun Gothic'  # Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정

json_file = 'XXXAll_UlfptcaAlarmInfo.json'
with open(json_file, 'r', encoding='utf-8') as file:
    dataUlfptcaAlarms = json.load(file)  ##json.loads()함수: file을 json으로 변환

selected_df = pd.DataFrame(dataUlfptcaAlarms, columns=['districtName', 'issueDate', 'issueGbn', 'issueVal', 'itemCode', 'moveName', 'sn'])
selected_df = selected_df.set_index('sn')
selected_df['issueVal'] = selected_df['issueVal'].astype(int)
selected_df['issueDate'] = pd.to_datetime(selected_df['issueDate'])
selected_df.fillna(0, inplace=True)  # selected_df의 NaN 값이 모두 0으로 대체되어 원본이 변경되어 출력됨

# 수도권 & 연도별 데이터프레임 생성
citylist = selected_df['districtName'].unique()
listData = ['PM25', 'PM10']

for city in citylist:
    result_data = []  # 데이터 초기화
    for PMdata in listData:
        print(f'{city}의 분기별 {PMdata} 농도 추세')
        df_PMdata = selected_df.loc[(selected_df['districtName'] == city) & (selected_df['itemCode'] == PMdata), ['itemCode', 'issueDate', 'issueVal']]
        # df_PMdata['issueDate']
        # 분기별 데이터
        for year in range(2018, 2024):
            print(f'{year}년도 데이터')
            df_YearPMdata = df_PMdata[df_PMdata['issueDate'].dt.year == year]
            months = df_YearPMdata['issueDate'].dt.month.unique()

            for month in months: # month변수의 값에 따라 분기값을 설정
                #quater = []
                #avg_quater = []

                if month in range(1, 4):
                    #quater.append(f'{year}년도 1분기')
                    quater = f'{year}년도 1분기'
                    df_MonthPMdata = df_YearPMdata[df_YearPMdata['issueDate'].dt.month.isin([1, 2, 3])] # df_YearPMdata 데이터프레임에서 1,2,3월에 해당하는 데이터를 추출
                    avg_issueVal_quater = np.round(df_MonthPMdata['issueVal'].mean(skipna=True)) # df_MonthPMdata 데이터프레임에서 issueVal열의 값들의 평균 계산
                    #avg_quater.append(avg_issueVal_quater)
                    result_data.append([city, PMdata, year, quater, avg_issueVal_quater])
                    print(f'{year}년도 1분기 : {avg_issueVal_quater}')
                    print('-' * 50)
                elif month in range(4, 7):
                    #quater.append(f'{year}년도 2분기')
                    quater = f'{year}년도 2분기'
                    df_MonthPMdata = df_YearPMdata[df_YearPMdata['issueDate'].dt.month.isin([4, 5, 6])]
                    avg_issueVal_quater = np.round(df_MonthPMdata['issueVal'].mean(skipna=True))
                    result_data.append([city, PMdata, year, quater, avg_issueVal_quater])
                    #avg_quater.append(avg_issueVal_quater)
                    print(f'{year}년도 2분기 : {avg_issueVal_quater}')
                    # print('-' * 50)
                elif month in range(7, 10):
                    #quater.append(f'{year}년도 3분기')
                    quater = f'{year}년도 3분기'
                    df_MonthPMdata = df_YearPMdata[df_YearPMdata['issueDate'].dt.month.isin([7, 8, 9])]
                    avg_issueVal_quater = np.round(df_MonthPMdata['issueVal'].mean(skipna=True))
                    #avg_quater.append(avg_issueVal_quater)
                    result_data.append([city, PMdata, year, quater, avg_issueVal_quater])
                    print(f'{year}년도 3분기 : {avg_issueVal_quater}')
                    print('-' * 50)
                elif month in range(10, 13):
                    #quater.append(f'{year}년도 4분기')
                    quater = f'{year}년도 4분기'
                    df_MonthPMdata = df_YearPMdata[df_YearPMdata['issueDate'].dt.month.isin([10, 11, 12])]
                    avg_issueVal_quater = np.round(df_MonthPMdata['issueVal'].mean(skipna=True))
                    #avg_quater.append(avg_issueVal_quater)
                    result_data.append([city, PMdata, year, quater, avg_issueVal_quater])
                    print(f'{year}년도 4분기 : {avg_issueVal_quater}')
                    print('-' * 50)
                #result_data.append([city, PMdata, year, quater, avg_quater])
            result_data_unique = [x for x in result_data if result_data.count(x) == 1]
            print(result_data_unique)
    Df_Result = pd.DataFrame(result_data_unique, columns=['발령 지역 명', '미세먼지 항목 구분', '발령 연도', '분기', '평균 미세먼지 농도'])
    #Df_Result['분기'] = Df_Result['분기'].apply(lambda x: x[0])
    #Df_Result['평균 미세먼지 농도'] = Df_Result['평균 미세먼지 농도'].apply(lambda x: x[0])
    print(Df_Result)
    Df_Result.to_csv(f'./QuaterDataFrame/{city}의 분기별 미세먼지 농도 추세.csv', encoding='utf-8')
    print(f'{city} file is saved~!!')
    print('-' * 50)