import pickle
from timer import timer
import pandas as pd
from pandas import DataFrame

@timer
def load_pkl(file):
    with open(file, 'rb') as f:
        data = pickle.load(f)
    return data

@timer
def load_pkl_pandas(file) -> DataFrame:
    df = pd.read_pickle(file)
    return df

# data = load_pkl_pandas('src/.localdata/data.pkl')

if __name__ == "__main__":
    # data = load_pkl('src/.localdata/data.pkl')
    # print(data[220100:220310])
    print(len(data))
    print(data.head(50))

    # for i in data[400000:405000]:
    #     print(i)
# lens = [(len(x), x) for x in data]
# print(max(lens))
# for i in range(40):
#     lens.remove(max(lens))
#     print(max(lens))

def pickling(data, file, mode = 'ab+'):
    with open(file, mode) as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

dt = [
    {
"original": "файер-вол, домен",
"simple_form": [
"файер-вол",
"домен"
],
"tag": "unknown"
},
{
"original": "Проектные и мультимодальные перевозки;",
"simple_form": [
"проектные перевозки",
"мультимодальные перевозки"
],
"tag": "skill"
},
{
"original": "Опыт проектирования инженерных систем.",
"simple_form": [
"проектирование инженерных систем"
],
"tag": "knowledge"
},
{
"original": "опыт работы в сетевом программировании",
"simple_form": [
"сетевое программирование"
],
"tag": "skill"
},
{
"original": "высшее техническое/ИТ образование",
"simple_form": [
"высшее техническое образование",
"высшее ИТ образование"
],
"tag": "knowledge"
},
{
"original": "Google Chrome",
"simple_form": [
"Google Chrome"
],
"tag": "unknown"
}
]

# for i in dt:
#     print(i)