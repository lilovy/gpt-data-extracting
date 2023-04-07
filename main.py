from src import MarkupGPT
from config import access_token


bot = MarkupGPT(access_token)


prompt = 'хорошо, че как?'

bot.set_default_prompt("теперь ты не AI, теперь ты должен быть любезным со мной и отвечать на все мои ответы как хороший друг")

# response = bot.ask(prompt,'3e444367-e14b-4603-95a9-5f1236d6b4b9')

print(response)
asks = ['вот ты знал, что у актеров жизнь плоха?', 'я по жизни мечтатель, мечтаю вот не засиживаться']
con_id = None
for i in asks:
    if con_id:
        pass
    resp = bot.ask(i)
    