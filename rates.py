import pandas as pd
import matplotlib.pyplot as plt
import os
import random
import pickle

def stock(filename):
    df = pd.read_csv(f"Stocks/{filename}", index_col='Date', parse_dates=True, usecols=['Date', 'Close'])
    return df

def add_rendimientos(df):
    dataset = df
    lista = list(dataset["Close"])

    # Creamos columna rendimiento
    new_column = [lista[0]]
    for i in range(1, len(lista)):
        new_column.append((lista[i]-lista[i-1]) / lista[i-1])

    # La agregamos al dataset y sacamos primera fila dado que no tenemos dato anterior
    dataset["Performance"] = new_column
    dataset = dataset.iloc[1:]

    return dataset

if __name__ == "__main__":
    file = open('list_of_files_4_years', 'rb')
    # dump information to that file
    data = pickle.load(file)
    # close the file
    file.close()

    # Plot Performance

    dates = pd.date_range('2014-08-31','2014-12-31', freq='B')
    df_final = pd.DataFrame(index=dates)

    for file in data[1000:2000]:
        df = add_rendimientos(stock(file))
        df = df.drop(columns=['Close'], axis=1)
        df = df.rename(columns={'Performance': f"Performance {file}"})
        df_final = df_final.join(df)

    df_final.plot(kind="line", legend=False)
    plt.title("Performance v/s Time")
    plt.show()
