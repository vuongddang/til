from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
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
code_chain = LLMChain(llm=llm, prompt=code_prompt, output_key="code")

unit_test_prompt = PromptTemplate(
    template = "Write a test for the following {language} code:\n{code}",
    input_variables = ["language", "code"]
)
unit_test_chain = LLMChain(llm=llm, prompt=unit_test_prompt, output_key="test") 


chain = SequentialChain(
    chains=[code_chain, unit_test_chain],
    input_variables=["language", "task"],
    output_variables=["code", "test"]  # Add "test" to the output variables
)

result = chain({
    "language": args.language, 
    "task": args.task
})

print("Generated code:")
print(result["code"])
print("\n\n")

print("Generated test:")
print(result["test"])