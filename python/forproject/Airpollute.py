#빈 리스트 jsonResult를 생성합니다. 이 리스트는 모든 결과를 저장
jsonResult = []
nPage = 0
while(True):
    print('pageNo : %d, nPage : %d' % (pageNo, nPage))  # 현재 페이지 번호와 총 페이지 개수를 출력
    jsonData = getArpltInfoData(pageNo, numOfRows)
    print(jsonData)

    if (jsonData['response']['header']['resultCode'] == '00'):
        totalCount = jsonData['response']['body']['totalCount']
        print('데이터 총 개수 : ', totalCount)

        for item in jsonData['response']['body']['items']:
            jsonResult.append(item)  #가져온 데이터를 jsonResult 리스트에 추가

        if totalCount == 0:  # 데이터의 총 개수가 0인 경우(데이터가 더이상 없는 경우), 루프를 종료
            break

        # 총 페이지 개수 계산
        nPage = math.ceil(totalCount / numOfRows)  # 한 페이지당 결과 개수인 numOfRows로 나눈 뒤, 올림

        if (pageNo == nPage):  # 만약 현재 페이지 번호가 총 페이지 개수와 같다면, 루프를 종료
            break
        pageNo += 1  # 현재 페이지 번호인 pageNo를 1 증가

    else:  # 위의 조건들을 만족하지 않을 경우, 루프를 종료
        break

    savedFilename = 'xx_getMinuDustFrcstDspth.json'  # 저장할 파일 명 설정

    # jsonResult에 저장된 데이터를 JSON 형식으로 변환하여 파일에 저장
    # with 문을 사용 => 파일을 열고 사용한 후에 자동으로 닫히도록 보장
    with open(savedFilename, 'w', encoding='utf-8') as outfile:  # 파일을 쓰기 모드로 열기
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)  # jsonResult 리스트를 JSON 형식으로 변환
        # json.dumps() 함수를 사용하여 jsonResult를 JSON 문자열로 변환
        # indent 매개변수: 들여쓰기 칸 수 설정
        # sort_keys=True: 키를 기준으로 정렬
        # ensure_ascii=False: 유니코드 문자를 그대로 유지

        outfile.write(retJson)  # JSON 데이터를 파일에 쓰기

print(savedFilename + ' file saved..')