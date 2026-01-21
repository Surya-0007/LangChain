from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report on the topic \n {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the text \n {text}",
    input_variables=["text"]
)

model = ChatOpenAI()

parser = StrOutputParser()

sequence_chain = RunnableSequence(prompt1 | model | parser)

branch_runnable = RunnableBranch(
    (lambda x : len(x.split()) > 500, RunnableSequence(prompt2 | model | parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(sequence_chain | branch_runnable)

result = final_chain.invoke({"topic": "Salman Khan"})

print(result)