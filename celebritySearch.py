import os
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv


import streamlit as st


st.title('Celebrity Search Results')
input_text = st.text_input("Search about the celebrity you want: ")

print(load_dotenv())

os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")

#prompt Template

first_input_prompt=PromptTemplate(
    input_variables=['name'],
    template="Tell me about {name}"
)

llm=OpenAI(temperature = 0.8)
chain=LLMChain(llm=llm, prompt=first_input_prompt, verbose=True)

if input_text:
    st.write(chain.run(input_text))