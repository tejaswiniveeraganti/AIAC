
from math import isqrt
def classify_number(number: int) -> str:
	"""Return ``prime``, ``composite``, or ``neither``.

	Values below 2 are neither prime nor composite.
	"""
	if isinstance(number, bool) or not isinstance(number, int):
		raise TypeError("an integer is required")
	if number < 2:
		return "neither"
	if number == 2:
		return "prime"
	if number % 2 == 0:
		return "composite"

	# Testing through sqrt(number) is sufficient to find any factor.
	for divisor in range(3, isqrt(number) + 1, 2):
		if number % divisor == 0:
			return "composite"
	return "prime"


def read_and_classify(text: str) -> str:
	"""Validate user text and classify it, returning a user-friendly result."""
	try:
		number = int(text.strip())
	except (ValueError, TypeError):
		return "invalid input"
	return classify_number(number)


def run_tests() -> None:
	"""Exercise boundary, prime, composite, negative, and invalid inputs."""
	for value in (0, 1, 2, 17, 25, -7, "abc", "2.5"):
		print(f"{value!r} -> {read_and_classify(value)}")


if __name__ == "__main__":
	raw_value = input("Enter an integer (or 'test'): ")
	if raw_value.strip().lower() == "test":
		run_tests()
	else:
		print(read_and_classify(raw_value))




