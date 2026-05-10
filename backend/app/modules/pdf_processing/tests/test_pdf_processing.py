from unittest.mock import MagicMock, patch

from app.modules.pdf_processing.service import PdfService, _split_chunks


def test_split_chunks_basic():
    text = "a" * 2500
    chunks = _split_chunks(text, 1000)
    assert len(chunks) == 3
    assert all(len(c) <= 1000 for c in chunks)


def test_split_chunks_ignores_blank():
    # chunk de apenas espaços é descartado
    text = "a" * 1000 + " " * 1000 + "b" * 1000
    chunks = _split_chunks(text, 1000)
    assert len(chunks) == 2


def test_upload_creates_document():
    db = MagicMock()
    service = PdfService(db)
    fake_doc = MagicMock()
    fake_doc.id = "doc-uuid"
    fake_doc.training_id = "training-uuid"
    fake_doc.filename = "arquivo.pdf"
    service.repo.create_document = MagicMock(return_value=fake_doc)

    result = service.upload("training-uuid", "arquivo.pdf", b"pdf-content")

    service.repo.create_document.assert_called_once_with(
        training_id="training-uuid", filename="arquivo.pdf"
    )
    assert result.id == "doc-uuid"


def test_process_saves_chunks():
    db = MagicMock()
    service = PdfService(db)
    service.repo.save_chunks = MagicMock()

    with patch("app.modules.pdf_processing.service.pymupdf4llm.to_markdown", return_value="texto " * 200):
        service.process("doc-uuid", b"%PDF-fake")

    service.repo.save_chunks.assert_called_once()
    args = service.repo.save_chunks.call_args
    assert args[0][0] == "doc-uuid"
    assert len(args[0][1]) > 0
