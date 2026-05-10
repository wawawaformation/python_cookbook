"""Retourner une erreur HTTP explicite."""

from fastapi import FastAPI, HTTPException


app = FastAPI()


FAKE_USERS = {
	1: {"id": 1, "name": "Alice"},
	2: {"id": 2, "name": "Bob"},
}


@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict[str, object]:
	user = FAKE_USERS.get(user_id)
	if user is None:
		raise HTTPException(status_code=404, detail="Utilisateur introuvable")
	return user