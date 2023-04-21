from pkls import load_pkl, pickling
import requests
import re
import json
from timer import timer

@timer
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

def find_dict(data: str):
    pattern = r'\{"original":.*?\]\}'
    dict_list = re.findall(pattern, data)
    return dict_list

def str_to_dict(data: str):
    # print(data, type(data))
    dct = json.loads(data)
    return dct

dt = """
{"original": "Английский на уровне чтения документации", "simple_forms": [{"simple_form": "английский на уровне чтения документации", "tag": "knowledge"}]}, {"original": "Навыки монтажа СКС", "simple_forms": [{"simple_form": "навыки монтажа СКС", "tag": "skill"}]}, {"original": "доброжелательность, общительность, мобильность", "simple_forms": [{"simple_form": "доброжелательность", "tag": "unknown"}, {"simple_form": "общительность", "tag": "unknown"}, {"simple_form": "мобильность", "tag": "unknown"}]}, {"original": "web container", "simple_forms": [{"simple_form": "web container", "tag": "knowledge"}]}, {"original": "представление хозяйственной деятельности предприятия,", "simple_forms": [{"simple_form": "представление хозяйственной деятельности предприятия", "tag": "knowledge"}]}, {"original": "Redmine/Jira,", "simple_forms": [{"simple_form": "Redmine", "tag": "knowledge"}, {"simple_form": "Jira", "tag": "knowledge"}]}, {"original": "Ищешь стабильную работу;", "simple_forms": [{"simple_form": "стабильная работа", "tag": "unknown"}]}, {"original": "Опыт создания аналитических отчетов;", "simple_forms": [{"simple_form": "опыт создания аналитических отчетов", "tag": "skill"}]}, {"original": "Владение Kotlin, coroutines", "simple_forms": [{"simple_form": "владение Kotlin", "tag": "skill"}, {"simple_form": "владение coroutines", "tag": "skill"}]}, {"original": "Желательно наличие сертификата 1С8", "simple_forms": [{"simple_form": "сертификат 1С8", "tag": "unknown"}]}, {"original": "Навыки верстки документов;", "simple_forms": [{"simple_form": "навыки верстки документов", "tag": "skill"}]}, {"original": "понимание системы процессов организации;", "simple_forms": [{"simple_form": "понимание системы процессов организации", "tag": "knowledge"}]}, {"original": "Владение русским - приветствуется.", "simple_forms": [{"simple_form": "владение русским", "tag": "knowledge"}]}, {"original": "Знакомство с вычислительной геометрией", "simple_forms": [{"simple_form": "знакомство с вычислительной геометрией", "tag": "knowledge"}]}, {"original": "Навыки программирование АТС", "simple_forms": [{"simple_form": "навыки программирования АТС", "tag": "skill"}]}, {"original": "Знание ПК- высокий уровень", "simple_forms": [{"simple_form": "знание ПК", "tag": "knowledge"}]}, {"original": "Архитектуры SAS Customer Intelligence Studio", "simple_forms": [{"simple_form": "архитектура SAS Customer Intelligence Studio", "tag": "knowledge"}]}, {"original": "наличие коммуникативных навыков;", "simple_forms": [{"simple_form": "коммуникативные навыки", "tag": "skill"}]}, {"original": "имеет аналитический склад ума.", "simple_forms": [{"simple_form": "аналитический склад ума", "tag": "skill"}]}, {"original": "Опыт работы с Mercurial", "simple_forms": [{"simple_form": "опыт работы с Mercurial", "tag": "skill"}]}"""

def save_data(data, filename = 'result.txt'):
    with open(filename, 'a+', encoding='utf-8') as f:
        if isinstance(data, list):
            for i in data:
                json.dump(i, f, ensure_ascii=False)
                f.write('\n')
        else:
            json.dump(data, f, ensure_ascii=False)
            f.write('\n')

def extract_data(filename = 'result.txt'):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        for l in f:
            data.append(json.loads(l))
    return data

@timer
def partial_request(data: list[str], num: int = 20):
    res = []
    x = data
    while x:
        part_x = x[:num]
        splt = '\n'.join(part_x)    
        print(splt)
        try:
            dt = get_data(splt)
            for i in find_dict(*dt):
                d = str_to_dict(i)
                save_data(d)
                res.append(d)
        except Exception as e:
            print(e)
        x = x[num:]
    return res


if __name__ == "__main__":
    data = load_pkl('data.pkl')[20:40]
    # data = extract_data()
    # for i in data:
    #     print(i)
    #     break
    # print(data)
    # save_data(data)

    res = partial_request(data)
    print(res)

    # for i in (extract_data()):
    #     print(i)