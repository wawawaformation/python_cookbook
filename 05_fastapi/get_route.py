"""Route GET simple avec FastAPI."""

from fastapi import FastAPI


app = FastAPI()


@app.get("/users")
def list_users() -> list[dict[str, object]]:
	return [
		{"id": 1, "name": "Alice"},
		{"id": 2, "name": "Bob"},
	]