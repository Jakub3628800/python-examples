from typing import Generator


def fibonacci_numbers(n) -> Generator[int, None, None]:
    """Return first n fibonacci numbers as a generator."""
    a, b = 0, 1
    for _ in range(0, n):
        yield a
        a, b = b, a + b


for i in fibonacci_numbers(10):
    print(i)
