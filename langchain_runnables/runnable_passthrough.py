from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a joke on the topic {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain this joke \n {joke}",
    input_variables=["joke"]
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_chain = RunnableSequence(prompt1 | model | parser)

chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": RunnableSequence(prompt2 | model | parser)
})

final_chain = RunnableSequence(joke_chain | chain)

result = final_chain.invoke({"topic": "Salman Khan"})

print(result)