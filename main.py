import streamlit as st
import openai

st.title("💬 Free ChatGPT Chatbot")

openai_api_key = st.text_input("Enter your OpenAI API Key:", type="password")

if openai_api_key:
    user_input = st.text_area("You:", placeholder="Ask me anything...")
    
    if st.button("Send"):
        if user_input:
            with st.spinner("ChatGPT is typing..."):
                try:
                    openai.api_key = openai_api_key
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "user", "content": user_input}
                        ]
                    )
                    bot_reply = response.choices[0].message["content"]
                    st.markdown(f"**ChatGPT:** {bot_reply}")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a message!")
