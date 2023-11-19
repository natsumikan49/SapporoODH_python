from flask import Flask
import snowfall_csv
import weather_forecast
import yosoku_shiroishi
from yosoku import yosoku_tyuou, kita, teine, kiyota, toyohira, minami, higashi, atsubetsu
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
    if yosoku2 < 0:
        yosoku2 = 0
    snowfall2["24時間降雪量 現在値(cm)"] = yosoku2
    data_json3 = dict(**data2, **snowfall2)
    data_json["北"] = data_json3
    # 東区
    snowfall3 = snowfall_csv.snowfall_dict
    data3 = weather_forecast.data
    snowfall2["地点"] = "東区"
    yosoku3 = float(weather_forecast.jma_temp) * float(higashi.coef_temp) + float(
        weather_forecast.jma_rain) * float(higashi.coef_rain) + float(higashi.intercept)
    if yosoku3 < 0:
        yosoku3 = 0
    snowfall3["24時間降雪量 現在値(cm)"] = yosoku3
    data_json4 = dict(**data3, **snowfall3)
    data_json["東"] = data_json4
    # 南区
    snowfall4 = snowfall_csv.snowfall_dict
    data4 = weather_forecast.data
    snowfall4["地点"] = "南区"
    yosoku4 = float(weather_forecast.jma_temp) * float(minami.coef_temp) + float(
        weather_forecast.jma_rain) * float(minami.coef_rain) + float(minami.intercept)
    if yosoku4 < 0:
        yosoku4 = 0
    snowfall4["24時間降雪量 現在値(cm)"] = yosoku4
    data_json5 = dict(**data4, **snowfall4)
    data_json["南"] = data_json5
    # 清田区
    snowfall5 = snowfall_csv.snowfall_dict
    data5 = weather_forecast.data
    snowfall5["地点"] = "清田区"
    yosoku5 = float(weather_forecast.jma_temp) * float(kiyota.coef_temp) + float(
        weather_forecast.jma_rain) * float(kiyota.coef_rain) + float(kiyota.intercept)
    if yosoku5 < 0:
        yosoku5 = 0
    snowfall5["24時間降雪量 現在値(cm)"] = yosoku5
    data_json6 = dict(**data5, **snowfall5)
    data_json["清田"] = data_json6
    # 手稲区
    snowfall6 = snowfall_csv.snowfall_dict
    data6 = weather_forecast.data
    snowfall6["地点"] = "手稲区"
    yosoku6 = float(weather_forecast.jma_temp) * float(teine.coef_temp) + float(
        weather_forecast.jma_rain) * float(teine.coef_rain) + float(teine.intercept)
    if yosoku6 < 0:
        yosoku6 = 0
    snowfall6["24時間降雪量 現在値(cm)"] = yosoku6
    data_json7 = dict(**data6, **snowfall6)
    data_json["手稲"] = data_json7
    # 豊平区
    snowfall7 = snowfall_csv.snowfall_dict
    data7 = weather_forecast.data
    snowfall7["地点"] = "豊平区"
    yosoku7 = float(weather_forecast.jma_temp) * float(toyohira.coef_temp) + float(
        weather_forecast.jma_rain) * float(toyohira.coef_rain) + float(toyohira.intercept)
    if yosoku7 < 0:
        yosoku7 = 0
    snowfall7["24時間降雪量 現在値(cm)"] = yosoku7
    data_json8 = dict(**data7, **snowfall7)
    data_json["豊平"] = data_json8

    print(data_json)
    # 厚別区
    snowfall8 = snowfall_csv.snowfall_dict
    data8 = weather_forecast.data
    snowfall8["地点"] = "厚別区"
    yosoku8 = float(weather_forecast.jma_temp) * float(atsubetsu.coef_temp) + float(
        weather_forecast.jma_rain) * float(atsubetsu.coef_rain) + float(atsubetsu.intercept)
    if yosoku8 < 0:
        yosoku8 = 0
    snowfall8["24時間降雪量 現在値(cm)"] = yosoku8
    data_json9 = dict(**data8, **snowfall8)
    data_json["厚別"] = data_json9

    print(data_json)
    return


showFall_shiro()


