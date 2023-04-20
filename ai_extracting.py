import openai
from config import api_token, access_token2 as access_token
import gradio as gr
from prompts import load_prompt
from src.V1 import MarkupGPT

prmpt = """
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


openai.api_key = api_token

prompt = load_prompt('prompt_light_v2.txt')


def make_request(prompt, sys_prompt ):
    resp = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": sys_prompt},
            {"role": "assistant", "content": sys_prompt},
            {"role": "user", "content": sys_prompt},
        ],
        temperature=0,
    )


messages = [
    {"role": "system", "content": prompt},
    {"role": "user", "content": "Знание adaptive, responsive верстки"},
    {"role": "assistant", "content": """{"original": "Знание adaptive, responsive верстки", "simple_forms": [{"simple_form": "знание adaptive верстки", "tag": "knowledge"}, {"simple_form": "знание responsive верстки", "tag": "knowledge"}]}"""},
    {"role": "user", "content": "файер-вол, домен\nПроектные и мультимодальные перевозки;"},
    {"role": "assistant", "content": """{"original": "файер-вол, домен", "simple_forms": [{"simple_form": "файер-вол", "tag": "unknown"}, {"simple_form": "домен", "tag": "unknown"}]}, {"original": "Проектные и мультимодальные перевозки;", "simple_forms": [{"simple_form": "проектные перевозки", "tag": "skill"}, {"simple_form": "мультимодальные перевозки", "tag": "skill"}]}"""},
]

def chatbot(input):
    if input:
        # messages.append({"role": "user", "content": input})
        message = messages + [{"role": "user", "content": input}]
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=message,
            temperature=0,
        )
        reply = chat.choices[0].message.content
        # messages.append({"role": "assistant", "content": reply})
        return reply


# bot = MarkupGPT(access_token)
# bot.set_default_prompt(prmpt)

def chatgpt_req(input):
    if input:
        bot = MarkupGPT(access_token)
        bot.set_default_prompt(prmpt)
        return bot.ask(input)

def make_interface():

    inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
    outputs = gr.outputs.Textbox(label="Reply")

    gr.Interface(fn=chatgpt_req, inputs=inputs, 
                outputs=outputs, title="AI Chatbot",
                description="Ask anything you want",
                theme="compact").launch(share=True)

if __name__ == "__main__":
    make_interface()