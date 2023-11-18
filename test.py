import json
import snowfall_csv
import weather_forecast

snowfall = snowfall_csv.snowfall_dict
data = weather_forecast.data
data_json = dict(**data, **snowfall)

print(data_json)