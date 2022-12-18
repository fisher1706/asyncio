import asyncio


async def send_email():
    print('Hello')
    await asyncio.sleep(2)
    print('Awake now')


if __name__ == '__main__':
    print(asyncio.iscoroutinefunction(send_email))
    asyncio.run(send_email())
