from rates import add_rendimientos, stock
import pandas as pd
import pickle

file = open('list_of_files_4_years', 'rb')
# dump information to that file
data = pickle.load(file)
# close the file
file.close()

"""
PARA HACER UNA DATAFRAME CON LAS PERFORMANCE EN 4 MESES
dates = pd.date_range('2014-08-31','2014-12-31', freq='B')
df_final = pd.DataFrame(index=dates)
for file in data:
    df = add_rendimientos(stock(file))
    df = df.drop(columns=['Close'], axis=1)
    promedio = sum(df['Performance'])/len(df)
    df = df.rename(columns={'Performance': f"Performance {file}"})
    if promedio > 0.001:
        df_final = df_final.join(df)
"""

dates = pd.date_range('2014-08-31','2014-12-31', freq='B')
lista = []
for file in data:
    df = add_rendimientos(stock(file))
    df = df.drop(columns=['Close'], axis=1)
    promedio = sum(df['Performance'])/len(df)
    df = df.rename(columns={'Performance': f"Performance {file}"})
    if promedio > 0.001:
        lista.append(file)


file = open('list_of_files_4_years_01_4months', 'wb')
# dump information to that file
pickle.dump(lista, file)
# close the file
file.close()
