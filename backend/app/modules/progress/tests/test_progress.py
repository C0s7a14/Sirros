from unittest.mock import MagicMock

import pytest

from app.modules.progress.service import ProgressService


def _make_service():
    return ProgressService(MagicMock())


def test_get_not_found_raises():
    service = _make_service()
    service.repo.get = MagicMock(return_value=None)

    with pytest.raises(ValueError, match="Progresso não encontrado"):
        service.get("user-id", "training-id")


def test_get_returns_progress():
    service = _make_service()
    fake = MagicMock()
    fake.id = "prog-uuid"
    fake.user_id = "user-uuid"
    fake.training_id = "training-uuid"
    fake.percentage = 50.0
    service.repo.get = MagicMock(return_value=fake)

    result = service.get("user-uuid", "training-uuid")
    assert result.percentage == 50.0
