import tiktoken


encoding = tiktoken.get_encoding("cl100k_base")
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

phrase = """
Изучите список требований к соискателям.
Для каждого требования определите его тип (skill - навык, knowledge - знание, unknown - неизвестно).
Сформулируйте простую форму каждого требования, убрав из оригинала лишнее и избавившись от сложных конструкций. Если требование содержит несколько навыков/знаний, разделите их на отдельные строки.
Укажите тип требования (skill/knowledge/unknown) и полученную простую форму в формате:
{"original": "Оригинальный текст требования", "simple_form": ["Простая форма требования"], "tag": "Тип требования"}.
Повторите шаги 3-4 для всех требований в списке.
Сохраните все данные в формате JSON.
"""

encoding.encode("tiktoken is great!")


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


counts = num_tokens_from_string(phrase, "cl100k_base")

print(counts)