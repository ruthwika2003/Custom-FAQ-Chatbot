import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-type': 'application/json',
}

def generate_response():
    data = {
        "model": "mistral",
        "prompt": "Why is mental health important?",
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        return actual_response
    
    else:
        print("Error:", response.status_code, response.text)
        return None
    
iface = gr.Interface(
    fn=generate_response,
    inputs=gr.inputs.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="text"
)

iface.launch()