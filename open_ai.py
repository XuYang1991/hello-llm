import os
from openai import OpenAI

print(os.getenv("OPENAI_API_KEY"))
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "what's the weather, response in chinese",
        }
    ],
    model="gpt-4o-mini",
)
print(chat_completion)