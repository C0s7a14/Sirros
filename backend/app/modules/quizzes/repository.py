from sqlalchemy.orm import Session

from app.modules.quizzes.models import Quiz


class QuizRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Quiz]:
        return self.db.query(Quiz).all()

    def get_by_id(self, quiz_id: str) -> Quiz | None:
        return self.db.query(Quiz).filter(Quiz.id == quiz_id).first()

    def create(self, training_id: str, title: str) -> Quiz:
        quiz = Quiz(training_id=training_id, title=title)
        self.db.add(quiz)
        self.db.commit()
        self.db.refresh(quiz)
        return quiz
