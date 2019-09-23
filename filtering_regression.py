from filtering_dates import stock_data
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

file = open('listof_files/list_of_files_4_years_01_4months', 'rb')
# dump information to that file
data = pickle.load(file)
filenames = data
# close the file
file.close()

dates_real_total = pd.date_range('2013-09-30','2014-02-28', freq='B')
dates_train = pd.date_range('2013-09-30','2014-01-31', freq='B')
df_final = pd.DataFrame(index=dates_real_total)

sample_n = [43, 46]

lista_accepted = []
lista_declined = []
#for file in data[sample_n[0]:sample_n[1]]:
for file in data:

    # Train de 2010 a 2014
    df_dates_train = pd.DataFrame(index=dates_train)
    df = stock_data(file)

    df_regression = df_dates_train.join(df).dropna()

    regressor = LinearRegression()
    y = df_regression['Close']
    X = np.array([i for i in range(len(y))]).reshape(-1,1)
    regressor.fit(X, y)
    if regressor.coef_ > 0.001:
        lista_accepted.append(file)
    else:
        lista_declined.append(file)

file = open('listof_files/list_of_files_4_years_coefpositivein4months', 'wb')
# dump information to that file
pickle.dump(lista_accepted, file)
# close the file
file.close()

file = open('listof_files/list_of_files_4_years_coefconstantnegativain4months', 'wb')
# dump information to that file
pickle.dump(lista_declined, file)
# close the file
file.close()
