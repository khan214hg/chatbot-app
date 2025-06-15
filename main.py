import streamlit as st
from openai import OpenAI

st.title("💬 ChatGPT Chatbot")

# API key input
api_key = st.text_input("Enter your OpenAI API key", type="password")

# Prompt input
prompt = st.text_input("Ask me anything")

if st.button("Send"):
    if not api_key:
        st.error("Please enter your API key!")
    elif not prompt:
        st.error("Please enter your question!")
    else:
        client = OpenAI(api_key=api_key)
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.success("Response:")
            st.write(response.choices[0].message.content)

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    st.success("Response:")
    st.write(response.choices[0].message.content)

except openai.RateLimitError:
    st.error("Rate limit exceeded! Please try again later or check your API usage.")
except Exception as e:
    st.error(f"An error occurred: {e}")
