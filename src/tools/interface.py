import gradio as gr


def hello(input):
    if input:
        return f"Hi {input}"

def make_interface(func):

    inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
    outputs = gr.outputs.Textbox(label="Reply")

    gr.Interface(fn=func, inputs=inputs, 
                outputs=outputs, title="AI Chatbot",
                description="Ask anything you want",
                ).launch(share=True)


if __name__ == "__main__":
    make_interface(hello)
