from dotenv import load_dotenv
from openai import OpenAI

#SECTION 1: SET UP THE ENVIRONMENT 
load_dotenv()
client = OpenAI()

#SECTION 2: READ THE GIVEN SYSTEM PROMPT AND THE SAMPLE CODE
f = open("cot.txt","r")
SYSTEM_PROMPT =f.read()
f.close()

f = open("sample1_code.txt","r")
CODE_INPUT=f.read()
f.close()


#SECTION 3: INVOKE THE LLM CALL
response = client.responses.create(
    model="gpt-5.6-luna",
    input=CODE_INPUT,
    instructions=SYSTEM_PROMPT
)

#SECTION 4: PRINT THE OUTPUT
#print(response)
#print("="*15)
print(response.output_text)
