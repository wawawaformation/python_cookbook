"""Exemple de mock avec unittest.mock."""

import unittest
from unittest.mock import Mock, patch

from api_client import fetch_user_name


class TestApiClientWithMock(unittest.TestCase):
	@patch("api_client.requests.get")
	def test_fetch_user_name(self, mock_get: Mock) -> None:
		fake_response = Mock()
		fake_response.json.return_value = {"name": "Alice"}
		fake_response.raise_for_status.return_value = None
		mock_get.return_value = fake_response

		result = fetch_user_name(42)

		self.assertEqual(result, "Alice")
		mock_get.assert_called_once_with("https://api.example.com/users/42", timeout=10)


if __name__ == "__main__":
	unittest.main()