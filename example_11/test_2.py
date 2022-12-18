import asyncio


async def async_func():
    print('Запуск ...')
    await asyncio.sleep(1)
    print('... Готово!')


async def main():
    task = asyncio.create_task(async_func())
    await task


if __name__ == '__main__':
    asyncio.run(main())
