"""Validation d'entree avec Pydantic et FastAPI."""

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app = FastAPI()


class UserCreate(BaseModel):
	name: str
	email: EmailStr
	age: int


@app.post("/users")
def create_user(user: UserCreate) -> dict[str, object]:
	return {
		"message": "Utilisateur valide",
		"user": user.model_dump(),
	}