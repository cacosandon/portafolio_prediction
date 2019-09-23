import pickle


# open a file, where you stored the pickled data
file = open('listof_files/list_of_files_4_years_coefpositivein4months', 'rb')
# dump information to that file
data = pickle.load(file)
# close the file
file.close()

print(len(data))
