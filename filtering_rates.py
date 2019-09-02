from rates import *
from datetime import datetime
import pickle

file = open('list_of_files_4_years', 'rb')
# dump information to that file
data = pickle.load(file)
# close the file
file.close()


dates = pd.date_range('2010-12-31','2014-12-31', freq='B')
df_final = pd.DataFrame(index=dates)
for file in data:
    df = add_rendimientos(stock(file))
    df = df.drop(columns=['Close'], axis=1)
    df = df.rename(columns={'Performance': f"Performance {file}"})
    df_final = df_final.join(df)
