def fib(n):
    x1, x2, x3 = 1, 1, 0
    print(x1)
    print(x2)
    
    while x1 + x2 < n:
        print(x1 + x2)
        x3 = x2
        x2 += x1
        x1 = x3

fib(1000)
