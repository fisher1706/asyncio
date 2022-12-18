from inspect import getgeneratorstate


def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received: ', message)


if __name__ == '__main__':
    g = subgen()
    # y = getgeneratorstate(g)
    # print(y)

    g.send(None)
    # x = getgeneratorstate(g)
    # print(x)

    g.send('zapel')
    # z = getgeneratorstate(g)
    # print(z)
