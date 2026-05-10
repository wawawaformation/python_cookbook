"""Application FastAPI minimale."""

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
	return {"message": "Hello FastAPI"}


@app.get("/health")
def healthcheck() -> dict[str, str]:
	return {"status": "ok"}