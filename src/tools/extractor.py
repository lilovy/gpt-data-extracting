import openai
from config import (
    api_token,
    access_token2 as access_token,
    )
# from src.tools import LoadPrompt
# from src.tools import get_proxy
# from src.tools import FindDict
# from src.V1 import MarkupGPT

from .prompt_loader import LoadPrompt
from .proxy import get_proxy
from .data_transform import FindDict
from ..V1 import markupGPT
# from src.database import get_data


class GPTResponser(object):
    def __init__(
        self, 
        token: str,
        prompt: str | list[dict] = None,
        proxy: str = None, 
        ) -> None:

        if prompt:
            self.prompt = prompt
        else:
            self.prompt = ""

        self.__proxy = proxy
        self.__token = token

    def ask(self, question: str | list[dict]):

        if isinstance(question, str):
            question = self.prompt + question
            return self.__unofficial_request(question)

        if isinstance(question, list):
            if self.prompt != "":
                question = self.prompt + question
            return self.__official_request(question)

    @property
    def prompt(self) -> str:
        return self.__prompt

    @prompt.setter
    def prompt(self, prompt: str) -> None:
        self.__prompt = prompt

    def __official_request(self, message: list[dict]):
        openai.api_key = self.__token
        resp = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=message,
            temperature=0,
        )
        reply = resp.choices[0].message.content
        return reply

    def __unofficial_request(self, question: str):

        resp = MarkupGPT(
            access_token=self.__token,
            proxy=self.__proxy,
            )
        return resp.ask(question)


def combine(token):
    prompt = LoadPrompt('prompts/prompt_extract_data.txt')
    proxy = get_proxy()
    num = 20
    data: list = get_data(used=False, num=num)

    while len(data) > 0:
        texts = []
        ids = []
        for id, text in data:
            ids.append(id)
            texts.append(text)
        str_data = '\n'.join(texts)

        try:
            resp = GPTResponser(token, prompt=prompt, proxy=proxy).ask(str_data)

            dicts = FindDict(resp)
            if len(dicts) != num:
                save_bad_request(data)
            else:
                result = list(zip(ids, dicts))
                save_result(result)

        except Exception as e:
            save_bad_request(data)
            print(e)

        data: list = get_data(used=False, num=num)


def msg(prompt):
    return [
        {"role": "system", "content": prompt},
        {"role": "user", "content": "Знание adaptive, responsive верстки"},
        {"role": "assistant", "content": """{"original": "Знание adaptive, responsive верстки", "simple_forms": [{"simple_form": "знание adaptive верстки", "tag": "knowledge"}, {"simple_form": "знание responsive верстки", "tag": "knowledge"}]}"""},
        {"role": "user", "content": "файер-вол, домен\nПроектные и мультимодальные перевозки;"},
        {"role": "assistant", "content": """{"original": "файер-вол, домен", "simple_forms": [{"simple_form": "файер-вол", "tag": "unknown"}, {"simple_form": "домен", "tag": "unknown"}]}, {"original": "Проектные и мультимодальные перевозки;", "simple_forms": [{"simple_form": "проектные перевозки", "tag": "skill"}, {"simple_form": "мультимодальные перевозки", "tag": "skill"}]}"""},
        ]

def resp(token, messages: str | list[dict], proxy: str = None, prompt: str = None):
    response = GPTResponser(token, proxy=proxy, prompt=prompt)
    return response.ask(message)


if __name__ == "__main__":
    cont = "мультимодальные перевозки"

    prompt = LoadPrompt('prompts/prompt_extract_data.txt')  
    prompt += cont
    print(resp(access_token, question))

    prompt = LoadPrompt('prompts/prompt_light_v2.txt')
    messages = msg(prompt) + {"role": "user", "content": cont}
    print(resp(api_token, messages, prompt=prompt))
