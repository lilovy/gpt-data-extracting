import openai
from random import sample

from config import proxy_file
from .prompt_loader import LoadPrompt
from .proxy import get_proxy, proxy_from_file
from .data_transform import FindDict
from ..V1.markupGPT import MarkupGPT
from .tokenizer import num_tokens_from_string as token_sum
from ..database.init_database import DB


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


def get_ids_texts(data: list[tuple]):
    ids = []
    texts = []
    for id, text in data:
        ids.append(id)
        texts.append(text)
    return ids, texts

def combine(token, proxy):
    n = 20
    ns = 5000
    prompt = LoadPrompt('prompts/prompt_extract_data.txt').to_str
    proxy = 'http://' + proxy
    num = n
    data = sample(DB.get_raw_data(ns), num)

    while len(data) > 0:
        ids, texts = get_ids_texts(data)

        str_data = str(texts)
        while token_sum(str_data) > 200:
            num -= 1
            data = sample(DB.get_raw_data(ns), num)
            ids, texts = get_ids_texts(data)
            str_data = str(texts)
        print(len(texts), proxy)

        try:
            resp = GPTResponser(token, prompt=prompt, proxy=proxy).ask(str_data)

            dicts = FindDict(resp)
            if len(dicts) != num:
                print('info is lost')
            else:
                result = list(zip(ids, dicts))
                DB.insert_result_data(result)

        except Exception as e:
            print(e)
            pass

        data = sample(DB.get_raw_data(ns), num)
        num = n
        # break

