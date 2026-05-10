"""Afficher proprement des données imbriquées."""

from pprint import pprint


def main() -> None:
	payload = {
		"user": {"name": "David", "skills": ["php", "python", "docker"]},
		"meta": {"page": 1, "total": 3},
	}
	pprint(payload, sort_dicts=False)


if __name__ == "__main__":
	main()
