from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

class person(BaseModel):
    name: str = Field(description="Write the name of the person")
    age: int = Field(gt=18, description="Write the age of the person")
    city: str = Field(description="Write the city of the person")

parser = PydanticOutputParser(pydantic_object=person)

template1 = PromptTemplate(
    template="Write the details about the {place} fictional character \n {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template1 | model | parser

result = chain.invoke({"place": "Indian"})

print(result)