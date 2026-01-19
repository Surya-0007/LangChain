from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed 2 paragraph notes on the following text \n {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="Generate a 5 question answers on the folowing text \n {text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="Merge the following notes and quiz into one \n {notes} and {quiz}",
    input_variables=["notes", "quiz"]
)

model1 = ChatOpenAI()

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": prompt1 | model1 | parser,
    "quiz": prompt2 | model1 | parser
})

chains = parallel_chain | prompt3 | model1 | parser

text = """
Salman Khan is an Indian actor, film producer, and television personality who predominantly works in Hindi films. In a career spanning over three decades, his awards include two National Film Awards as a film producer, and two Filmfare Awards as an actor
"""

result = chains.invoke({"text": text})

print(result)

chains.get_graph().print_ascii()