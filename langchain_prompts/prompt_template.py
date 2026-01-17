from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
    Summarize the Research Paper on {paper_input} in the best way possible,
    keep the tone of explanation in {style_input} and length should be {length_input}
""",
input_variables=['paper_input', 'style_input', 'length_input'],
validate_template=True
)

template.save('template.json')