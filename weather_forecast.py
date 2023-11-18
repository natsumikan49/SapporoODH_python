# -*- coding:utf-8 -*-
import requests
import json

# 気象庁データの取得
jma_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/016000.json"
jma_json = requests.get(jma_url).json()

# 取得したいデータを選ぶ
jma_date = jma_json[0]["timeSeries"][0]["timeDefines"][1]
jma_weather = jma_json[0]["timeSeries"][0]["areas"][0]["weathers"][1]

# 全角スペースの削除
jma_weather = jma_weather.replace('　', '')

print(jma_date)
print(jma_weather)
