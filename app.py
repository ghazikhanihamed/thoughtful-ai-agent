import streamlit as st
import json
from difflib import get_close_matches

# Load predefined responses
PREDEFINED_DATA = {
    "questions": [
        {
            "question": "What does the eligibility verification agent (EVA) do?",
            "answer": "EVA automates the process of verifying a patient's eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
        },
        {
            "question": "What does the claims processing agent (CAM) do?",
            "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
        },
        {
            "question": "How does the payment posting agent (PHIL) work?",
            "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
        },
        {
            "question": "Tell me about Thoughtful AI's Agents.",
            "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
        },
        {
            "question": "What are the benefits of using Thoughtful AI's agents?",
            "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
        }
    ]
}

def find_best_match(user_question, questions):
    """Find the most similar question to the user input"""
    questions_list = [q["question"].lower() for q in questions]
    matches = get_close_matches(user_question.lower(), questions_list, n=1, cutoff=0.6)
    
    if matches:
        return questions[questions_list.index(matches[0])]
    return None

def get_answer(user_question):
    """Get the answer based on user question"""
    match = find_best_match(user_question, PREDEFINED_DATA["questions"])
    
    if match:
        return match["answer"]
    else:
        return "I don't have specific information about that. As a Thoughtful AI support agent, I can help with questions about our AI agents like EVA, CAM, and PHIL. How else can I assist you?"

# Set up the Streamlit app
st.title("Thoughtful AI Support Agent")
st.write("Ask me questions about Thoughtful AI's agents!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get agent response
    response = get_answer(prompt)
    
    # Display agent response
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add agent response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
