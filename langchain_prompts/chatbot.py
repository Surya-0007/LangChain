from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

ChatHistory = []

while True:
    user_input = input('You ')
    ChatHistory.append(HumanMessage(content=user_input))
    if user_input == 'Exit':
        break
    result = model.invoke(ChatHistory)
    ChatHistory.append(AIMessage(content=result.content))
    print('AI: ', result.content)

print(ChatHistory)
