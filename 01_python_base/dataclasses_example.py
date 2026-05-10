"""Dataclasses pour représenter des données simplement."""

from dataclasses import asdict, dataclass, field


@dataclass
class User:
	name: str
	email: str
	roles: list[str] = field(default_factory=list)

	def is_admin(self) -> bool:
		return "admin" in self.roles


def main() -> None:
	user = User(name="Alice", email="alice@example.com", roles=["editor", "admin"])

	print(user)
	print(asdict(user))
	print(user.is_admin())


if __name__ == "__main__":
	main()