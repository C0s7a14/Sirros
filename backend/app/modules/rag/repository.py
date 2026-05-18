import math

from sqlalchemy.orm import Session

from app.modules.pdf_processing.models import TrainingChunk, TrainingDocument


def _cosine_distance(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 1.0
    return 1.0 - dot / (norm_a * norm_b)


class RagRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def search_similar_chunks(
        self, training_id: str, embedding: list[float], limit: int = 5
    ) -> list[TrainingChunk]:
        try:
            return (
                self.db.query(TrainingChunk)
                .join(TrainingDocument, TrainingChunk.document_id == TrainingDocument.id)
                .filter(TrainingDocument.training_id == training_id)
                .filter(TrainingChunk.embedding.isnot(None))
                .order_by(TrainingChunk.embedding.cosine_distance(embedding))
                .limit(limit)
                .all()
            )
        except Exception:
            return self._fallback_search(training_id, embedding, limit)

    def _fallback_search(
        self, training_id: str, embedding: list[float], limit: int
    ) -> list[TrainingChunk]:
        chunks = (
            self.db.query(TrainingChunk)
            .join(TrainingDocument, TrainingChunk.document_id == TrainingDocument.id)
            .filter(TrainingDocument.training_id == training_id)
            .filter(TrainingChunk.embedding.isnot(None))
            .all()
        )
        if not chunks or not embedding:
            return chunks[:limit]
        ranked = sorted(chunks, key=lambda c: _cosine_distance(c.embedding, embedding))
        return ranked[:limit]
