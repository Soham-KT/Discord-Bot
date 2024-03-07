import os
from openai import OpenAI
from dotenv import load_dotenv
from discord import Intents, Client, Message

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("CHATGPT_API_KEY"),
)

def gm_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "explain this to me like an old grand master assassin is teaching it to a novice assassin "
                           "(in short): " + prompt
            },
        ]
    )

    return response.choices[0].message.content
