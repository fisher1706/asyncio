import asyncio


async def count(counter):
    print(f'+ len counter {len(counter)}')
    while True:
        await asyncio.sleep(1 / 1000)
        counter.append(1)


async def print_every_one_sec(counter):
    while True:
        await asyncio.sleep(1)
        print(f'1 - sec\n'
              f'++ len counter {len(counter)}')


async def print_every_five_sec(counter):
    while True:
        await asyncio.sleep(5)
        print(f'5 - sec\n'
              f'++++ len counter {len(counter)}')


async def print_every_ten_sec(counter):
    while True:
        await asyncio.sleep(10)
        print(f'10 - sec\n'
              f'++++++++ len counter {len(counter)}')


async def main():
    counter = list()

    tasks = [
        count(counter),
        print_every_one_sec(counter),
        print_every_five_sec(counter),
        print_every_ten_sec(counter)
    ]

    await asyncio.gather(*tasks)

asyncio.run(main())
