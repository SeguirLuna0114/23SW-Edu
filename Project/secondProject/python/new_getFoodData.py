import json 
import pandas as pd
from pandas import DataFrame as df
import pymongo
from pymongo import MongoClient
import json, datetime, math
import requests
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

def getRequestUrl(url):
    res = requests.get(url)
    try:
        if res.status_code == 200:
            return res
    except Exception as e:
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

# 현재 opneAPI를 불러올 준비물을 생성한다.
# 관련 get_secret을 통하여 url을 만들고 getRequestUrl의 에약어를 사용하여 받아온다.
# 정상작동 하는 경우에는 json.loads(res.text)를 한다.
def getFoodData(pageNo, numOfRows):
    end_point = 'https://apis.data.go.kr/1471000/FoodNtrIrdntInfoService1/getFoodNtrItdntList1'

    parameters = ''
    parameters += "?serviceKey=" + get_secret("data_apiKey")
    parameters += "&pageNo=" + str(pageNo)
    parameters += "&numOfRows=" + str(numOfRows)
    parameters += "&type=json" 
    url = end_point + parameters
    
    res = getRequestUrl(url)
    if (res == None):
        return None
    else:
        dict_json = json.loads(res.text) 
        return dict_json

# opneAPI를 json형식으로 불러온다.
def NewData():
    jsonResult = []
    pageNo = 1  
    numOfRows = 100
    nPage = 0
    while(True):
        print('pageNo : %d, nPage : %d' % (pageNo, nPage))
        jsonData = getFoodData(pageNo, numOfRows)
        print(jsonData)

        if (jsonData['header']['resultCode'] == '00'):
            totalCount = jsonData['body']['totalCount']
            print('데이터 총 개수 : ', totalCount)  

            for item in jsonData['body']['items']:
                jsonResult.append(item)

            if totalCount == 0:
                break
            # nPage = math.ceil(totalCount / numOfRows)
            if (pageNo == 10):  
                break  

            pageNo += 1
        else :
            break
    return jsonResult

# 해당 위의 단계는 json형식으로 수집하는 단계이다 현재 부터는 DataFarme 형식으로 가공하는 단계이다.
# 우선 컬럼이 코드로 되었이기에 변경하고 불필요한 데이터를 삭제했다.
# 그 후 최신 연도로 업데이트를 하기 위해서 sort_values와 drop_duplicates 사용하여 연도로 정렬 후 마지막날의 식품이름을 keep했다 이렇게 되면 최신날짜로 없데이트가 가능하다.
# 그리고 인덱스를 제정의하고 nan을 0으로 바꿔준다.
def first_process(myframe):
    myframe = NewData()
    df = pd.DataFrame(list(myframe))
    newdf = df.drop(['ANIMAL_PLANT'], axis=1)

    mycolumn = ['식품이름','1회제공량','열량','탄수화물','단백질','지방','당류','나트륨','콜레스테롤','포화지방산','트랜스지방산','연도']
    newdf.columns = mycolumn
    food_update = newdf[(newdf["1회제공량"] != "0")]
    new_Data = food_update.reset_index(drop=True)
    new_Data = new_Data.sort_values("연도")
    set_food = new_Data.drop_duplicates(["식품이름"], keep = 'last')
    new_set_food = set_food.reset_index(drop=True)
    new_set_food = new_set_food.replace('N/A', 0)
    return new_set_food
   
# 1회제공량을 100g으로 설정해야하기에 object타입을 float타입으로 전환 후에 연산을 했다.
def format_process(format_data):
    for _ in format_data.columns:
      if (_ == '연도') or (_ == '식품이름'): 
          print(f'{_}는 포맷을 안합니다')
      else:
        format_data = format_data.astype({ _ : 'float'})
        print(f'{_} 포맷')


    cnt = 0
    for i in format_data["1회제공량"]:
      if i == 100.0:
        cnt += 1
      else:
        change = 100 / i

        kal = format_data.loc[cnt,"열량"] 
        carbohy = format_data.loc[cnt,"탄수화물"]
        protein = format_data.loc[cnt,"단백질"] 
        fat = format_data.loc[cnt,"지방"] 
        suars = format_data.loc[cnt,"당류"] 
        na = format_data.loc[cnt,"나트륨"] 
        col = format_data.loc[cnt,"콜레스테롤"] 
        poh = format_data.loc[cnt,"포화지방산"] 
        trans = format_data.loc[cnt,"트랜스지방산"] 

        format_data.loc[cnt,"열량"] = kal * change
        format_data.loc[cnt,"탄수화물"] = carbohy * change
        format_data.loc[cnt,"단백질"] = protein * change
        format_data.loc[cnt,"지방"] = fat * change
        format_data.loc[cnt,"당류"] = suars * change
        format_data.loc[cnt,"나트륨"] = na * change
        format_data.loc[cnt,"콜레스테롤"] = col * change
        format_data.loc[cnt,"포화지방산"] = poh * change
        format_data.loc[cnt,"트랜스지방산"] = trans * change
        format_data.loc[cnt,"1회제공량"] = i * change
        
        cnt += 1
    new_set_food1 = format_data.round()
    return new_set_food1

# 이 데이터의 핵심인 식품이름의 이름이 모호한 기준이다 예를들어 귀리이면 귀리,
# 마른것 귀리, 구운것 이런 단어들이 존재하기에 가공에 들어갔다.
def final_process(final_data):
    sample_data = final_data.copy()
    sample_data["횟수"] = [len(str(sample_data["식품이름"].iloc[i]).split(",")) for i in range(len(sample_data))]
    sample_data["식품이름"] = [str(sample_data["식품이름"].iloc[i]).split(",") for i in range(len(sample_data))]
    sample_data_1 = sample_data[sample_data["횟수"] == 1].reset_index(drop=True)
    sample_data_2 = sample_data[sample_data["횟수"] == 2].reset_index(drop=True)
    sample_data_3 = sample_data[sample_data["횟수"] == 3].reset_index(drop=True)

    cnt = 0 
    for _ in sample_data_1["식품이름"]:
        sample_data_1.loc[cnt, "식품이름"] = _[0]
        cnt += 1

    sample_list = []
    sample_set = []
    for i in sample_data_2["식품이름"]:
        if i[1] in sample_list:
          sample_set.append(i[1])
        else:
          sample_list.append(i[1])

    set_list = list(set(sample_set))

    cnt = 0 
    for i in sample_data_2["식품이름"]:
      if i[1] in set_list:
        sample_data_2.loc[cnt, "식품이름"] = i[0]
        sample_data_2.loc[cnt, "종류"] = i[1]
        cnt += 1
      else:
        sample_data_2.loc[cnt, "식품이름"] = i[1]
        sample_data_2.loc[cnt, "종류"] = i[0]
        cnt += 1

    drop_list = ["통곡물로든든한아침을만들면", "1", "베지밀칼슘가득두유검은깨", "미스터칩스치즈맛콘칩(옥수수66.49%", '허니앤아몬드쇼트브레드(꿀4%', "노리마끼치즈(김2.06%", "켄돈2컬러(오렌지, 탕고와퍼렌야초콜릿(코코아분말5%", "크롤리푸드버터크림초콜릿크레커(코코아분말3%", "피쉬크래커카라멜(실꼬리돔40%", "피쉬크래커커틀피쉬(실꼬리돔40%"]
    revers_list = ["도우넛", "된장", "곤약", "딸기맛요구르트", "삼각김밥", "너구리", "스파게티"]

    cnt = 0
    for _ in sample_data_2["종류"]:
      if _ in drop_list:
        sample_data_2 = sample_data_2[sample_data_2["종류"] != _]
        cnt += 1
      elif _ in revers_list:
        sample_data_2.loc[cnt, "종류"] = sample_data_2.loc[cnt, "식품이름"]
        sample_data_2.loc[cnt, "식품이름"] = _
        cnt += 1
      else:
        cnt += 1
        
    f_list = ['피자', '샌드위치']
    
    cnt = 0
    for i in sample_data_3["식품이름"]:
      if i in f_list:
        sample_data_3 = sample_data_3[sample_data_3["식품이름"] != _]
        cnt += 1
      else:
        sample_data_3.loc[cnt, "종류"] = i[1]
        sample_data_3.loc[cnt, "식품이름"] = i[0]
        cnt += 1

    sample_data_1["종류"] = ""
    new_data = pd.concat([sample_data_1, sample_data_2, sample_data_3], axis = 0).reset_index(drop=True)
    new_data = new_data.drop(["연도", "종류", "횟수"], axis= 1)
    # new_data = pd.to_dict(new_data)
    new_data = new_data.to_dict("records")
    print(new_data)
    client = MongoClient('mongodb://192.168.1.78:27017/')
    db = client['test']
    collection_name = 'FoodData'
    collection = db[collection_name]
    collection.insert_many(new_data)
    client.close()  
    return new_data[0]
  
# 위 해당코드들을 한번에 선언할수 있는 코드다.
def arrange_code():
  myframe = NewData()
  format_data = first_process(myframe)
  final_data = format_process(format_data)
  final_data = final_process(final_data)
  return final_data

# arrange_code()