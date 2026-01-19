from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()



prompt = PromptTemplate(
    template="Write 5 lines about {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

chains = prompt | model | parser

result = chains.invoke({"topic": "Cricket"})

print(result)

chains.get_graph().print_ascii()