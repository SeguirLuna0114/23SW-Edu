import uvicorn
from fastapi import FastAPI  # FastAPI와 MongoDB를 사용하여 API를 구현
from pymongo import mongo_client
from pymongo import InsertOne
import pydantic
import requests
from bson.objectid import ObjectId
import os.path
import os
import requests
import json
import pandas as pd
from PIL import Image
import numpy as np
from datetime import datetime, timedelta
from typing import Union
from bson.objectid import ObjectId
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import asyncio
from aioconsole import ainput

def merge_images(image_path_list):
    images = [Image.open(image_path) for image_path in image_path_list]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_image = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for image in images:
        new_image.paste(image, (x_offset, 0))
        x_offset += image.width

    return new_image

#CN DATA
file1 = '/allnew/python/forproject/fastapi_mongodb/china_fastapi/api bo {year}{quarter}.PNG'
file2 = './allnew/python/forproject/fastapi_mongodb/code_img/getCNData_app.py/5.async def get_data(year, quater).png'

image_path_list = [file1, file2]
merged_image = merge_images(image_path_list)
merged_image.show()

savedFile = './code_img/async_def_get_data(year, quarter).png'
merged_image.save(savedFile, 'PNG')
print(savedFile, 'saved~!!')