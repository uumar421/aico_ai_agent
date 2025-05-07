from agents.summarizer_agent import WebSummarizerAgent
from models.schemas import SummarizeResponse
from utils.chat_memory import load_memory, save_memory
import re

class SummarizeService:
    def __init__(self):
        self.agent = WebSummarizerAgent()

    async def summarize(self, url: str) -> SummarizeResponse:
        response = await self.agent.summarize_url(url)

        if isinstance(response, dict) and "text" in response:
            response_text = response["text"]
        else:
            response_text = response

        main_topic = self.extract_main_topic(response_text)
        cleaned_summary = self.remove_main_topic_line(response_text)

        # save summary as first chat history entry
        memory = [{"role": "assistant", "content": cleaned_summary.strip()}]
        save_memory(memory)

        return SummarizeResponse(summary=cleaned_summary.strip(), main_topic=main_topic.strip())

    def extract_main_topic(self, text: str) -> str:
        match = re.search(r"\*\*Main Topic:\s*(.*?)\*\*", text, re.IGNORECASE)
        return match.group(1) if match else "Unknown"

    def remove_main_topic_line(self, text: str) -> str:
        return re.sub(r"\*\*Main Topic:.*?\*\*\n*", "", text, flags=re.IGNORECASE)

    async def answer_follow_up(self, question: str) -> str:

        memory = load_memory()

        chat_history = ""
        for msg in memory:
            role = "User" if msg["role"] == "user" else "Assistant"
            chat_history += f"{role}: {msg['content']}\n"

        response = await self.agent.answer_follow_up(question, chat_history)

        # update memory
        memory.append({"role": "assistant", "content": response})

        save_memory(memory)
        return response["text"]
