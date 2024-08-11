#!/usr/bin/env python3

""" Basic Chat Model """

# Chat Model Documents:
# https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents:
# https://python.langchain.com/v0.2/docs/integrations/chat/ollama/

from langchain_ollama import ChatOllama

# Create a ChatOpenAI model
model = ChatOllama(model="llama3.1:8b", temperature=0.4)

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
