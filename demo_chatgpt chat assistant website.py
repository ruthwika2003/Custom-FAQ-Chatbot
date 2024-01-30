import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "what are the common queries regarding mental health?"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Mental Health")

demo.launch(share=True)