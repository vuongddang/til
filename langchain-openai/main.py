from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--language", default = "Python")  # or "JavaScript" or "C#" or "TypeScript" or "PHP" or "Ruby" or "Go" or "Rust" or "Java" or "C" or "C++" or "Swift" or "Kotlin
parser.add_argument("--task", default = "return the square of a number")
args = parser.parse_args()

load_dotenv()

llm = OpenAI()

code_prompt = PromptTemplate(
    template= "Write a very short {language} function that will {task}",
    input_variables= ["language", "task"]
)

code_chain = LLMChain(llm=llm, prompt=code_prompt)

result = code_chain({
    "language": args.language, 
    "task": args.task
})

print(result["text"])