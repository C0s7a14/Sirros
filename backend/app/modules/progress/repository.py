from sqlalchemy.orm import Session

from app.modules.progress.models import Progress


class ProgressRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get(self, user_id: str, training_id: str) -> Progress | None:
        return (
            self.db.query(Progress)
            .filter(Progress.user_id == user_id, Progress.training_id == training_id)
            .first()
        )

    def upsert(self, user_id: str, training_id: str, percentage: float) -> Progress:
        progress = self.get(user_id, training_id)
        if progress:
            progress.percentage = percentage
        else:
            progress = Progress(user_id=user_id, training_id=training_id, percentage=percentage)
            self.db.add(progress)
        self.db.commit()
        self.db.refresh(progress)
        return progress
