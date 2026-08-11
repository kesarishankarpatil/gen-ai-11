from dotenv import load_dotenv
from openai import OpenAI

#load the .env file
load_dotenv()

#ASK FOR CUSTOMER QUERY
query= input("Enter your query:")

#MAKE THE REQUEST TO OPENAI LLM
client = OpenAI()
response = client.responses.create(
    model= "gpt-5.6-luna",
    input= [
        {
            "role":"user",
            "content":"Hello, My name is Kesari"
        },
        {
            "role":"assistant",
            "content":"Sure, Kesari—what’s your query?"
        },
        {
            "role":"user",
            "content":query
        }
    ]
)
print(response.output_text)