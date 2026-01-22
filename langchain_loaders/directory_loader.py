from langchain_community.document_loaders import TextLoader, PyPDFLoader, DirectoryLoader
from dotenv import load_dotenv

load_dotenv()

loader1 = DirectoryLoader(
    path="folder",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

loader2 = DirectoryLoader(
    path="folder",
    glob="*.txt",
    loader_cls=TextLoader
)

docs = loader1.load() + loader2.load()

print(len(docs))