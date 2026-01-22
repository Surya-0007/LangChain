from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

url = "https://www.imdb.com/name/nm0006795/bio/"

loader = WebBaseLoader(url)

model = ChatOpenAI()

parser = StrOutputParser()

docs = loader.load()

prompt = PromptTemplate(
    template="Answer the following question about the text given \n {question} \n {text}",
    input_variables=["question", "text"]
)

chain = prompt | model | parser

result = chain.invoke({"question": "What is the real name of Salman Khan", "text": docs[0].page_content})

print(result)