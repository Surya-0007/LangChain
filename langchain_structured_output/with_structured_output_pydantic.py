from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["positive", "negative"] = Field(description="Return sentiment of the review")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros if mentioned in the review")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons if mentioned in the review")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The movie Se7en has one of the best stories I have ever watched""")

print(result.sentiment)