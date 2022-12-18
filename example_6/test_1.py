import asyncio


async def task1():
    print('Send first Email')
    asyncio.create_task(task2())
    await asyncio.sleep(5)
    print('First Email reply')


async def task2():
    print('Send second Email')
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print('Second Email reply')


async def task3():
    print('Send third Email')
    await asyncio.sleep(1)
    print('Third Email reply')


if __name__ == '__main__':
    asyncio.run(task1())
