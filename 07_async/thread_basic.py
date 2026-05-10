"""Thread simple."""

from threading import Thread
from time import sleep


def worker(name: str) -> None:
	print(f"{name} commence")
	sleep(1)
	print(f"{name} fini")


def main() -> None:
	thread = Thread(target=worker, args=("thread-1",))
	thread.start()
	thread.join()
	print("Programme termine")


if __name__ == "__main__":
	main()