from unittest.mock import MagicMock, patch

import pytest

from app.modules.rag.service import RagService
from app.modules.pdf_processing.models import TrainingChunk


def _make_chunk(index: int) -> TrainingChunk:
    chunk = TrainingChunk()
    chunk.id = f"chunk-{index}"
    chunk.chunk_text = f"Texto do chunk {index}"
    chunk.chunk_index = index
    chunk.embedding = [0.1] * 384
    return chunk


@patch("app.modules.rag.service.ollama.chat")
@patch("app.modules.rag.service.embed")
def test_ask_returns_answer(mock_embed, mock_chat):
    mock_embed.return_value = [0.1] * 384

    mock_message = MagicMock()
    mock_message.content = "Resposta gerada pelo modelo."
    mock_chat.return_value = MagicMock(message=mock_message)

    db = MagicMock()
    service = RagService(db)
    service.repo = MagicMock()
    service.repo.search_similar_chunks.return_value = [_make_chunk(0), _make_chunk(1)]

    result = service.ask("training-123", "O que é X?")

    assert result.answer == "Resposta gerada pelo modelo."
    assert len(result.sources) == 2


@patch("app.modules.rag.service.embed")
def test_ask_sem_chunks_retorna_mensagem(mock_embed):
    mock_embed.return_value = [0.1] * 384

    db = MagicMock()
    service = RagService(db)
    service.repo = MagicMock()
    service.repo.search_similar_chunks.return_value = []

    result = service.ask("training-123", "O que é X?")

    assert "Nenhum conteúdo encontrado" in result.answer
    assert result.sources == []
