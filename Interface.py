from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load fine-tuned model and tokenizer
model_path = Model_Fine_Tuning.py  # Path to the directory containing the fine-tuned model
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

# Set the device to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Define function for generating response
def generate_response(prompt, max_length=50):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    output_ids = model.generate(input_ids, max_length=max_length, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return response

# CLI for interacting with the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    else:
        response = generate_response(user_input, max_length=100)
        print("Chatbot:", response)
