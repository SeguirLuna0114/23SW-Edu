import pandas as pd
import csv
import os

# XLSX 파일 경로
excel_file = 'FabCapacityData.xlsx'

# CSV 파일 경로
csv_file = 'FabCapacityData.csv'

# XLSX 파일 읽기
data = pd.read_excel(excel_file)

# CSV 파일로 저장
data.to_csv(csv_file, index=False, encoding='utf-8')

# 임시 파일을 생성하여 삭제된 행을 저장할 준비를 합니다
temp_filename = 'temp.csv'

with open(csv_file, 'r', newline='', encoding='utf-8') as file, open(temp_filename, 'w', newline='', encoding='utf-8') as temp_file:
    reader = csv.reader(file)
    writer = csv.writer(temp_file)

    # 첫 번째 행과 두 번째 행을 건너뛰고 나머지 행을 임시 파일에 복사합니다
    for i, row in enumerate(reader):
        if i > 1:  # 첫 번째 행과 두 번째 행을 건너뜁니다
            writer.writerow(row)

# 원본 파일을 삭제하고 임시 파일을 원본 파일명으로 변경합니다
os.remove(csv_file)
os.rename(temp_filename, csv_file)

print('CSV 파일로 변환 완료:', csv_file)
