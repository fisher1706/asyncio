import asyncio


async def file_reply():
    await asyncio.sleep(4)
    return 'file returned'


async def data_reply():
    await asyncio.sleep(2)
    return {'data', 100}


async def task1():
    print('Waiting for file ...')
    f = await file_reply()
    print('f =', f)


async def task2():
    print('Waiting for data ...')
    x = await data_reply()
    print('x =', x)


async def main():
    x = asyncio.create_task(task1())
    y = asyncio.create_task(task2())

    await x
    await y


if __name__ == '__main__':
    asyncio.run(main())

