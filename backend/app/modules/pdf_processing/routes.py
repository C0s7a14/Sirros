from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.pdf_processing.schemas import DocumentResponse
from app.modules.pdf_processing.service import PdfService

router = APIRouter()


@router.post(
    "/trainings/{training_id}/documents",
    response_model=DocumentResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def upload_document(
    training_id: str,
    file: UploadFile,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    if not file.filename or not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Arquivo deve ser um PDF")

    content = file.file.read()
    service = PdfService(db)
    doc = service.upload(training_id=training_id, filename=file.filename, content=content)
    background_tasks.add_task(service.process, doc.id, content)
    return doc
