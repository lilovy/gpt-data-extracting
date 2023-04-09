from pkls import load_pkl, pickling
import requests
import re
import json


def get_data(data):
    resp = requests.post(
        "http://127.0.0.1:7860/run/predict", 
        json={
            "data": [
                data,
                ]
            },
        ).json()
    data = resp["data"]
    return data

def reformat_data(data: str):
    pattern = r'\{"original":.*?\}'
    dict_list = re.findall(pattern, data)
    return dict_list

def str_to_dict(data: str):
    # print(data, type(data))
    dct = json.loads(data)
    return dct

dt = """
['{"original": "Опыт программирования с использованием ООП"
"simple_form": ["опыт использования ООП при программировани], "tag": "skill"}\n\n{"original": "Знание PHP/Yii2.", "sime_form": ["знание PHP", "знание Yii2"], "tag": "knowledge"}\n{"original": "Понимание работы Terraform.", "simple_form"
["понимание работы Terraform"], "tag": "knowledge"}\n\n{"orinal": "отличное знание Transact-SQL", "simple_form": ["отлное знание Transact-SQL"], "tag": "knowledge"}\n\n{"origina: "Знания бухгалтерских программ желательно;", "simple_form ["знание бухгалтерских программ"], "tag": "knowledge"}\n\noriginal": "Желательно знание C#,Visual ForPro.", "simple_fm": ["знание C#", "знание Visual ForPro"], "tag": "knowledg}\n\n{"original": "опыт обслуживания и администрирования", imple_form": ["опыт обслуживания", "опыт администрирования" "tag": "skill"}\n\n{"original": "понимание монетизационныхсобенностей F2P;", "simple_form": ["понимание монетизационн особенностей F2P"], "tag": "knowledge"}\n\n{"original": "Ux-системами желательны", "simple_form": ["желательно знаниеnix-систем"], "tag": "knowledge"}\n\n{"original": "опыт посоения хранилищ данных приветствуется", "simple_form": ["опы
построения хранилищ данных"], "tag": "skill"}']
"""



if __name__ == "__main__":
    data = load_pkl('data.pkl')
    smpl = data[:3]
    splt = '\n'.join(smpl)
    # print(splt)
    # print(get_data(splt))
    for i in reformat_data(dt):
        try:
            d = str_to_dict(i)
            print(type(i), type(d), d)
        except Exception as e:
            pass