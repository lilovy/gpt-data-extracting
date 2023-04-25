import tiktoken


phrase = """
Изучите список требований к соискателям.
Для каждого требования определите его тип (skill - навык, knowledge - знание, unknown - неизвестно).
knowledge - это понимание того, как что-то работает или что-то означает.
skill - это умение применять знания в практических ситуациях или выполнять определенные задачи с опытом и мастерством.
Сформулируйте самую простую форму каждого требования, убрав из оригинала лишнее и избавившись от сложных конструкций. Если требование содержит несколько навыков/знаний, разделите их на отдельные строки.
Укажите тип требования (skill/knowledge/unknown) и полученную простую форму в формате:
{"original": "Оригинальный текст требования", "simple_forms": [{"simple_form": "Простая форма требования", "tag": "Тип требования"}]}.
Повторите шаги 3-4 для всех требований в списке.
Сохраните все данные в формате JSON.

Я: 
['Знание adaptive, responsive верстки']

ChatGPT: 
{"original": "Знание adaptive, responsive верстки", "simple_forms": [{"simple_form": "знание adaptive верстки", "tag": "knowledge"}, {"simple_form": "знание responsive верстки", "tag": "knowledge"}]}

Я:
['Описание, моделирование (желательно Bizagi) и/или оптимизация бизнес-процессов;', 'Знание нотаций IDEF0, DFD, IDEF3 и умение работать в стандарте BPMN;']

ChatGPT:
{"original": "Описание, моделирование (желательно Bizagi) и/или оптимизация бизнес-процессов;", "simple_forms": [{"simple_form": "описание бизнес-процессов", "tag": "skill"}, {"simple_form": "моделирование бизнес-процессов", "tag": "skill"}, {"simple_form": "оптимизация бизнес-процессов", "tag": "skill"}]}, {"original": "Знание нотаций IDEF0, DFD, IDEF3 и умение работать в стандарте BPMN;", "simple_forms": [{"simple_form": "знание нотации IDEF0", "tag": "knowledge"}, {"simple_form": "знание нотации DFD", "tag": "knowledge"}, {"simple_form": "знание нотации IDEF3", "tag": "knowledge"}, {"simple_form": "умение работать в стандарте BPMN", "tag": "skill"}]}

Я:
"""


def num_tokens_from_string(string: str, model_name: str = "gpt-3.5-turbo") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


if __name__ == "__main__":
    counts = num_tokens_from_string(phrase, "gpt-3.5-turbo")
    print(counts)