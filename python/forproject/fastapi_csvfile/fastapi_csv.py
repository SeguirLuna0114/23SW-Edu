from fastapi import FastAPI 
import pandas as pd 

app = FastAPI()

@app.get('/')
def healthCheck():
    return "OK"

@app.get('/getcsv')
def getcsv():
    csv_file = '../FabCapacityData.csv'

    df = pd.read_csv(csv_file, encoding='utf-8')
    dict_data = df.to_dict()

    return dict_data