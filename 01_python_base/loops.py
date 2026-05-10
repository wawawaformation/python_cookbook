"""Boucles for, enumerate et itération sur un dict."""


def main() -> None:
	frameworks = ["fastapi", "flask", "django"]
	for index, framework in enumerate(frameworks, start=1):
		print(index, framework)

	user = {"name": "David", "role": "admin"}
	for key, value in user.items():
		print(f"{key}={value}")


if __name__ == "__main__":
	main()
