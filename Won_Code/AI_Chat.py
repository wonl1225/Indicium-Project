from apikey import APIKEY
from openai import OpenAI
client = OpenAI(api_key=APIKEY)

conversation = []

print("this is AI Chat (type 'E' to quit)")

while True:
    user_input = input("You: ")

    if user_input.upper() == "E":
        break

    conversation.append({"role": "user", "content": user_input})

    response = client.responses.create(model="gpt-5-mini", input=conversation)

    reply = response.output_text
    print("AI:", reply)

    conversation.append({"role": "assistant", "content": reply})