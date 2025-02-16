def calculate_fib(index: int) -> int:
    a = 0
    b = 1
    for _ in range(index):
        c = a + b
        a = b
        b = c
    return a
