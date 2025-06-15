import streamlit as st
import openai

st.title("💬 ChatGPT Chatbot")

# API key box
api_key = st.text_input("Enter your OpenAI API key", type="password")

# Prompt box
prompt = st.text_input("Ask me anything")

if st.button("Send"):
    if not api_key:
        st.error("Please enter your API key!")
    elif not prompt:
        st.error("Please enter your question!")
    else:
        openai.api_key = api_key
        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.success("Response:")
            st.write(response.choices[0].message["content"])
