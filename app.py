from flask import Flask
import snowfall_csv
import weather_forecast
import yosoku_shiroishi
from yosoku import yosoku_tyuou, kita, teine, kiyota, toyohira, minami
app = Flask(__name__)


def showFall_shiro():
    data_json = {}
    # 白石区
    snowfall = snowfall_csv.snowfall_dict
    data = weather_forecast.data
    snowfall['地点'] = "白石区"
    yosoku = float(weather_forecast.jma_temp) * float(yosoku_shiroishi.coef_temp) + float(weather_forecast.jma_rain) * float(yosoku_shiroishi.coef_rain) + float(yosoku_shiroishi.intercept)
    if yosoku < 0:
        yosoku = 0
    snowfall["24時間降雪量 現在値(cm)"] = yosoku
    data_json1 = dict(**data, **snowfall)
    # 中央区
    snowfall1 = snowfall_csv.snowfall_dict
    data1 = weather_forecast.data
    snowfall1["地点"] = "中央区"
    yosoku1 = float(weather_forecast.jma_temp) * float(yosoku_tyuou.coef_temp) + float(weather_forecast.jma_rain) * float(yosoku_tyuou.coef_rain) + float(yosoku_tyuou.intercept)
    if yosoku1 < 0:
        yosoku1 = 0
    snowfall1["24時間降雪量 現在値(cm)"] = yosoku1
    data_json2 = dict(**data1, **snowfall1)
    data_json["白石"] = data_json1
    data_json["中央"] = data_json2
    # 北区
    snowfall2 = snowfall_csv.snowfall_dict
    data2 = weather_forecast.data
    snowfall2["地点"] = "北区"
    yosoku2 = float(weather_forecast.jma_temp) * float(kita.coef_temp) + float(
        weather_forecast.jma_rain) * float(kita.coef_rain) + float(kita.intercept)
    if yosoku1 < 0:
        yosoku1 = 0
    snowfall1["24時間降雪量 現在値(cm)"] = yosoku1
    data_json2 = dict(**data1, **snowfall1)
    data_json["白石"] = data_json1
    data_json["中央"] = data_json2

    print(data_json)
    return


showFall_shiro()


