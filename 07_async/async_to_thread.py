"""Lancer du code bloquant depuis asyncio."""

import asyncio
from time import sleep


def blocking_task() -> str:
	print("Tache bloquante commence")
	sleep(1)
	print("Tache bloquante finie")
	return "ok"


async def main() -> None:
	result = await asyncio.to_thread(blocking_task)
	print(result)


if __name__ == "__main__":
	asyncio.run(main())