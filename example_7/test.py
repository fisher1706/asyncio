import asyncio
from asyncio import sleep


async def make_request():
    print('I take request to BD')
    await sleep(.1)


async def main():
    chunk = 200
    tasks = []
    pended = 0

    for x in range(10000):
        tasks.append(asyncio.create_task(make_request()))
        pended += 1
        if len(tasks) == chunk or pended == 10000:
            await asyncio.gather(*tasks)
            tasks = []
            print(pended)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
