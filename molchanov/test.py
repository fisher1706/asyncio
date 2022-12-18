from inspect import getgeneratorstate


def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received:', message)


def average():
    count = 0
    sum = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
        else:
            count += 1
            print('count = ', count)

            sum += x
            print('sum = ', sum)

            average = round(sum / count, 2)
            print('average = ', average)


# def subgen():
#     for i in 'oleg':
#         yield i


def delegator(g):
    for i in g:
        yield i


if __name__ == '__main__':
    g = subgen()
    y = getgeneratorstate(g)
    print(y)

    d = g.send(None)
    # d = next(g)
    x = getgeneratorstate(g)
    print(x)
    print(d)

    g.send('zapel')
    z = getgeneratorstate(g)
    print(z)

    # a = average()
    # d = a.send(None)
    # print(d)
    #
    # z = a.send(5)
    # print(z)
    #
    # z = a.send(1)
    # print(z)
    #
    # a.throw(StopIteration)

    # sg = subgen()
    # g = delegator(sg)
    #
    # print(next(g))





