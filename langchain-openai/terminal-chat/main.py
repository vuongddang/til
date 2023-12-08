from langchain.chat_models import ChatOpenAI
from langchain.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.memory import ConversationSummaryMemory, FileChatMessageHistory
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(verbose=False)
# With ConversationSummaryMemory, for every call to OpenAI api, there's additional call to sumarize the conversation to be used as input for the next call
memory  = ConversationSummaryMemory(
    memory_key="messages", 
    return_messages=True,
    llm=chat # llm uses to sumarize the conversation
)
prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages = [
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}"),
    ],
)

chain = LLMChain(
    llm = chat,
    prompt = prompt,
    memory = memory,
    verbose=True # see what we send to llm
)
while True:
    content = input(">> ")
    result = chain({"content": content})
    print(result["text"])
