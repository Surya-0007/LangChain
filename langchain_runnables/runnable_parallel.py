from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a joke on the topic, for tweeter \n {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Write a joke on the topic, for LinkedIn \n {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = RunnableParallel({
    "Tweet": RunnableSequence(prompt1 | model | parser),
    "LinkedIn": RunnableSequence(prompt2 | model | parser)
})

result = chain.invoke({"topic": "Salman Khan"})

print(result)