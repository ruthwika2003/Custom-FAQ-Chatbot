import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)