from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Return sentiment of the review"]
    pros: Annotated[Optional[list[str]], "Write down all the pros if mentioned in the review"]
    cons: Annotated[Optional[list[str]], "Write down all the cons if mentioned in the review"]


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The movie Se7en has one of the best stories I have ever watched""")

print(result)
print(result["summary"])
print(result["sentiment"])