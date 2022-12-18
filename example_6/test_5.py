import asyncio


async def fetch_data():
    print('Fetching data ...')
    await asyncio.sleep(5)
    print('Data returned ...')
    return {'data': 100}


async def task2():
    for i in range(10):
        print(i)
        await asyncio.sleep(2)


async def main():
    x = asyncio.create_task(fetch_data())
    y = asyncio.create_task(task2())

    data = await x
    print(data)
    await y


if __name__ == '__main__':
    asyncio.run(main(), debug=True)

