from functools import cache


def add_numbers(a: int, b: int) -> int:
    print(f"summing {a} + {b}")
    return a + b


add_numbers = cache(add_numbers)


add_numbers(5, 7)
add_numbers(5, 7)  # add_numbers won't actually be called here - because result is cached

# Output: summing 5 + 7
