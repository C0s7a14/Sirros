from sqlalchemy.orm import Session

from app.modules.trainings.repository import TrainingRepository
from app.modules.trainings.schemas import TrainingCreate, TrainingResponse, TrainingUpdate


class TrainingService:
    def __init__(self, db: Session) -> None:
        self.repo = TrainingRepository(db)

    def list_all(self) -> list[TrainingResponse]:
        return [TrainingResponse.model_validate(t) for t in self.repo.get_all()]

    def get(self, training_id: str) -> TrainingResponse:
        training = self.repo.get_by_id(training_id)
        if not training:
            raise ValueError("Treinamento não encontrado")
        return TrainingResponse.model_validate(training)

    def create(self, data: TrainingCreate) -> TrainingResponse:
        training = self.repo.create(title=data.title, description=data.description)
        return TrainingResponse.model_validate(training)

    def update(self, training_id: str, data: TrainingUpdate) -> TrainingResponse:
        training = self.repo.get_by_id(training_id)
        if not training:
            raise ValueError("Treinamento não encontrado")
        training = self.repo.update(training, data.title, data.description)
        return TrainingResponse.model_validate(training)

    def delete(self, training_id: str) -> None:
        training = self.repo.get_by_id(training_id)
        if not training:
            raise ValueError("Treinamento não encontrado")
        self.repo.delete(training)
