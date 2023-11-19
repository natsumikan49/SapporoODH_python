from flask import Flask
import snowfall_csv
import weather_forecast
import yosoku_shiroishi
app = Flask(__name__)


@app.route("/")
def showFall():
    snowfall = snowfall_csv.snowfall_dict
    data = weather_forecast.data
    data["地点"] = "白石区"
    yosoku = weather_forecast.jma_temp * yosoku_shiroishi.coef_temp + weather_forecast.jma_rain * yosoku_shiroishi.coef_rain + yosoku_shiroishi.intercept
    data["24時間降雪量 現在値(cm)"] = yosoku
    if yosoku < 0:
        yosoku = 0
    data_json = dict(**data, **snowfall)
    return data_json

if __name__ == "__main__":
    app.run()
    
    

