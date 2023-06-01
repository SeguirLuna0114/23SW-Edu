import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

def generate_Ulfptca_graph(year):
    plt.rcParams['font.family'] = 'Malgun Gothic'

    json_file = f'xx{year}_UlfptcaAlarmInfo.json'

    with open(json_file, 'r', encoding='utf-8') as file:
        dataUlfptcaAlarms = json.load(file)  ##json.loads()함수: file을 json으로 변환

    # 데이터프레임 생성
    myframe_year = pd.DataFrame(dataUlfptcaAlarms)
    print(f'\n# {year} 데이터프레임 myframe_year 출력')
    print(myframe_year)
    myframe_year['issueVal'] = myframe_year['issueVal'].astype(int)

    # 필요한 columns만 가져와서 새로운 데이터프레임 생성
    print('\n# 필요한 columns만 가져와서 새로운 데이터프레임 생성')
    if 'itemCode' in myframe_year.columns:
        myframe_year = myframe_year[['districtName','issueGbn', 'issueDate', 'issueTime', 'issueVal', 'itemCode', 'moveName']]
        print(myframe_year)

        # 'districtName'가 같은 행을 기준으로 그룹화하여 'issueDate'별 'issueVal'의 평균을 계산
        print(f'\n \'districtName\'가 같은 행을 기준으로 그룹화한 {year} 데이터프레임')
        newdf_year = myframe_year.groupby(['districtName', 'issueDate', 'itemCode'])['issueVal'].mean().apply(np.ceil).reset_index()
        print(newdf_year)

        # newdf_year를 활용하여 막대 그래프 작성
        df_PM25 = newdf_year[newdf_year['itemCode'] == 'PM25']
        df_PM10 = newdf_year[newdf_year['itemCode'] == 'PM10']

        if not df_PM25.empty and not df_PM10.empty:
            # 그래프 생성
            plt.bar(df_PM25['districtName'], df_PM25['issueVal'], color='red', label='PM25')
            plt.bar(df_PM10['districtName'], df_PM10['issueVal'], color='blue', label='PM10', alpha=0.5)  # alpha 값을 조정하여 투명도 조절

            plt.title(f'{year}년도 지역별 미세먼지 지수')
            plt.xticks(rotation=0)
            plt.yticks(range(int(min(newdf_year['issueVal'])), int(max(newdf_year['issueVal']))+1, 100))
            plt.ylabel('미세먼지 지수')
            plt.xlabel('지역')
            plt.legend()

            plt.show()
        else:
            print(f'{year} 데이터에는 "PM25" 또는 "PM10" 아이템이 없습니다.')
    else:
        print(f'{year} 데이터에는 "itemCode" 열이 없습니다.')

#연도별 그래프 생성
years =[2018, 2019, 2020, 2021, 2022, 2023]
for year in years:
    generate_Ulfptca_graph(year)
    print(f'{year} Ulfptca graph is generated~!!')

    filename = f'xx{year}_UlfptcaAlarmInfo_Dist_IssueVal.png'
    plt.savefig(filename, dpi=400, bbox_inches='tight')
    print(filename + 'Saved...')