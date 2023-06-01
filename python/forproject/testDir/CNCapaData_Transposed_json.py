import pandas as pd
import json

#CNCapaData_Transposed_All.csv -> CNCapaData_Transposed_All.json
csv_data = pd.read_csv("CNCapaData_Transposed_All.csv", sep=",", skiprows=7, engine='python')
#skiprows: 위에서부터 n개의 행 삭제
data_dict = csv_data.to_dict(orient="records")
final_dict = {"CNCapaData_All": data_dict}

with open("CNCapaData_Transposed_All.json", "w", encoding="utf-8") as json_file:
    json.dump(final_dict, json_file, ensure_ascii=False)

#CNCapaData_Transposed.csv -> CNCapaData_Transposed.json
csv_data2 = pd.read_csv("CNCapaData_Transposed.csv", sep=",", skiprows=1, engine='python')
#skiprows: 위에서부터 n개의 행 삭제
data_dict2 = csv_data2.to_dict(orient="records")
final_dict2 = {"CNCapaData": data_dict2}

with open("CNCapaData_Transposed.json", "w", encoding="utf-8") as json_file2:
    json.dump(final_dict2, json_file2, ensure_ascii=False)
