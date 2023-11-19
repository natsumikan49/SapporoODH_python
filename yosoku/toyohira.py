# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

df_2019 = pd.read_csv(r".\data\2019toyohira.csv", encoding="utf8")
df_2018 = pd.read_csv(r".\data\2018toyohira.csv", encoding="utf8")
df_2017 = pd.read_csv(r".\data\2017toyohira.csv", encoding="utf8")

df_2019_co = df_2019[["気温(℃)", "風速(m/s)","風向(度:0～359)", "降水量(mm)", "積雪深(cm)"]]
df_2019_co = df_2019_co.replace('×', np.NaN).dropna()
df_2018_co = df_2018[["気温(℃)", "風速(m/s)","風向(度:0～359)", "降水量(mm)", "積雪深(cm)"]]
df_2018_co = df_2018_co.replace('×', np.NaN).dropna()
df_2017_co = df_2017[["気温(℃)", "風速(m/s)","風向(度:0～359)", "降水量(mm)", "積雪深(cm)"]]
df_2017_co = df_2017_co.replace('×', np.NaN).dropna()

print(df_2019_co.corr())
print(df_2018_co.corr())
print(df_2017_co.corr())

df = pd.concat([df_2019_co, df_2018_co, df_2017_co])

print(df)

# 目的変数を積雪、説明変数をそれ以外
y = df["積雪深(cm)"]
x = df[["気温(℃)", "降水量(mm)"]]

# データを訓練データとテストデータに分ける
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)

# x_train を標準化し x_train に格納
ss = preprocessing.StandardScaler()
ss.fit(x_train)
x_train = ss.transform(x_train)

# x_test を標準化し x_test に格納
x_test = ss.transform(x_test)

# モデルの初期化と学習
model = LinearRegression()
model.fit(x_train, y_train)

print('訓練データに対する決定係数：', model.score(x_train, y_train))
print('テストデータに対する決定係数：', model.score(x_test, y_test))

# 偏回帰係数
coef = pd.Series(model.coef_, index=x.columns)
coef_temp = coef["気温(℃)"]
coef_rain = coef["降水量(mm)"]

# 切片
intercept = model.intercept_