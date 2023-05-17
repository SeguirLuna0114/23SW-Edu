from fastapi import FastAPI #FastAPI 애플리케이션을 만들기 위해 사용

app = FastAPI() #FastAPI 클래스의 인스턴스를 생성하여 app 변수에 할당. 웹 애플리케이션의 핵심이 되는 객체

@app.get('/')
async def healthCheck():
    return "OK"

@app.get('/hello')
async def Hello():
    return "Hello World~!!"

@app.get('/random')
async def random(max=None):
    import random

    if max is None:
        max = 10
    else:
        max = int(max)
    random_v = random.randint(1, max)

    return random_v