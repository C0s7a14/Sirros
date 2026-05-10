from pydantic import BaseModel


class ProgressResponse(BaseModel):
    id: str
    user_id: str
    training_id: str
    percentage: float

    model_config = {"from_attributes": True}
