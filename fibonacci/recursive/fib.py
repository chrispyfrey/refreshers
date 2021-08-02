def fib(n):
    def f(x1, x2, n):
        if x1 + x2 < n:
            print(x1 + x2)
            f(x2, x1 + x2, n)
    print(1)
    print(1)
    f(1, 1, n)

fib(1000)
