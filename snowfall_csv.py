import pandas as pd

url = "https://www.data.jma.go.jp/stats/data/mdrr/snc_rct/alltable/sndall00_rct.csv"

snowfall_df = pd.read_csv(url, encoding="shift-jis")
sapporo_snowfall_df = snowfall_df.query('観測所番号 == 14163').dropna(axis=1)
sapporo_snowfall_df['取得時刻'] = sapporo_snowfall_df['現在時刻(年)'].astype(str) + '/' + sapporo_snowfall_df['現在時刻(月)'].astype(str) + '/' + sapporo_snowfall_df['現在時刻(日)'].astype(str) + '/' + sapporo_snowfall_df['現在時刻(時)'].astype(str) + ':' + sapporo_snowfall_df['現在時刻(分)'].astype(str) + '0'
snowfall = sapporo_snowfall_df[['都道府県', '地点', '取得時刻', '24時間降雪量 現在値(cm)']]
print(snowfall)

data = snowfall.to_string()
print(data)