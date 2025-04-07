# Thoughtful AI Support Agent

A simple customer support AI agent built to answer questions about Thoughtful AI's products and services.

## Overview

This application provides a conversational interface where users can ask questions about Thoughtful AI's agents. The system matches user queries against a predefined set of questions and returns the most relevant answer. For questions outside its knowledge base, it responds with a friendly fallback message.

## Features

- Web-based chat interface using Streamlit
- Fuzzy matching algorithm to find the most relevant answers
- Predefined responses for common questions about Thoughtful AI agents
- Clean, user-friendly UI with conversation history

## How to Run

### Option 1: Run Locally

1. Clone this repository:
   ```
   git clone https://github.com/ghazikhanihamed/thoughtful-ai-agent.git
   cd thoughtful-ai-agent
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run app.py
   ```

4. Open your browser and navigate to `http://localhost:8501`

## Implementation Details

The agent uses a simple but effective string matching algorithm to find the most similar question in its knowledge base. It maintains conversation history for a better user experience and provides helpful responses when it doesn't have specific information about a query.

## Future Improvements

With more time, potential enhancements could include:
- Expanding the knowledge base
- Implementing more sophisticated NLP for query understanding
- Adding additional conversation contexts
- Integrating with external documentation
