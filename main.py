from fastapi import FastAPI, HTTPException
from models.schemas import SummarizeRequest, SummarizeResponse, FollowUpRequest, FollowUpResponse
from services.summarize_service import SummarizeService


app = FastAPI()
summarizer = SummarizeService()


@app.post("/summarize", response_model=SummarizeResponse)
async def summarize_url(request: SummarizeRequest) -> SummarizeResponse:
    try:
        return await summarizer.summarize(request.url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/follow-up", response_model=FollowUpResponse)
async def follow_up(request: FollowUpRequest) -> FollowUpResponse:
    try:
        answer = await summarizer.answer_follow_up(request.question)
        return FollowUpResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))