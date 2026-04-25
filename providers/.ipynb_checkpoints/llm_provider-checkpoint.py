from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_response(messages, model="gpt-4o-mini", temperature=0):
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=messages
    )

    return response.choices[0].message.content