import pandas as pd
import csv
import numpy as np
file_ = 'amazon_Book_prune.csv'
_ = pd.read_csv(file_)

new_ = _.sort_values('customer_id')
data = new_.to_numpy()
len_ = data.shape[0]
repeat_list = []

###############################清小於50

check = int(1)

__ = [] 
new_len = (data.shape[0]-2)
for i in range(new_len):
    if data[i, 0] == data[i+1, 0]:
        check += 1
    else:
        if check < 30:
            for a in reversed(range(check)):
                __.append(i-a)              
        check = 1
print(new_.shape)
print(f"clear_size:{len(__)}")
new_ = new_.drop(__)
data = np.delete(data, __, axis = 0)

print(new_.shape, data.shape)

##################################換ID
check = int(0)
len_ = data.shape[0]
for i in range(len_):
    if i == (len_-2):
        if data[i, 0] == data[i+1, 0]:
            data[i, 0] = check
            data[i+1, 0] = check
        else:
            data[i, 0] = check
            data[i+1, 0] = (check+1)
        break
    if data[i, 0] == data[i+1, 0]:
        data[i, 0] = check
    else:
        data[i, 0] = check
        check += 1

for i in range(data.shape[0]):
    new_.iat[i, 0] = data[i, 0]

new_.to_csv('amazon_idchanged.csv', index=False)

