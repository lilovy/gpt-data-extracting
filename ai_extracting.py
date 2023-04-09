import openai
from config import api_token
import gradio as gr
from prompts import load_prompt


openai.api_key = api_token

prompt = load_prompt('prompt_light.txt')


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
    {"role": "assistant", "content": """{"original": "Знание adaptive, responsive верстки", "simple_form": ["знание adaptive верстки", "знание responsive верстки"], "tag": "knowledge"}"""},
    {"role": "user", "content": "файер-вол, домен\nПроектные и мультимодальные перевозки;"},
    {"role": "assistant", "content": """{"original": "файер-вол, домен", "simple_form": ["файер-вол", "домен"], "tag": "unknown"}, {"original": "Проектные и мультимодальные перевозки;", "simple_form": ["проектные перевозки", "мультимодальные перевозки"], "tag": "skill"}"""},
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


def make_interface():

    inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
    outputs = gr.outputs.Textbox(label="Reply")

    gr.Interface(fn=chatbot, inputs=inputs, 
                outputs=outputs, title="AI Chatbot",
                description="Ask anything you want",
                theme="compact").launch(share=True)

if __name__ == "__main__":
    make_interface()