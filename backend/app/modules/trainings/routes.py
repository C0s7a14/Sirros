from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.trainings.schemas import TrainingCreate, TrainingResponse, TrainingUpdate
from app.modules.trainings.service import TrainingService

router = APIRouter()


@router.get("", response_model=list[TrainingResponse])
def list_trainings(db: Session = Depends(get_db)):
    return TrainingService(db).list_all()


@router.post("", response_model=TrainingResponse, status_code=status.HTTP_201_CREATED)
def create_training(body: TrainingCreate, db: Session = Depends(get_db)):
    return TrainingService(db).create(body)


@router.get("/{training_id}", response_model=TrainingResponse)
def get_training(training_id: str, db: Session = Depends(get_db)):
    try:
        return TrainingService(db).get(training_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put("/{training_id}", response_model=TrainingResponse)
def update_training(training_id: str, body: TrainingUpdate, db: Session = Depends(get_db)):
    try:
        return TrainingService(db).update(training_id, body)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{training_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_training(training_id: str, db: Session = Depends(get_db)):
    try:
        TrainingService(db).delete(training_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
