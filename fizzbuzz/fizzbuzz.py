def fizz_buzz(n):
    for i in range(1, n+1):
        print(f'{i} ', end='')
        if i % 3 == 0:
            print('fizz', end='')
        if i % 5 == 0:
            print('buzz', end='')
        print('');

fizz_buzz(100)
