from sqlalchemy.orm import Session

from app.modules.pdf_processing.models import TrainingChunk, TrainingDocument


class PdfRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_document(self, training_id: str, filename: str) -> TrainingDocument:
        doc = TrainingDocument(training_id=training_id, filename=filename)
        self.db.add(doc)
        self.db.commit()
        self.db.refresh(doc)
        return doc

    def save_chunks(self, document_id: str, chunks: list[tuple[str, list[float]]]) -> None:
        for index, (text, embedding) in enumerate(chunks):
            chunk = TrainingChunk(document_id=document_id, chunk_text=text, chunk_index=index, embedding=embedding)
            self.db.add(chunk)
        self.db.commit()
