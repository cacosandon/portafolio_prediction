from filtering_dates import stock_data
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import random

file = open('listof_files/list_of_files_4_years', 'rb')
# dump information to that file
data = pickle.load(file)
filenames = data
# close the file
file.close()

dates_real_first = pd.date_range('2013-09-30','2014-01-31', freq='B')
dates_real_scnd = pd.date_range('2014-01-31','2014-02-28', freq='B')
dates_real_total = pd.date_range('2013-09-30','2014-02-28', freq='B')
dates_train = pd.date_range('2013-09-30','2014-01-31', freq='B')
df_final = pd.DataFrame(index=dates_real_total)

sample_n = [50, 53]

for file in data[sample_n[0]:sample_n[1]]:

    # Obtenemos curva real de 2010 a 2017, y el train de 2010 a 2014
    df_dates_real_first = pd.DataFrame(index=dates_real_first)
    df_dates_real_scnd = pd.DataFrame(index=dates_real_scnd)
    df_dates_real_total = pd.DataFrame(index=dates_real_total)
    df_dates_train = pd.DataFrame(index=dates_train)
    df = stock_data(file)

    df_temp = df_dates_real_first.join(df)
    df_real = df_dates_real_scnd.join(df)
    df_regression = df_dates_train.join(df).dropna()
    df_regression_large = df_dates_real_total.join(df).dropna()

    regressor = LinearRegression()
    y = df_regression['Close']
    X = np.array([i for i in range(len(y))]).reshape(-1,1)
    regressor.fit(X, y)
    print(regressor.coef_)

    # Obtenemos recta de 2010 a 2017
    X_real = np.array([i for i in range(len(df_regression_large))]).reshape(-1,1)
    Y_predicted = regressor.predict(X_real)
    df_regression_large['Close'] = Y_predicted

    df_temp = df_temp.rename(columns={'Close': f"Curva 1 {file.strip('.txt')}"})
    df_real = df_real.rename(columns={'Close': f"Curva 2 {file.strip('.txt')}"})
    df_regression = df_regression_large.rename(columns={'Close': f"Regresion {file.strip('.txt')}"})

    df_final = df_final.join(df_temp)
    df_final = df_final.join(df_real)
    df_final = df_final.join(df_regression)

color_dict = {}
for name in data[sample_n[0]:sample_n[1]]:
    color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
    color_dict[f"Curva 1 {name.strip('.txt')}"] = color
    color_dict[f"Regresion {name.strip('.txt')}"] = color

df_final.plot(legend=False, color=[color_dict.get(x) for x in df_final.columns])
plt.title("Curvas de precios de acciones con LinearRegression")
plt.show()
