def range(start, stop):
    current = start
    while current < stop:
        reset = yield current
        if reset is not None:
            current = reset - 1
        current += 1


def two_ranges(start, stop):
    yield from range(start, stop)


if __name__ == '__main__':
    t = two_ranges(0, 3)

    print(next(t))
    print(next(t))
