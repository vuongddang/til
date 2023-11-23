from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()
result = llm("What is the capital of France?")
print(result)