from dotenv import load_dotenv
from openai import OpenAI
# import os

#env
result = load_dotenv(
    dotenv_path=r"Part1-30days\.env",
    encoding="utf-8"
)
# print(result)
# print(os.getenv("OPENAI_API_KEY"))
client= OpenAI()

while True:
    #INPUT
    user = input("你：")
    # print(user)

    #when jump out loop.
    if user=="exit":
        break

    #put user into openai and get value response
    response = client.responses.create(
        model="gpt-5.5",
        input= user
    )

    print(response.output_text)