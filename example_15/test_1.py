def generator(a, b):
    while True:
        yield a * b
        print(f'a = {a}')
        a += 1


if __name__ == '__main__':
    g = generator(2, 2)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
