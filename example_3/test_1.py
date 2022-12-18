import asyncio


async def async_func():
    print('Запуск ...')
    await asyncio.sleep(1)
    print('... Готово!')


async def main():
    await async_func()


if __name__ == '__main__':
    asyncio.run(main())
