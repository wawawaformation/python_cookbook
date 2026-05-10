"""Heritage et composition sur un exemple simple."""


class Notifier:
	def send(self, message: str) -> None:
		print(f"Notification: {message}")


class User:
	def __init__(self, name: str, notifier: Notifier) -> None:
		self.name = name
		self.notifier = notifier

	def welcome(self) -> None:
		self.notifier.send(f"Bienvenue {self.name}")


class Admin(User):
	def __init__(self, name: str, notifier: Notifier, permissions: list[str]) -> None:
		super().__init__(name, notifier)
		self.permissions = permissions

	def welcome(self) -> None:
		super().welcome()
		print(f"Permissions: {', '.join(self.permissions)}")


def main() -> None:
	notifier = Notifier()
	user = User("Alice", notifier)
	admin = Admin("David", notifier, ["users:write", "billing:read"])

	user.welcome()
	admin.welcome()


if __name__ == "__main__":
	main()