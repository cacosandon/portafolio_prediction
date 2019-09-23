import pandas as pd
import matplotlib.pyplot as plt
import os
import random
import pickle
from filtering_dates import stock_data

file = open('listof_files/list_of_files_4_years_coefconstantnegativain4months', 'rb')
# dump information to that file
data = pickle.load(file)
# close the file
file.close()

filenames = data

dates = pd.date_range('2014-08-31','2014-12-31', freq='B')
df_final = pd.DataFrame(index=dates)


graphs = 0
for filename in filenames[545:552]:
    df_temp = stock_data(filename)
    df_temp = df_temp.rename(columns={'Close': f"Curva {graphs}"})
    df_final = df_final.join(df_temp)
    graphs += 1

df_final.plot(legend=False)
plt.title("Curvas de precios de acciones")
plt.show()
