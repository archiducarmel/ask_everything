import os, time
from langchain import HuggingFaceHub
import streamlit as st 
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

st.title ("Ask everything 🤔🤔🤔")

llm = HuggingFaceHub(repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1", model_kwargs={"max_new_tokens": 512})

# Using "with" notation
with st.sidebar:
    st.title("Configuration")
    st.markdown('#') 
    token_length = st.number_input('Token length', 256,1024)

st.markdown('####') 
input_prompt = st.text_input('Tell me what you want', '')
st.markdown('#') 
st.markdown('#') 

if st.button('Process', type="primary"):
    with st.spinner('Processing in progress ...'): 
        st.balloons()   
        time.sleep(15)
        result = llm.invoke(input_prompt)
        result = os.linesep.join([s for s in result.splitlines() if s])

    
    st.markdown('#') 
    st.markdown('#') 

    print(result)

    txt = st.text_area("Result", result, height=512)
