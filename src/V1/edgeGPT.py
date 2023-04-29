import asyncio
import json
from time import sleep
from EdgeGPT import Chatbot, ConversationStyle
from ..tools.prompt_loader import LoadPrompt
from ..tools.timer import async_timer

with open('./cookies/cookies2.json', 'r') as f:
    cookies = json.load(f)

prompt = LoadPrompt('prompts/prompt_extract_data_bing.txt').to_str
proxy = "http://4mfV1C:WBKQk4@45.153.20.233:11371"

prompt += str(
    [
        # 'Инициативность и нацеленность на результат', 
        # 'Отличные организаторские способности', 
        # 'Способность работать в стрессовой ситуации',
        'Хорошее знание СКД и языка запросов, опыт анализа и построения сложных запросов.',
        'Опыт разработки на управляемых формах под тонкий- и веб-клиент.',
        'Опыт разработки на обычных формах под толстый клиент (как правило, для обратной совместимости).',
        ]
    )

# print(len(prompt))

class BingGPT:
    def __init__(self, cookies: dict | list[dict], proxy: str = None):
        self.cookies = cookies
        self.proxy = proxy
        self.__bot = Chatbot(cookies=self.cookies, proxy=self.proxy)
    
    @async_timer
    async def ask(self, prompt: str, debag: bool = False):
        request = await self.__bot.ask(
            prompt=prompt,
            conversation_style=ConversationStyle.precise,
            wss_link="wss://sydney.bing.com/sydney/ChatHub",
        )
        response = request["item"]["messages"][1]["adaptiveCards"][0]["body"][0]["text"]
        await self.__bot.close()
        if debag:
            return request
        return request["item"]["messages"][1]['text']
        return response

async def amain(cookies, prompt):
    bot = Chatbot(cookies=cookies, proxy="http://4mfV1C:WBKQk4@45.153.20.233:11371")
    resp = await bot.ask(
        prompt=prompt, 
        conversation_style=ConversationStyle.precise, 
        wss_link="wss://sydney.bing.com/sydney/ChatHub",
        )
    # json.dump(resp, 'resp.json')
    print(resp["item"]["messages"][1])
    await bot.close()


def main(bot: BingGPT, prompt):
    return asyncio.run(bot.ask(prompt=prompt))
    # asyncio.run(amain(cookies, prompt))

async def main_loop():
    bot = BingGPT(cookies, proxy)
    n = 0
    while n < 2:
        n += 1
        try:
            task = asyncio.create_task(bot.ask(prompt, True))
            print(await task)
        except Exception as e:
            print(e)
        sleep(1)

def get_loop():
    asyncio.run(main_loop())

if __name__ == "__main__":
    print(main())
    # asyncio.run(amain(cookies, prompt))
