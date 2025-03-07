import pandas as pd
import numpy as np
import pickle

file = open('listof_files/list_of_files_4_years', 'rb')
# dump information to that file
data = pickle.load(file)
filenames = data
# close the file
file.close()

def read_file_liq(filename):
    return pd.read_csv(f"Stocks/{filename}", index_col='Date', parse_dates=True, usecols=['Date', 'Close', 'Volume'])


for file in data[:100]:
    df = read_file_liq(file)
    df["VolumeporPrice"] = df["Volume"] * df["Close"]
    porcentaje = sum([1 for x in df["VolumeporPrice"] if x < 500])/len(df["Volume"]) * 100
    print(f"{file}: %{porcentaje}")

file = open('listof_files/list_of_files_4_years_liqu', 'wb')
# dump information to that file
pickle.dump(dataframe_filtered, file)
# close the file
file.close()
