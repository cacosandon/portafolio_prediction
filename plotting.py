import pandas as pd
import matplotlib.pyplot as plt
import os
import random
import pickle
from filtering_dates import stock_data

# Archivos con info de 4 años, 4 meses con más de 0.1% de rentabilidad promedio
file = open('list_of_files_4_years', 'rb')
# dump information to that file
data = pickle.load(file)
# close the file
file.close()

filenames = data

dates = pd.date_range('2014-08-31','2014-12-31', freq='B')
df_final = pd.DataFrame(index=dates)


graphs = 0
for filename in filenames[:10]:
    df_temp = stock_data(filename, f"Curva {graphs}")
    df_temp = df_temp.rename(columns={'Close': f"Curva {graphs}"})
    df_final = df_final.join(df_temp)
    graphs += 1

df_final.plot(legend=True)
plt.title("Curvas de precios de acciones")
plt.show()
