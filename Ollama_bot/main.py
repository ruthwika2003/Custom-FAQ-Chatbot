import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-type': 'application/json',
}

# BASIC BOT

def generate_response():
    data = {
        "model": "llama2:7b",
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

# CUSTOM BOT

urls = [
    'https://www.medicalnewstoday.com/articles/73936'
    'https://www.totalhealthandfitness.com/what-is-mindful-eating-your-complete-guide-to-enjoying-your-food-more/'
    'https://www.totalhealthandfitness.com/nutrition-and-chronic-disease/'
    'https://www.glofox.com/blog/fitness-blogs/'
]

def answer():
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            if text:
                return f"{text[0]}"
        
        except Exception as e:
            print(f"Error processing URL : {e}")
    
    return f"Sorry I couldn't find the answer to your questions."
    

iface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="text"
)


iface.launch()