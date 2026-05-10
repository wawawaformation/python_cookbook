"""Lancer plusieurs taches async en meme temps."""

import asyncio


async def fetch_data(name: str, delay: int) -> str:
	print(f"{name} commence")
	await asyncio.sleep(delay)
	print(f"{name} fini")
	return f"resultat {name}"


async def main() -> None:
	results = await asyncio.gather(
		fetch_data("A", 1),
		fetch_data("B", 2),
		fetch_data("C", 1),
	)
	print(results)


if __name__ == "__main__":
	asyncio.run(main())