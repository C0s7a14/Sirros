from sqlalchemy.orm import Session

from app.modules.quizzes.repository import QuizRepository
from app.modules.quizzes.schemas import QuizCreate, QuizResponse


class QuizService:
    def __init__(self, db: Session) -> None:
        self.repo = QuizRepository(db)

    def list_all(self) -> list[QuizResponse]:
        return [QuizResponse.model_validate(q) for q in self.repo.get_all()]

    def get(self, quiz_id: str) -> QuizResponse:
        quiz = self.repo.get_by_id(quiz_id)
        if not quiz:
            raise ValueError("Quiz não encontrado")
        return QuizResponse.model_validate(quiz)

    def create(self, data: QuizCreate) -> QuizResponse:
        quiz = self.repo.create(training_id=data.training_id, title=data.title)
        return QuizResponse.model_validate(quiz)
