import pandas as pd
import csv
import numpy as np
file_ = 'amazon_idchanged.csv'
_ = pd.read_csv(file_)

new_ = _.sort_values('product_id')
data = new_.to_numpy()
ID =int(0)
len_ = data.shape[0]
for i in range(len_):
    if i == (len_-2):
        if data[i, 1] == data[i+1, 1]:
            data[i, 1] = ID
            data[i+1, 1] = ID
        else:
            data[i, 1] = ID
            data[i+1, 1] = (ID+1)
        break
    if data[i, 1] == data[i+1, 1]:
        data[i, 1] = ID
    else:
        data[i, 1] = ID
        ID += 1

for i in range(data.shape[0]):
    new_.iat[i, 1] = data[i, 1]

new_.to_csv('amazon_ori.csv', index=False, header=False)
