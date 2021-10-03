import pandas as pd
import csv
import numpy as np
file_ = 'fox_unsort.csv'
_ = pd.read_csv(file_)
new_ = _.sort_values(by=['custom_uuid', 'movie_id'])
data = new_.to_numpy()
len_ = data.shape[0]
repeat_list = []
#################################清重複

for i in range(len_):
    if i == (len_-2):
        if data[i, 1] == data[i+1, 1]:
            repeat_list.append(i)
        break
    if  data[i, 1] == data[i+1, 1]:
        repeat_list.append(i)


print(new_.shape)
new_ = new_.drop(repeat_list)
print(new_.shape)
new_ = new_.sort_values(by=['custom_uuid', 'movie_id'])
new_.to_csv('fox_unrepeat.csv', index=False)