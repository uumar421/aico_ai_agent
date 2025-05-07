import httpx

BASE_URL = "http://localhost:8000"

def test_summarize():
    url = f"{BASE_URL}/summarize"
    payload = {
        "url": "https://en.wikipedia.org/wiki/Standard_score"
    }
    response = httpx.post(url, json=payload)
    print("Summarize Response:")
    print(response.json())

def test_follow_up():
    url = f"{BASE_URL}/follow-up"
    payload = {
        "question": "Can you tell me what the previous summary was about?"
    }
    response = httpx.post(url, json=payload)
    print("\nFollow-Up Response:")
    print(response.json())

if __name__ == "__main__":
    test_summarize()
    input("\nPress Enter to continue with follow-up...\n")
    test_follow_up()