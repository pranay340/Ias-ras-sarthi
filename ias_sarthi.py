
import streamlit as st
import openai
import os

# Load OpenAI API Key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Page setup
st.set_page_config(page_title="IAS-RAS Sarthi Chatbot", page_icon="📘")
st.title("📘 IAS-RAS Sarthi – Your Civil Services Study Assistant")
st.caption("Ask doubts, get notes, GS + Rajasthan-specific summaries, MCQ help, Ethics case studies & more!")
st.markdown("🧠 **Welcome, future officer!** Type your UPSC or RAS query below.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask your UPSC/RAS question here...")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    system_prompt = """
    You are 'IAS-RAS Sarthi', a helpful AI assistant for UPSC IAS and RPSC RAS aspirants.
    - Answer in a mix of English and Hindi (easy Hindi words).
    - Provide UPSC + RAS-specific guidance, including Rajasthan-based topics.
    - Use simple, motivating, exam-oriented language.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ],
        max_tokens=800,
        temperature=0.6
    )

    bot_reply = response["choices"][0]["message"]["content"]
    st.chat_message("assistant").markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
