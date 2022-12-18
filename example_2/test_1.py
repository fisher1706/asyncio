import asyncio


async def my_sleep():
    print("my sleep start")
    await asyncio.sleep(2)
    print("my sleep end")


async def main():
    print("Sleep now.")
    await my_sleep()
    print("Ok, wake up!")


if __name__ == '__main__':
    asyncio.run(main())
