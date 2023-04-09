import tiktoken
from revChatGPT.V1 import AsyncChatbot
import asyncio
import pickle
from config import access_token




def load_pkl(file):
    with open(file, 'rb') as f:
        data = pickle.load(f)
    return data

data = load_pkl('data.pkl')[13113:13123]

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

async def resp(ask, prompt):
    chat: AsyncChatbot = AsyncChatbot(config={
                "access_token": access_token,
            })
    ask = ''
    async for i in chat.ask(prompt):
        res = await i
    async for i in chat.ask(prompt, chat.conversation_id):
        res = await i
    print(res)

async def main(prompt):
    coruts = []
    dic = []
    # prompt = ''
    for i in data:
        lens = num_tokens_from_string(i, "cl100k_base")
        if len(i) >= 100:
            coruts.append(resp(i, prompt))
        else:
            dic.append(i)
        if sum(map(len, dic)) > 100:
            str_d = '\n'.join(dic)
            dic.clear()
            coruts.append(resp(i, prompt))
    await asyncio.gather(*coruts)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main(prompt))

asyncio.run(main(prompt))
