def range_1(start, stop):
    current = start
    while current < stop:
        yield current
        current += 1


def range_2(start, stop):
    current = start
    while current < stop:
        reset = yield current
        if reset is not None:
            current = reset - 1
        current += 1


if __name__ == '__main__':
    # x = range_1(1, 5)
    # print(x)
    #
    # for i in x:
    #     print(i)

    f = range_2(1, 5)
    print(next(f))
    # print(next(f))
    print(f.send(0))
