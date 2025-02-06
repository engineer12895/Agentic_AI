# step 1: Setup UI with streamlit
import streamlit as st

st.set_page_config(page_title="LangGraph AI Agent", page_icon="🤖", layout="centered")
st.title("AI Agent ChatBot")
st.write("This is a simple UI for interacting with the LangGraph AI Agent")

system_prompt = st.text_area("# define you AI agent", height=70, placeholder="Type your prompt here...")    

Modles_name_Groq = ['llama-3.3-70b-versatile', 'deepseek-r1-distill-llama-70b', 'mixtral-8x7b-32768']


provider =  st.radio("Select AI Model", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("selected Groq model", Modles_name_Groq)
else:
    st.write("OpenAI is not supported yet")

allow_search = st.checkbox("Allow Web Search?")

user_query = st.text_area("Type your query here...", height=150, placeholder="Ask me anything...")

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask agent"):
    st.write("Agent is thinking...")
# Step 2: Connect with backend via URL
    import requests
    payload = {
        "model_name": selected_model,
        "model_provider": provider,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": allow_search
    }
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        response_data = response.json()
        if "error" in response_data:
            st.write("Error in response")
            st.write(response_data["error"])
        else:
            st.write("AI Agent Response:")
            st.write(response_data)
