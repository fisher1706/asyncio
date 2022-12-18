def test_1():
    yield from [x for x in range(20)]


def test_2():
    print('start')

    while True:
        x = yield
        print('recv:', x)


if __name__ == '__main__':
    # for i in test_1():
    #     print(i)

    t = test_2()
    d = next(t)
    print(d)

    r = t.send('ok')
    print(r)

