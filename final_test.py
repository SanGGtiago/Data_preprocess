import pandas as pd

def read_data(filename):
    df = pd.read_csv(filename,
                   sep=',', names=['custom_uuid','movie_id','movie_rate','gen_date'], engine='python', encoding='latin-1')
    matrix = df.pivot_table(index='custom_uuid', columns='movie_id', values='movie_rate')
    matrix.fillna(0, inplace=True)
    users = matrix.index.tolist()
    items = matrix.columns.tolist()
    matrix_list = matrix.values
    return matrix_list

filepath = "slicedata/mon14.csv"
data = read_data(filepath)
print(data.shape)
