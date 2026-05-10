from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: str
    training_id: str
    filename: str
    status: str = "processing"

    model_config = {"from_attributes": True}
