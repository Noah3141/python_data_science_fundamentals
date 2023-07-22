# We need to make a customized iterator, lazily computed:

def fibonacci_iter():
    one = 1
    two = 1
    yield one
    yield two
    for i in range(50):
        current = one + two
        yield current
        one = two
        two = current
    pass


fib_values = fibonacci_iter()

print(next(fib_values))
print(next(fib_values))
print(next(fib_values))
print(next(fib_values))
print(next(fib_values))
print(next(fib_values))

print("As we start a loop, the iterator begins from current value: ")
for value in fib_values:
    print(value)
