"""Petit client HTTP pour illustrer les mocks."""

import requests


def fetch_user_name(user_id: int) -> str:
	response = requests.get(f"https://api.example.com/users/{user_id}", timeout=10)
	response.raise_for_status()
	data = response.json()
	return data["name"]