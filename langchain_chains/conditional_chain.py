from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from typing import Literal

load_dotenv()

model = ChatOpenAI()

class feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Classify the sentiment of the feedback")

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template="Write the appropriate response to this positive feedback \n {positive_feedback}",
    input_variables=["positive_feedback"]
)

prompt3 = PromptTemplate(
    template="Write the appropriate response to this negative feedback \n {negative_feedback}",
    input_variables=["negative_feedback"]
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "positive", prompt2 | model | parser),
    (lambda x:x.sentiment == "negative", prompt3 | model | parser),
    (RunnableLambda(lambda x: "Could not find sentiment"))
)

chain = classifier_chain | branch_chain

result = chain.invoke({"feedback": "This movie was not that good as expected"})

print(result)

chain.get_graph().print_ascii()