import csv
import pandas as pd

data = pd.read_csv('amazon_ori.csv', names=['custom_id','movie_id','movie_rate','review_date'])
data = data.sort_values('review_date')
data = data.reset_index(drop=True)
print(data.index)
print(data)
dataset_name = 'amazon'
#data = data.reset_index(drop=True)
#data.loc[data["gen_date"] > "2018-05-11", 'movie_rate'] = 0

###第一種分類法
def time_slice(num = int):
    f = ["2000-01-01", "2001-01-01", "2002-01-01", "2003-01-01", "2004-01-01", "2005-01-01", "2006-01-01", "2007-01-01", "2000-01-01"]
    data.to_csv(f'slicedata/mon{num}.csv', index=False)
    for date in reversed(f):
        data.loc[data["gen_date"] > date, 'movie_rate'] = 0
        data.to_csv(f'slicedata/mon{num}.csv', index=False)
        i = i-1
    
###第二種分類法
def num_slice(num = int):
    count = int(data.shape[0]/num)
    j = num
    data.to_csv(f'slicedata/{dataset_name}_mon{num}.csv', header=False, index=False)
    for i in range(num-1, 0, -1):
        j = j-1
        data.loc[count*i:, 'movie_rate'] = 0
        data.to_csv(f'slicedata/{dataset_name}_mon{j}.csv', header=False, index=False)
        print(i, count*i)

num_slice(15)