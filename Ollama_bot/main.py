import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-type': 'application/json',
}
with open("Ollama_bot\Source.txt", "r", encoding="utf-8") as file:
    source  = file.read()

conversation_history = [source]

# BASIC BOT

def generate_response(prompt):
    conversation_history.append(prompt)
    
    full_prompt = "\n".join(conversation_history)
    
    data = {
        "model": "mistral",
        "prompt": full_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        conversation_history.append(actual_response)
        return actual_response

    else:
        print("Error:", response.status_code, response.text)
        return None

iface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="text"
)


iface.launch()