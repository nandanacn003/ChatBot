import gradio
from groq import Groq
client = Groq(
    api_key="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",
)
def initialize_messages():
    return [{"role": "system",
             "content": """You are a skilled Teacher with a successful track record in clearing exams. Your role is to assist people by providing guidance on NET Exams and
             offering answers in a friendly way."""}]
messages_prmt = initialize_messages()
def customLLMBot(user_input, history):
    global messages_prmt
    
    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply
iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to Computer Application"),
                     title="Teacher ChatBot",
                     description="Chat bot for NET Exam Assistance",
                     theme="soft",
                     examples=["Hello","What is Class", "How to run script in Java"]
                     )
iface.launch(share=True)
    
