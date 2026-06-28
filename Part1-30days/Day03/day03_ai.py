from dotenv import load_dotenv
from openai import OpenAI
import os

result=load_dotenv(
    dotenv_path=r"Part1-30days\.env",
    encoding="utf-8"
            )

# print(result)
# print(os.getenv("OPENAI_API_KEY"))

client = OpenAI()
response = client.responses.create(
model="gpt-5.5",
input="Hello! This is my first AI program!")

print(response.output_text)