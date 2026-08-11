from dotenv import load_dotenv
from openai import OpenAI

#load the .env file
load_dotenv()

#MAKE THE REQUEST TO OPENAI LLM
client = OpenAI()
response = client.responses.create(
    model= "gpt-5.6-luna",
    input= input("Enter the Query")
)
print(response.output_text) 