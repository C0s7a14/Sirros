from sqlalchemy.orm import Session

from app.modules.trainings.models import Training


class TrainingRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Training]:
        return self.db.query(Training).all()

    def get_by_id(self, training_id: str) -> Training | None:
        return self.db.query(Training).filter(Training.id == training_id).first()

    def create(self, title: str, description: str) -> Training:
        training = Training(title=title, description=description)
        self.db.add(training)
        self.db.commit()
        self.db.refresh(training)
        return training

    def update(self, training: Training, title: str | None, description: str | None) -> Training:
        if title is not None:
            training.title = title
        if description is not None:
            training.description = description
        self.db.commit()
        self.db.refresh(training)
        return training

    def delete(self, training: Training) -> None:
        self.db.delete(training)
        self.db.commit()
