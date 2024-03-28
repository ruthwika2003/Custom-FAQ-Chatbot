import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-type': 'application/json',
}

conversation_history = []

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

# THE METHOD IS RUNNING SUCCESSFULLY



# CUSTOM BOT

'''
from bs4 import BeautifulSoup

urls = [
    'https://www.medicalnewstoday.com/articles/73936'
    'https://www.totalhealthandfitness.com/what-is-mindful-eating-your-complete-guide-to-enjoying-your-food-more/'
    'https://www.totalhealthandfitness.com/nutrition-and-chronic-disease/'
    'https://www.glofox.com/blog/fitness-blogs/'
]

def answer(urls):
    answers = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            answer_element = soup.find('div', class_='answer')

            if answer_element:
                answer_text = answer_element.text.strip()
                answers.append(answer_text)        
        
        except Exception as e:
            print(f"Error processing URL : {url} - {e}")
    
    if answers:
        return "\n".join(answers)
    
    else:
        return "Sorry, I couldn't find the answer to your questions."
    

iface = gr.Interface(
    fn=answer,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="text"
)


iface.launch()
'''
# THE METHOD IS UNABLE TO PROCESS THE URLS