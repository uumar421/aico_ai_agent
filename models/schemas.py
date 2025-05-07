from pydantic import BaseModel, HttpUrl


class SummarizeRequest(BaseModel):
    url: HttpUrl


class SummarizeResponse(BaseModel):
    summary: str
    main_topic: str

class FollowUpRequest(BaseModel):
    question: str

class FollowUpResponse(BaseModel):
    answer: str