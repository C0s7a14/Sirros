from pydantic import BaseModel


class QuizCreate(BaseModel):
    training_id: str
    title: str


class QuizResponse(BaseModel):
    id: str
    training_id: str
    title: str

    model_config = {"from_attributes": True}
