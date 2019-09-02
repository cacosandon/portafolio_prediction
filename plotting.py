import pandas as pd
import matplotlib.pyplot as plt
import os
import random
import pickle

def stock_graph(filename,title):
    df = pd.read_csv(f"Stocks/{filename}", index_col='Date', parse_dates=True, usecols=['Date', 'Close'])
    return df

file = open('list_of_files_6_years', 'rb')
# dump information to that file
data = pickle.load(file)
# close the file
file.close()

filenames = data

dates = pd.date_range('2010-12-31','2014-12-31', freq='B')
df_final = pd.DataFrame(index=dates)


graphs = 0
for filename in filenames:
    df_temp = stock_graph(filename, f"Curva {graphs}")
    df_temp = df_temp.rename(columns={'Close': f"Curva {graphs}"})
    df_final = df_final.join(df_temp)
    graphs += 1

df_final.plot(legend=False)
plt.title("Líneas")
plt.show()
