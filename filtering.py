import os
import pandas as pd
from random import sample
from datetime import datetime
import pickle

filenames = [x for x in os.listdir("Stocks") if x.endswith('.txt') and os.path.getsize(f"Stocks/{x}") > 0]

def stock_data(filename):
    df = pd.read_csv(f"Stocks/{filename}", index_col='Date', parse_dates=True, usecols=['Date'])
    return df

def proportion_more_x_years(filenames, x):
    date_format = "%Y-%m-%d"
    final_date = datetime.strptime("2017-11-10", date_format)
    files = []
    for filename in filenames:
        df = stock_data(filename)
        initial_date = datetime.strptime(str(df.index[0])[:10], date_format)
        if (final_date-initial_date).days/365 >= x:
            files.append(filename)
    return files

files = proportion_more_x_years(filenames, 6)

# open a file, where you ant to store the data
file = open('list_of_files_6_years', 'wb')
# dump information to that file
pickle.dump(files, file)
# close the file
file.close()
