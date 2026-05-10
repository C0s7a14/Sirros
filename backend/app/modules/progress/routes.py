from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.progress.schemas import ProgressResponse
from app.modules.progress.service import ProgressService

router = APIRouter()


@router.get("/{training_id}", response_model=ProgressResponse)
def get_progress(training_id: str, db: Session = Depends(get_db)):
    # user_id virá do token JWT numa próxima iteração
    user_id = "placeholder-user-id"
    try:
        return ProgressService(db).get(user_id=user_id, training_id=training_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
