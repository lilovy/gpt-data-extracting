from src.V1 import MarkupGPT
import tiktoken
import pickle
from config import access_token2 as access_token


def load_pkl(file):
    with open(file, 'rb') as f:
        data = pickle.load(f)
    return data

data = load_pkl('data.pkl')[13113:13123]

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


# bot = MarkupGPT(access_token)


prompt = """
Изучите список требований к соискателям.
Для каждого требования определите его тип (skill - навык, knowledge - знание, unknown - неизвестно).
knowledge - это понимание того, как что-то работает или что-то означает.
skill - это умение применять знания в практических ситуациях или выполнять определенные задачи с опытом и мастерством.
Сформулируйте простую форму каждого требования, убрав из оригинала лишнее и избавившись от сложных конструкций. Если требование содержит несколько навыков/знаний, разделите их на отдельные строки.
Укажите тип требования (skill/knowledge/unknown) и полученную простую форму в формате:
{"original": "Оригинальный текст требования", "simple_forms": [{"simple_form": "Простая форма требования", "tag": "Тип требования"}]}.
Повторите шаги 3-4 для всех требований в списке.
Сохраните все данные в формате JSON.

Я: 
Знание adaptive, responsive верстки

ChatGPT: 
{"original": "Знание adaptive, responsive верстки", "simple_forms": [{"simple_form": "знание adaptive верстки", "tag": "knowledge"}, {"simple_form": "знание responsive верстки", "tag": "knowledge"}]}

Я: 
файер-вол, домен
Проектные и мультимодальные перевозки;

ChatGPT:
{"original": "файер-вол, домен", "simple_forms": [{"simple_form": "файер-вол", "tag": "unknown"}, {"simple_form": "домен", "tag": "unknown"}]}, {"original": "Проектные и мультимодальные перевозки;", "simple_forms": [{"simple_form": "проектные перевозки", "tag": "skill"}, {"simple_form": "мультимодальные перевозки", "tag": "skill"}]}
"""

# bot.set_default_prompt(prompt)

asks = [
    'Обладаниесобственнымвидениемразвития проекта обоснованное профессиональнымопытом',
    # 'я по жизни мечтатель, мечтаю вот не засиживаться',
    ]

def main(data: list):
    dic = []
    bot = MarkupGPT(access_token)
    bot.enable_chat_mode()
    while data:
        i = data.pop() + '\n'
        lens = num_tokens_from_string(i)
        if lens >= 80:
            print(i, lens, sep='\n')
            bot.ask(prompt)
            print(bot.ask(i))
            bot.rollback_conversation(1)

        else:
            dic.append(i)
        token_sum = sum(map(num_tokens_from_string, dic))
        if token_sum > 80 or not data:
            str_d = '\n'.join(dic)
            dic.clear()
            print(str_d, token_sum, sep='\n')
            bot.ask(prompt)
            print(bot.ask(str_d))
            break

            bot.rollback_conversation(2)


def main(data: list):
    bot = MarkupGPT(access_token)
    bot.set_default_prompt(prompt)
    return bot.ask('\n'.join(data))
# for i in asks:
#     resp = bot.ask(i)
#     print(resp)

if __name__ == "__main__":

    print(main(data))
    # print(data)