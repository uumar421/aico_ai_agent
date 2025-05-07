from langchain_community.document_loaders import WebBaseLoader

class BrowserToolWrapper:
    def run(self, url: str) -> str:
        print("step 2")
        # convert HttpUrl to string
        if not isinstance(url, str):
            url = str(url) 
        loader = WebBaseLoader(url)
        docs = loader.load()
        return "\n".join([doc.page_content for doc in docs])