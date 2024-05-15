#Importing packages

import streamlit as st
from gpt4allj.langchain import GPT4AllJ

#Model Loading: 
#Download the model from: https://huggingface.co/qm9/ggml-gpt4all-j-v1.3-groovy.bin/resolve/main/ggml-gpt4all-j-v1.3-groovy.bin?download=true
#Load the downlaoded model from your local directory

llm = GPT4AllJ(model='C:/Users/vansh/Desktop/PC/ML/LLM/model/ggml-gpt4all-j-v1.3-groovy.bin')

#Setting up the layout and content for the streamlit web app

st.set_page_config(page_title = "Custom Chat GPT", layout = "wide")
st.markdown("<h1 style='text-align':centre;, '>Hello Vansh ! Welcome to your AI Chatbot</h1>", unsafe_allow_html  = True)
st.markdown("<h3 style='text-align':centre;, '>How may I help you today ?</h3>", unsafe_allow_html  = True)

#Adding some extra space on web app 
st.text("")
st.text("")


#Creating a Container/Box in the streamlit app 
with st.container():
    col1, col2, col3 = st.columns((0.10, 1, 0.10))
    with col1:
        pass
    with col2:
        input_qus = st.text_input("Ask me anything!")     #Creating the input text box
        button = st.button("Submit")     #Creating a button, by default False and returns True when you press it on web app.
    with col3:
        pass

    if button:  #Reading the button status
        st.info(llm(input_qus)) #Passing the input question to the model for inference.
