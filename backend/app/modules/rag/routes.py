from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.rag.schemas import AskRequest, AskResponse
from app.modules.rag.service import RagService

router = APIRouter()


@router.post("/trainings/{training_id}/ask", response_model=AskResponse)
def ask(training_id: str, body: AskRequest, db: Session = Depends(get_db)):
    try:
        return RagService(db).ask(training_id, body.question)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
