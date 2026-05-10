from pydantic import BaseModel


class TrainingCreate(BaseModel):
    title: str
    description: str = ""


class TrainingUpdate(BaseModel):
    title: str | None = None
    description: str | None = None


class TrainingResponse(BaseModel):
    id: str
    title: str
    description: str

    model_config = {"from_attributes": True}
