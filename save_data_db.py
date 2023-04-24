import pickle
import pandas as pd
from src.database import DBHelper


def read_pickle_transfer_pandas(file: str):
    df = pd.read_pickle(file)
    return df.text

list_unique_value = read_pickle_transfer_pandas('unique_data.pkl')

print('Данные загружены')

data_save = DBHelper('mydatabase.db')

list_save_data = []
data_save.save_data_in_db(list_unique_value, list_save_data)

