from sqlalchemy.orm import Session

from app.modules.pdf_processing.models import TrainingChunk, TrainingDocument


class RagRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def search_similar_chunks(
        self, training_id: str, embedding: list[float], limit: int = 5
    ) -> list[TrainingChunk]:
        return (
            self.db.query(TrainingChunk)
            .join(TrainingDocument, TrainingChunk.document_id == TrainingDocument.id)
            .filter(TrainingDocument.training_id == training_id)
            .filter(TrainingChunk.embedding.isnot(None))
            .order_by(TrainingChunk.embedding.cosine_distance(embedding))
            .limit(limit)
            .all()
        )
