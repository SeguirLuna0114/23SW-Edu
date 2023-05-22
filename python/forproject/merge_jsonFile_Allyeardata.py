import json

#2018 데이터
with open('xx2018_UlfptcaAlarmInfo.json', 'r', encoding='utf-8') as file:
    data2018 = json.load(file)

# 2019 데이터
with open('xx2019_UlfptcaAlarmInfo.json', 'r', encoding='utf-8') as file:
    data2019 = json.load(file)

# 2020 데이터
with open('xx2020_UlfptcaAlarmInfo.json', 'r', encoding='utf-8') as file:
    data2020 = json.load(file)

# 2018 데이터
with open('xx2021_UlfptcaAlarmInfo.json', 'r', encoding='utf-8') as file:
    data2021 = json.load(file)

# 2021 데이터
with open('xx2022_UlfptcaAlarmInfo.json', 'r', encoding='utf-8') as file:
    data2022 = json.load(file)

# 2022 데이터
with open('xx2023_UlfptcaAlarmInfo.json', 'r', encoding='utf-8') as file:
    data2023 = json.load(file)

#병합
merged_yearData = data2018 + data2019 + data2020 + data2021 + data2022 + data2023

savedFilename = 'xxAll_UlfptcaAlarmInfo.json'

with open(savedFilename, 'w', encoding='utf-8') as file:
    json.dump(merged_yearData, file, indent=4, sort_keys=True, ensure_ascii=False)

print(savedFilename, ' file saved...')