from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

def counter(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template="Write a joke on the topic {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()

parser = StrOutputParser()

sequence_chain = RunnableSequence(prompt1 | model | parser)

parallel_runnable = RunnableParallel({
    "joke": RunnablePassthrough(),
    "count": RunnableLambda(counter)
})

final_chain = RunnableSequence(sequence_chain | parallel_runnable)

result = final_chain.invoke({"topic": "Salman Khan"})

print(result)