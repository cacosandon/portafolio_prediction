import pandas as pd
import numpy as np
import pickle

file = open('listof_files/list_of_files_4_years', 'rb')
# dump information to that file
data = pickle.load(file)
filenames = data
# close the file
file.close()

dataframe_filtered = None
for file in data:
    # Filtrado

file = open('listof_files/list_of_files_4_years_liqu', 'wb')
# dump information to that file
pickle.dump(dataframe_filtered, file)
# close the file
file.close()
