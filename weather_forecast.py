# -*- coding:utf-8 -*-
import requests
import json

# 気象庁データの取得
jma_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/016000.json"
jma_json = requests.get(jma_url).json()

# 取得したいデータを選ぶ
jma_date = jma_json[0]["timeSeries"][0]["timeDefines"][1]
jma_weather = jma_json[0]["timeSeries"][0]["areas"][0]["weathers"][1]
jma_temp = jma_json[0]["timeSeries"][2]["areas"][0]["temps"][2]
jma_rainmin = jma_json[1]["precipAverage"]["areas"][0]["min"]
jma_rainmax = jma_json[1]["precipAverage"]["areas"][0]["max"]

jma_rain = (float(jma_rainmax) + float(jma_rainmin) )/ 2.0
print(jma_rain)
# 全角スペースの削除
jma_weather = jma_weather.replace('　', '')

data = {"time":jma_date, "weather":jma_weather}
print(jma_date)
print(jma_weather)
print(data)
