"""Variables et types de base.

Repères rapides pour un développeur PHP :
- dict ~= tableau associatif
- None ~= null
- f-string ~= interpolation de chaîne
"""


def main() -> None:
	user_name = "David"
	age = 38
	is_admin = True
	score = 19.5
	optional_note = None

	user = {
		"name": user_name,
		"age": age,
		"is_admin": is_admin,
		"score": score,
		"note": optional_note,
	}

	print(f"Hello {user['name']}, age={user['age']}, score={user['score']}")
	print(f"Admin? {user['is_admin']}")
	print(f"Missing note -> {user['note']}")

	languages = ["php", "python", "sql"]
	languages.append("bash")
	print(languages)


if __name__ == "__main__":
	main()
