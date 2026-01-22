from langchain_community.document_loaders import CSVLoader
from dotenv import load_dotenv

load_dotenv()

loader = CSVLoader("zone-guide-template.csv")

docs = loader.load()

print(docs[1])