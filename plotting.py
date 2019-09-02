import pandas as pd
import matplotlib.pyplot as plt
import os
import random

def stock_graph(filename,title):
    df = pd.read_csv(f"Stocks/{filename}", index_col='Date', parse_dates=True, usecols=['Date', 'Close'])
    return df

filenames = [x for x in os.listdir("Stocks") if x.endswith('.txt')]
filenames = random.sample(filenames,50)


dates = pd.date_range('2000-01-01','2014-12-31', freq='B')
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
