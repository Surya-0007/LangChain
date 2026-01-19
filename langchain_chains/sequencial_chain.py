from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following text into 5 points \n {text}",
    input_variables=["text"]
)

model = ChatOpenAI()

parser = StrOutputParser()

chains = prompt1 | model | parser | prompt2 | model | parser

result = chains.invoke({"topic": "Cricket"})

print(result)

chains.get_graph().print_ascii()