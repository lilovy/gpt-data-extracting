from src.tools import FindDict
from src.database import DBHelper

data = FindDict('{"original": "файер-вол, домен", "simple_forms": [{"simple_form": "файер-вол", "tag": "unknown"}, {"simple_form": "домен", "tag": "unknown"}]}, {"original": "Проектные и мультимодальные перевозки;", "simple_forms": [{"simple_form": "проектные перевозки", "tag": "skill"}, {"simple_form": "мультимодальные перевозки", "tag": "skill"}]}')

data = list(zip([1, 2], data))

# for tuple_ in data:
#     dict_ = tuple_[1]
#     values = dict_.get('simple_forms')
#     for value in values:
#         print(tuple_[0], value['simple_form'], value['tag'])

list_save_data = []
save_data = DBHelper('mydatabase.db')
save_data.insert_result_data(data, list_save_data)






