import pandas as pd
import matplotlib.pyplot as plt
import json
import numpy as np
import seaborn as sns

plt.rcParams['font.family'] = 'Malgun Gothic'  # Matplotlib의 기본 글꼴을 'Malgun Gothic'으로 설정

json_file = 'XXXAll_UlfptcaAlarmInfo.json'
with open(json_file, 'r', encoding='utf-8') as file:
    dataUlfptcaAlarms = json.load(file)  ##json.loads()함수: file을 json으로 변환

selected_df = pd.DataFrame(dataUlfptcaAlarms, columns=['districtName', 'issueDate', 'issueGbn', 'issueVal', 'itemCode', 'moveName'])
#selected_df = selected_df.set_index('sn')
selected_df['issueVal'] = selected_df['issueVal'].astype(int)
selected_df['issueDate'] = pd.to_datetime(selected_df['issueDate'])
selected_df.fillna(0, inplace=True)  # selected_df의 NaN 값이 모두 0으로 대체되어 원본이 변경되어 출력됨

# '분기' 필드 형성
citylist = selected_df['districtName'].unique()
listData = ['PM25', 'PM10']

result_data = []
for city in citylist:
    for PMdata in listData:
        #print(f'{city}의 분기별 {PMdata} 농도 추세')
        df_PMdata = selected_df.loc[(selected_df['districtName'] == city) & (selected_df['itemCode'] == PMdata), ['districtName', 'itemCode', 'issueDate', 'issueVal']]

        df_YearPMdata_list = []
        for year in range(2018, 2024):
            #print(f'{year}년도 데이터')
            df_YearPMdata = df_PMdata.loc[df_PMdata['issueDate'].dt.year == year, ['districtName', 'itemCode', 'issueDate', 'issueVal']]
            months = df_YearPMdata['issueDate'].dt.month.unique()
            #df_YearPMdata['Quarter'] = ''

            df_Quarter_list = []
            for month in months: # month변수의 값에 따라 분기값을 설정
                if month in range(1, 4):
                    quarter = f'{year}년도 1분기'
                    #df_YearPMdata.loc[df_YearPMdata['issueDate'].dt.month.isin([1, 2, 3]), 'quarter'] = quarter
                    df_Q1 = df_YearPMdata.loc[df_YearPMdata['issueDate'].dt.month.isin([1, 2, 3]), ['districtName', 'itemCode', 'issueDate', 'issueVal']]
                    df_Q1.loc[:, 'Quarter'] = quarter
                    df_Quarter_list.append(df_Q1)
                elif month in range(4, 7):
                    quarter = f'{year}년도 2분기'
                    #df_YearPMdata.loc[df_YearPMdata['issueDate'].dt.month.isin([1, 2, 3]), 'quarter'] = quarter
                    df_Q2 = df_YearPMdata.loc[df_YearPMdata['issueDate'].dt.month.isin([4, 5, 6]), ['districtName', 'itemCode', 'issueDate', 'issueVal']]
                    df_Q2.loc[:, 'Quarter'] = quarter
                    df_Quarter_list.append(df_Q2)
                elif month in range(7, 10):
                    quarter = f'{year}년도 3분기'
                    df_Q3 = df_YearPMdata.loc[df_YearPMdata['issueDate'].dt.month.isin([7, 8, 9]), ['districtName', 'itemCode', 'issueDate', 'issueVal']]
                    df_Q3.loc[:, 'Quarter'] = quarter
                    df_Quarter_list.append(df_Q3)
                elif month in range(10, 13):
                    quarter = f'{year}년도 4분기'
                    df_Q4 = df_YearPMdata.loc[df_YearPMdata['issueDate'].dt.month.isin([10, 11, 12]), ['districtName', 'itemCode', 'issueDate', 'issueVal']]
                    df_Q4.loc[:, 'Quarter'] = quarter
                    df_Quarter_list.append(df_Q4)

            if df_Quarter_list:
                df_YearPMdata_quarter = pd.concat(df_Quarter_list, ignore_index=True, axis=0)
                df_YearPMdata_list.append(df_YearPMdata_quarter)
            #print(df_YearPMdata_list)
        if df_YearPMdata_list:
            df_YearPMdata_all = pd.concat(df_YearPMdata_list, ignore_index=True, axis=0)
            result_data.append(df_YearPMdata_all)
            #print(df_YearPMdata_all)

Df_Result = pd.concat(result_data, ignore_index=True, axis=0)
print(Df_Result)
print('-'*50)
#print(Df_Result['Quarter'].unique())

#boxplot생성
#sns.set_style("darkgrid")
for q in Df_Result['Quarter'].unique():
    plt.figure(figsize=(12, 6))
    plt.title(f'{q} 각 도시의 미세먼지 농도 Boxplot')
    sns.boxplot(data=Df_Result, x='districtName', y='issueVal', hue='itemCode')
    plt.xlabel(f'{q} 각 도시별 미세먼지 농도')
    plt.ylabel('미세먼지 농도')
    plt.legend()
    plt.savefig(f'./QuaterBoxplot/{q}_도시별_미세먼지 농도 추세.png', dpi=400, bbox_inches='tight')
    plt.show()