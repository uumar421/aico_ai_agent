# AICO AI Agent – Smart Web Summarizer with Follow-Up Context

AICO AI Agent is a LangChain-powered web summarization service that reads, summarizes, and answers follow-up questions about any webpage using conversational memory and an intelligent LLM prompt system. 

## Features

- Summarizes any publicly accessible webpage  
- Identifies and returns the **main topic** along with a structured summary  
- Supports **follow-up questions** about the summarized content  
- Uses **LangChain agents + memory** for contextual replies  
- Clean **FastAPI** interface with structured JSON responses  
- Built with **modular, testable architecture**  
- Custom prompt engineering for high-quality summaries  
- Environment variable support for API keys via `.env` file  
- Easily deployable and extendable

## Technologies Used

- Python 3.10+
- FastAPI (async API framework)
- LangChain (agents, memory, prompting, tools)
- ChatGroq LLM (llama-3.3-70b-versatile)
- Pydantic (validation & typing)
- Python dotenv (secure env handling)

##  How It Works

1. **User inputs a URL** via API (/summarize).
2. LangChain tools extract and summarize the page content using `WebBaseLoader`.
3. The custom summarization chain extracts a **main topic** and a **concise summary**.
4. Conversation memory (via `ConversationBufferWindowMemory` and JSON file) stores the last 3 interactions.
5. Follow-up questions can be asked in context — via API (/follow-up).

---

## Project Structure

```
aico_ai_agent/
├── main.py                             # Entry point for the flow
├── config.py                           # LLM, prompt, memory, and chain setup
├── agents/summarizer_agent.py          # Chain execution for LangChain agent
├── models/schemas.py                   # Validation through pydantic schemas
├── services/summarize_service.py       # Core summarization service layer
├── tools/browser_tool.py               # Web content loader wrapper
├── utils/chat_memory.py                # Chat history conversation logic
├── requirements.txt                    # Dependencies list
├── test_script.py                      # Simple test script with example calls
└── README.md                           # Project documentation
```

## How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/uumar421/aico_ai_agent.git
cd aico_ai_agent
```

### 2. Installation and Setup

To set up the project, setup a virtual environment and install the required dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the root with:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

To run LLM via ChatGroq, visit their [webpage](https://console.groq.com/keys), generate an api_key and add it inside llm_service module or set as environment variable.
This project uses open-source cloud hosted LLM through ChatGroq. To use any other available llm, set the **api_key** in .env file and change the configuration in **config.py** file.

### 4. Run the Server

```bash
uvicorn main:app --reload
```

Run the included test script to ensure that setup is successful:

```bash
python test_script.py
```


## API Endpoints

### POST /summarize

Request:
{
  "url": "https://example.com"
}

Response:
{
  "main_topic": "AI in Education",
  "summary": "The website discusses the impact of AI on modern education..."
}

### POST /follow-up

Request:
{
  "question": "How is AI being applied in classrooms?"
}

Response:
{
  "response": "AI is used for personalized learning, student assessments, and automating administrative tasks..."
}

## Future Improvements

Here are a few enhancements that can be implemented to make AICO AI Agent even more powerful:

- **Web UI Integration**: Add a frontend (e.g., React, Streamlit, or Next.js) to interact with the summarizer visually.
- **Multiple URL Summarization**: Allow batch summarization of multiple URLs in a single request.
- **Named Session Memory**: Persist conversation history using user/session IDs and retain memory in database (e.g, Redis).
- **Streaming Responses**: Enable streaming response from the LLM through WebSockets.
- **Citation Extraction**: Automatically identify and list sources, references, or quotes from the web content.
- **More LLM Support**: Add switchable backends (OpenAI, Claude, Gemini, etc.) using LangChain’s multi-LLM interface.
- **Auto Unit Tests**: Extend the test suite with `pytest` and mocking for all components.


