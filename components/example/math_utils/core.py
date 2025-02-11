from .helpers import calculate_fib

def fib(index: int) -> None|int:
    if index is None:
        return None
    if index < 0:
        return None

    return calculate_fib(index)
