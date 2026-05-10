from sqlalchemy.orm import Session

from app.modules.progress.repository import ProgressRepository
from app.modules.progress.schemas import ProgressResponse


class ProgressService:
    def __init__(self, db: Session) -> None:
        self.repo = ProgressRepository(db)

    def get(self, user_id: str, training_id: str) -> ProgressResponse:
        progress = self.repo.get(user_id, training_id)
        if not progress:
            raise ValueError("Progresso não encontrado")
        return ProgressResponse.model_validate(progress)
