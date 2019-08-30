import json
from pandas import pandas as pd


def save_excel(data):
    # json 파일 으로 저장하기
    file = open("./recipe.json", "w+")
    file.write(json.dumps(data))  # json.dumps() 로 result 는 list 에서 string 으로 변경된다
    # excel 로 저장하기
    json_setting = pd.read_json('./recipe.json')
    xlsx_setting = pd.ExcelWriter('recipe.xlsx')
    json_setting.to_excel(xlsx_setting, 'sheet1')
    xlsx_setting.save()
