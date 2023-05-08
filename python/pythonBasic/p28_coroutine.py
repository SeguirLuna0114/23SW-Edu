def handler():
    print("Initialize Handler")
    while True: #yield는 호출되면 함수를 나가지 않고, 실행을 멈추고 스코프를 탈출함
        value = (yield) # yield를 parameter로 사용하기 위해서 ()를 사용
        print("Received %s " % value)

listener =  handler()
listener.__next__()
listener.send(1)
listener.send("message")