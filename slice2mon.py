import csv
import pandas as pd

data = pd.read_csv('fox_usermovieID.csv')
data = data.sort_values('custom_uuid')
data = data.reset_index(drop=True)
print(data.index)
print(data)

#data = data.reset_index(drop=True)
f = ["2018-05-11", "2018-05-21", "2018-06-01", "2018-06-11", "2018-06-21", "2018-07-01", "2018-07-11", "2018-07-20", "2018-07-28"]

#data.loc[data["gen_date"] > "2018-05-11", 'movie_rate'] = 0

'''
f.append(data["gen_date"] < "2018-05-21")
f.append(data["gen_date"] < "2018-06-01")
f.append(data["gen_date"] < "2018-06-11")
f.append(data["gen_date"] < "2018-06-21")
f.append(data["gen_date"] < "2018-07-01")
f.append(data["gen_date"] < "2018-07-11")
f.append(data["gen_date"] < "2018-07-20")
f.append(data["gen_date"] < "2018-07-28")
'''
i = int(8)
for date in reversed(f):
    data.loc[data["gen_date"] > date, 'movie_rate'] = 0
    data.to_csv(f'mon{i}.csv', index=False)
    i = i-1
