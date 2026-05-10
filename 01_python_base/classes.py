"""Classes simples et dataclasses."""

from dataclasses import dataclass


@dataclass
class User:
	name: str
	email: str
	is_admin: bool = False

	def label(self) -> str:
		role = "admin" if self.is_admin else "user"
		return f"{self.name} <{self.email}> ({role})"


def main() -> None:
	user = User(name="David", email="david@example.com", is_admin=True)
	print(user)
	print(user.label())


if __name__ == "__main__":
	main()
