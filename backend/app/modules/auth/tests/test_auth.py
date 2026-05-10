from unittest.mock import MagicMock, patch

import pytest

from app.modules.auth.service import AuthService
from app.modules.auth.schemas import TokenResponse


def _make_service():
    db = MagicMock()
    return AuthService(db)


def test_login_invalid_credentials_raises():
    service = _make_service()
    service.repo.get_by_email = MagicMock(return_value=None)

    with pytest.raises(ValueError, match="Credenciais inválidas"):
        service.login("user@test.com", "wrongpass")


def test_login_wrong_password_raises():
    service = _make_service()
    fake_user = MagicMock()
    fake_user.password_hash = "hashed"
    service.repo.get_by_email = MagicMock(return_value=fake_user)

    with patch("app.modules.auth.service.pwd_context.verify", return_value=False):
        with pytest.raises(ValueError, match="Credenciais inválidas"):
            service.login("user@test.com", "wrongpass")


def test_login_success_returns_tokens():
    service = _make_service()
    fake_user = MagicMock()
    fake_user.id = "user-uuid"
    fake_user.password_hash = "hashed"
    service.repo.get_by_email = MagicMock(return_value=fake_user)

    with patch("app.modules.auth.service.pwd_context.verify", return_value=True):
        result = service.login("user@test.com", "correctpass")

    assert isinstance(result, TokenResponse)
    assert result.access_token
    assert result.refresh_token


def test_refresh_invalid_token_raises():
    service = _make_service()

    with pytest.raises(ValueError, match="Refresh token inválido"):
        service.refresh("token-invalido")


def test_refresh_valid_token_returns_tokens():
    service = _make_service()
    result = service._issue_tokens("user-uuid")
    refreshed = service.refresh(result.refresh_token)

    assert isinstance(refreshed, TokenResponse)
    assert refreshed.access_token
