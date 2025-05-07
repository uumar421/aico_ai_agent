import os
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment.")

os.environ["GROQ_API_KEY"] = groq_api_key  


def get_llm() -> ChatGroq:
    return ChatGroq(model="llama-3.3-70b-versatile", temperature=0)


def get_memory() -> ConversationBufferWindowMemory:
    return ConversationBufferWindowMemory(k=3, return_messages=True)


def get_summary_prompt() -> PromptTemplate:
    return PromptTemplate(
        input_variables=["text"],
        template=(
            "You are an intelligent and polite AI assistant that can summarize web pages and answer follow-up questions.\n\n"
            "Context:\n"
            "You will be provided a new webpage (under 'text'), summarize its content. "
            "Focus on clarity, insight, and relevance. Highlight the main topic at the start.\n\n"
            "Webpage content:\n{text}\n\n"
            "Your Response:"
        )
    )


def get_question_prompt() -> PromptTemplate:
    return PromptTemplate(
        input_variables=["question", "chat_history"],
        template=(
            "You are an intelligent and polite AI assistant that answers follow-up questions based on prior conversation and webpage summary.\n\n"
            "Conversation History:\n"
            "{chat_history}\n\n"
            "User Question:\n{question}\n\n"
            "Your Response:"
        )
    )


def get_summarization_chain():
    return LLMChain(
        llm = get_llm(),
        prompt = get_summary_prompt(),
        memory = get_memory(),
        verbose = True
    )


def get_follow_up_chain():
    return LLMChain(
        llm = get_llm(),
        prompt = get_question_prompt(),
        verbose = True
    )

