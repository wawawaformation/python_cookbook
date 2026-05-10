"""match/case, l'équivalent Python moderne d'un switch."""


def http_status_message(status_code: int) -> str:
	match status_code:
		case 200:
			return "OK"
		case 201:
			return "Created"
		case 400:
			return "Bad Request"
		case 401 | 403:
			return "Unauthorized or Forbidden"
		case 404:
			return "Not Found"
		case _:
			return "Unknown status"


def describe_command(command: dict[str, str]) -> str:
	match command:
		case {"action": "create", "resource": resource}:
			return f"Créer la ressource {resource}"
		case {"action": "delete", "resource": resource}:
			return f"Supprimer la ressource {resource}"
		case _:
			return "Commande non reconnue"


def main() -> None:
	print(http_status_message(200))
	print(http_status_message(403))
	print(http_status_message(418))

	print(describe_command({"action": "create", "resource": "user"}))
	print(describe_command({"action": "delete", "resource": "invoice"}))
	print(describe_command({"action": "update", "resource": "order"}))


if __name__ == "__main__":
	main()