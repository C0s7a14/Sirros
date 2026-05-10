from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str


class ChunkSource(BaseModel):
    chunk_id: str
    chunk_text: str
    chunk_index: int


class AskResponse(BaseModel):
    answer: str
    sources: list[ChunkSource]
