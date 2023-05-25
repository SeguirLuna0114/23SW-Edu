import json

# 연도 범위: 2018부터 2023까지
for year in range(2018, 2024):
    file_name = 'XXX{}_UlfptcaAlarmInfo.json'.format(year)

    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 데이터 병합
    if year == 2018:
        merged_yearData = data
    else:
        merged_yearData += data

# 병합된 데이터 저장
savedFilename = 'XXXAll_UlfptcaAlarmInfo.json'
with open(savedFilename, 'w', encoding='utf-8') as file:
    json.dump(merged_yearData, file, indent=4, sort_keys=True, ensure_ascii=False)

print(savedFilename, ' file saved...')