#!/usr/bin/env python3

""" Alternative Chat Model """

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
]


# ---- LangChain Llama3.1 Chat Model Example ----

# Create a ChatOllama model
model = ChatOllama(model="llama3.1:8b", temperature=0.4)

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from Llama3.1: {result.content}")


# ---- Gemma2 Chat Model Example ----

# Create a Gemma2 model
model = ChatOllama(model="gemma2:9b", temperature=0.4)

result = model.invoke(messages)
print(f"Answer from Gemma2: {result.content}")


# ---- MistralChat Model Example ----

model = ChatOllama(model="mistral:7b", temperature=0.4)

result = model.invoke(messages)
print(f"Answer from Mistral: {result.content}")
