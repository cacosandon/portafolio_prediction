import pickle


### 4 years ###

# open a file, where you stored the pickled data
file = open('list_of_files_4_years', 'rb')
# dump information to that file
data = pickle.load(file)
# close the file
file.close()

### 6 years ###

# open a file, where you stored the pickled data
file = open('list_of_files_6_years', 'rb')
# dump information to that file
data = pickle.load(file)
# close the file
file.close()

### mayores a 0.001 en rendimiento en 4 meses, 4 años de datos ###

# open a file, where you stored the pickled data
file = open('4_years_0001_performance_4_months', 'rb')
# dump information to that file
data = pickle.load(file)
# close the file
file.close()

### mayores a 0.001 en rendimiento en 4 meses, 4 años de datos, 70% de los rendimientos diarios sobre 0.1% ###

# open a file, where you stored the pickled data
file = open('list_of_files_4_years_01_4months_under0', 'rb')
# dump information to that file
data = pickle.load(file)
# close the file
file.close()

print(len(data))
