import os
import torch

from uuid import uuid4
torch.classes.__path__ = [os.path.join(torch.__path__[0], torch.classes.__file__)] 

from app.llm import get_ai_response

import streamlit as st

SESSION_ID = str(uuid4())

st.title("AI Tutor")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What you want to learn today?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("🤔 Thinking..."):
        response = get_ai_response(prompt, SESSION_ID)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
