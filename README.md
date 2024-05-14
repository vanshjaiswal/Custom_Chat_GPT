# Custom Chat GPT
Hello! My name is Vansh Jaiswal and I am a data guy. Welcome to this new tutorial. 

It's time to build your own Chat GPT ! 

In this project we are building your own custom Chat GPT which you can run on your local machine.





## Installation

Install the requirements.txt file with the below command

```bash
  pip install -r requirement.txt
```
    
## Model

Now it's time to download the LLM model. For this project we are going to use the GPT4All-GGML model from huggingface. 

Don't have GPU ? No worries ! You can run this model on your local machine on CPU. 

Download this model from this link: 

https://huggingface.co/qm9/ggml-gpt4all-j-v1.3-groovy.bin/resolve/main/ggml-gpt4all-j-v1.3-groovy.bin?download=true

Now store this model into a "model" folder in your src. 



## Streamlit Web App

Now we are all set to build our frontend using the Streamlit framework.
No need of HTML, CSS or any frontend building tool.

Streamlit will help you to build your own UI with simple python code. The source code is available at *streamlit.py* file.
## Executing Streamlit

We are all set to launch our Custom Chat GPT ! 
Run the below command from the terminal for executing the code.

```bash
 streamlit run streamlit.py
```
This will automatically open a new tab in your browser.

Voila ! Your own Custom Chat GPT is done and ready to use. 