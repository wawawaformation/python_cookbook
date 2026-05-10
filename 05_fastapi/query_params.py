"""Query parameters avec FastAPI."""

from fastapi import FastAPI


app = FastAPI()


@app.get("/search")
def search_users(q: str = "", limit: int = 10) -> dict[str, object]:
	return {
		"query": q,
		"limit": limit,
		"results": [
			{"id": 1, "name": "Alice"},
			{"id": 2, "name": "Bob"},
		][:limit],
	}