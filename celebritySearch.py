import os
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory

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

# memory

person_memory= ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory=ConversationBufferMemory(input_key='person', memory_key='chat_history')
desc_memory= ConversationBufferMemory(input_key='dob', memory_key='description_history')

llm=OpenAI(temperature = 0.8)
chain=LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person', memory=person_memory)

second_input_prompt=PromptTemplate(
    input_variables=['person'],
    template="Mention the year of when was {person} born"
)

chain2=LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob', memory=dob_memory)

third_input_prompt=PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major points happened in {dob} around the world"
)

chain3=LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='description', memory=desc_memory)

parent_chain=SequentialChain(chains=[chain, chain2, chain3], input_variables=['name'], output_variables=['person', 'dob', 'description'], verbose=True)

if input_text:
    st.write(parent_chain({'name': input_text}))
    
    with st.expander('Person Name'):
        st.info(person_memory.buffer)
        
    with st.expander('Person DOB'):
        st.info(dob_memory.buffer)
        
    with st.expander('description'):
        st.info(desc_memory.buffer)