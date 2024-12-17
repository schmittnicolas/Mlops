from huggingface_hub import login
import torch
import os
# Log in with your Hugging Face token
token = os.getenv("TOKEN")
print("-------------------TOKEN-------------------")
print(token)
print("-------------------TOKEN-------------------")

login(token=token)

from transformers import pipeline


device = 'cuda' if torch.cuda.is_available() else 'cpu'

def generate_output(instruction, prompt):

    instruction = instruction + "Message:" + prompt + "\nMeme:"
    
    pipe = pipeline("text-generation", model="meta-llama/Llama-3.2-1B", device=device )
    generated_text = pipe(instruction, max_new_tokens=30, truncation=True)[0]['generated_text']

    generated_part = generated_text[len(instruction):].strip()

    
    print('generated_text:', generated_part)

    return generated_part




