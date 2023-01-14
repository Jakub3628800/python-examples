from typing import Generator


def my_range(start: int, end: int) -> Generator[int, None, None]:
    current = start
    while current < end:
        yield current
        current += 1
    return None


for i in my_range(0, 10):
    print(i)
