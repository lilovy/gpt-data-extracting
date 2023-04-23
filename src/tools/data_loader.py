import pickle
from src.tools import timer
import pandas as pd
from pandas import DataFrame

@timer
def load_pkl(file):
    with open(file, 'rb') as f:
        data = pickle.load(f)
    return data

@timer
def load_pandas_pkl(file) -> DataFrame:
    df = pd.read_pickle(file)
    return df

def pickling(data, file, mode = 'ab+'):
    with open(file, mode) as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    data = load_pkl('.localdata/data_500k.pkl')
    # print(data[220100:220310])
    print(len(data))
    # print(data.head(50))