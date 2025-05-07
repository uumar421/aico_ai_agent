import asyncio
import concurrent.futures
from config import get_summarization_chain, get_follow_up_chain
from tools.browser_tool import BrowserToolWrapper

class WebSummarizerAgent:
    def __init__(self) -> None:
        self.browser_tool = BrowserToolWrapper()
        self.loop = asyncio.get_event_loop()
        self.summary_chain = get_summarization_chain()
        self.follow_up_chain = get_follow_up_chain()

    async def summarize_url(self, url: str) -> str:
        with concurrent.futures.ThreadPoolExecutor() as pool:
            content = await self.loop.run_in_executor(pool, self.browser_tool.run, url)
        return self.summary_chain.invoke({
            "text": content
        })

    async def answer_follow_up(self, question: str, chat_history: str) -> str:
        return self.follow_up_chain.invoke({
            "question": question,
            "chat_history": chat_history
        })
        
