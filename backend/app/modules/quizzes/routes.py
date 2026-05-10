from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.quizzes.schemas import QuizCreate, QuizResponse
from app.modules.quizzes.service import QuizService

router = APIRouter()


@router.get("", response_model=list[QuizResponse])
def list_quizzes(db: Session = Depends(get_db)):
    return QuizService(db).list_all()


@router.post("", response_model=QuizResponse, status_code=status.HTTP_201_CREATED)
def create_quiz(body: QuizCreate, db: Session = Depends(get_db)):
    return QuizService(db).create(body)


@router.get("/{quiz_id}", response_model=QuizResponse)
def get_quiz(quiz_id: str, db: Session = Depends(get_db)):
    try:
        return QuizService(db).get(quiz_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
