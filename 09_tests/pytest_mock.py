"""Exemple de mock avec pytest et monkeypatch."""

from api_client import fetch_user_name


class FakeResponse:
	def raise_for_status(self) -> None:
		return None

	def json(self) -> dict[str, str]:
		return {"name": "Bob"}


def test_fetch_user_name_with_monkeypatch(monkeypatch) -> None:
	called = {}

	def fake_get(url: str, timeout: int) -> FakeResponse:
		called["url"] = url
		called["timeout"] = timeout
		return FakeResponse()

	monkeypatch.setattr("api_client.requests.get", fake_get)

	result = fetch_user_name(7)

	assert result == "Bob"
	assert called == {
		"url": "https://api.example.com/users/7",
		"timeout": 10,
	}