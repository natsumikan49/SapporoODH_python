from flask import Flask
import snowfall_csv
import weather_forecast
app = Flask(__name__)

@app.route("/")
def showFall():
    snowfall = snowfall_csv.snowfall_dict
    data = weather_forecast.data
    data_json = dict(**data, **snowfall)
    return data_json

if __name__ == "__main__":
    app.run()

