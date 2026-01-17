from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

template = load_prompt('template.json')

model = ChatOpenAI()

st.header('Research Tool')

paper_input = st.selectbox("Select Research Paper Name", ["Attention is all you need", "Black Coffee Analogy", "Social Media is not good"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 Paragraphs)", "Medium (3-5 Paragraphs)", "Long (6-8 Paragraphs)"])


prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
}
)

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)