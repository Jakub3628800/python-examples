from functools import wraps
from typing import Callable, Any


def deprecated(f: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(f)
    def wrap(*args, **kw):
        print(f"function {f.__name__} has been deprecated.")
        result = f(*args, **kw)

        return result

    return wrap


@deprecated
def add(a: int, b: int) -> int:
    return a + b


add(4, 3)
# Output: function add has been deprecated.
