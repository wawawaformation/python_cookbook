"""Fonction async simple."""

import asyncio


async def say_hello() -> None:
	print("Debut")
	await asyncio.sleep(1)
	print("Bonjour")


def main() -> None:
	asyncio.run(say_hello())


if __name__ == "__main__":
	main()