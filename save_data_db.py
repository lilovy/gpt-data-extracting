import pickle
import pandas as pd
from src.database.DBHelper import DBHelper


def read_pickle_transfer_pandas(file: str):
    df = pd.read_pickle(file)
    return df.text

list_unique_value = read_pickle_transfer_pandas('.localdata/unique_data.pkl')

print('Данные загружены')

data_save = DBHelper('markupdata.db')

data_save.insert_raw_data(list_unique_value)

