from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

json_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Write down all the key themes in the review"
        }
    },
    "required": ["key_themes"]
}
    


structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""The movie Se7en has one of the best stories I have ever watched""")

print(result)