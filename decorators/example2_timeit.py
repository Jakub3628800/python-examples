from functools import wraps
from typing import Callable, Any
import time


def time_it(f: Callable[[Any], Any]) -> Callable[[Any], Any]:
    @wraps(f)
    def wrap(*args, **kw):
        time_start = time.time()
        result = f(*args, **kw)
        time_end = time.time()

        print(f"function call took: {time_end - time_start} seconds")
        return result

    return wrap


@time_it
def sleep_for(seconds: int) -> None:
    time.sleep(seconds)


sleep_for(1)
sleep_for(3)
sleep_for(5)

# Output:
# function call took: 1.0010316371917725 seconds
# function call took: 3.00309419631958 seconds
# function call took: 5.005037546157837 seconds
