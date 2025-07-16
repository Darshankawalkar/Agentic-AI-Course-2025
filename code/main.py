# Simple test with Ollama and Llama 3.2
from ollama import Client

client = Client(host='http://localhost:11434')
response = client.chat(model='llama3.2:3b', messages=[
    {'role': 'user', 'content': 'Hello, I am learning to build an AI agent. Say hi!'}
])
print(response['message']['content'])
