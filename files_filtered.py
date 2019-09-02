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
