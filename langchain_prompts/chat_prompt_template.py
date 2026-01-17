from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
     ('user', 'Explain me about {topic}')

])

prompt = chat_template.invoke({'domain':'cricket', 'topic':'dusra'})

print(prompt)