# Simple test with Ollama and Llama 3.2
from ollama import Client

client = Client(host='http://localhost:11434')
response = client.chat(model='llama3.2:3b', messages=[
    {'role': 'user', 'content': 'Hello, I am learning to build an AI agent. Can you suggest a task for me?'}
])
print(response['message']['content'])
