def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def custom_range(start, end, step=1):
    while start < end:
        yield start
        start += step


if __name__ == "__main__":
    print("Fibonacci:")
    for num in fibonacci(50):
        print(num, end=" ")

    print("\n\nCustom Range:")
    for num in custom_range(1, 10, 2):
        print(num, end=" ")
