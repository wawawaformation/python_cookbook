"""Route POST simple avec FastAPI."""

from fastapi import FastAPI


app = FastAPI()


@app.post("/users")
def create_user(payload: dict[str, str]) -> dict[str, object]:
	return {
		"message": "Utilisateur cree",
		"user": {
			"id": 1,
			"name": payload["name"],
			"email": payload["email"],
		},
	}