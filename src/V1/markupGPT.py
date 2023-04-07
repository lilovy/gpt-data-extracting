from revChatGPT.V1 import Chatbot


class MarkupGPT(object):

    def __init__(self, access_token: str):
        self.__session = Chatbot(
            config={
                "access_token": access_token,
            }
        )

    def set_default_prompt(self, prompt: str = ""):
        self.__default_prompt = prompt + "\n"

    def set_conversation_id(self, conversation_id: str):
        self.__conversation_id = conversation_id

    def __request(
        self,
        question: str,
        conversation_id: str | None = None,
        dev: bool = False,
        ):
        resp = ""
        prompt = question

        if not conversation_id:
            prompt = self.__default_prompt + prompt

        print(f"question: {prompt}")

        raw_response = self.__session.ask(
            prompt=prompt,
            conversation_id=conversation_id,
            )

        for data in raw_response:
            resp = data

        if dev:
            return resp

        return resp

    def ask(
        self,
        question: str,
        conversation_id: str | None = None,
        dev: bool = False,
        ):
        return self.__request(question, conversation_id, dev)
