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
{"original": "приверженность MVC.", "simple_form": ["приверженность MVC"], "tag": "knowledge"}, {"original": "Опыт работы с ETL процессами", "simple_form": ["опыт работы с ETL процессами"], "tag": "skill"}, {"original": "Имеют подвижный ум.", "simple_form": ["подвижный ум"], "tag": "unknown"}, {"original": "Опыт прототипирования пользовательских интерфейсов", "simple_form": ["опыт прототипирования пользовательских интерфейсов"], "tag": "skill"}, {"original": "навыки работы с RabbitMQ", "simple_form": ["навыки работы с RabbitMQ"], "tag": "skill"}, {"original": "понимание RxJava", "simple_form": ["понимание RxJava"], "tag": "knowledge"}, {"original": "процессы управления ИБ;", "simple_form": ["процессы управления ИБ"], "tag": "skill"}, {"original": "Навык организации кода;", "simple_form": ["навык организации кода"], "tag": "skill"}, {"original": "знание современных интерфейсов;", "simple_form": ["знание современных интерфейсов"], "tag": "knowledge"}, {"original": "знание польского языка приветствуется.", "simple_form": ["знание польского языка"], "tag": "knowledge"}, {"original": "Системы расчета статистики торговых операций", "simple_form": ["системы расчета статистики торговых операций"], "tag": "knowledge"}, {"original": "Знание дизайн-паттернов", "simple_form": ["знание дизайн-паттернов"], "tag": "knowledge"}, {"original": "Знание QA-процессов;", "simple_form": ["знание QA-процессов"], "tag": "knowledge"}, {"original": "Умением оптимизировать код.", "simple_form": ["умение оптимизировать код"], "tag": "skill"}, {"original": "Крайне важна уверенная грамотная речь", "simple_form": ["грамотная речь"], "tag": "unknown"}, {"original": "Высшее образование - техническое,", "simple_form": ["высшее техническое образование"], "tag": "knowledge"}, {"original": "Уверенное владение Google документами", "simple_form": ["уверенное владение Google документами"], "tag": "skill"}, {"original": "Знание железа. Сетевые устройства", "simple_form": ["знание железа", "знание сетевых устройств"], "tag": "knowledge"}, {"original": "опыт в сфере телекоммуникаций", "simple_form": ["опыт в сфере телекоммуникаций"], "tag": "skill"}, {"original": "CakePHP framework", "simple_form": ["знание CakePHP framework"], "tag": "knowledge"}, {"original": "опыт разработки GUI", "simple_form": ["опыт разработки GUI"], "tag": "skill"}, {"original": "MS Analysis", "simple_form": ["знание MS Analysis"], "tag": "knowledge"}, {"original": "Опыт использования NodeJS", "simple_form": ["опыт использования NodeJS"], "tag": "skill"}, {"original": "навыки администрирования Linux приветствуются;", "simple_form": ["навыки администрирования Linux"], "tag": "skill"}, {"original": "RS-485 (UART);", "simple_form": ["знание RS-485 (UART)"], "tag": "knowledge"}, {"original": "XML и Json данными;", "simple_form": ["работа с XML данными", "работа с Json данными"], "tag": "skill"}, {"original": "Навык ведения телефонных переговоров", "simple_form": ["навык ведения телефонных переговоров"], "tag": "skill"}, {"original": "Продвинутое владение MS Excel", "simple_form": ["продвинутое владение MS Excel"], "tag": "skill"}, {"original": "знание JQuery будет плюсом", "simple_form": ["знание JQuery"], "tag": "knowledge"}
"""



if __name__ == "__main__":
    data = load_pkl('data.pkl')
    data = load_pkl('testdata.pkl')
    smpl = data
    # print(type(smpl))
    print((smpl))
    # splt = '\n'.join(smpl)
    # print(splt)
    # # print(get_data(splt))
    # d_list = []
    # for i in reformat_data(dt):
    #     try:
    #         d = str_to_dict(i)
    #         pickling(d, 'testdata.pkl')
    #         # d_list.append(d)
    #         # print(type(i), type(d), d)
    #     except Exception as e:
    #         pass
    # pickling(d_list, 'testdata.pkl')