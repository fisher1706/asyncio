import asyncio
import time

from aiohttp import ClientSession


async def fetch_url_data(session, url):
    try:
        async with session.get(url, timeout=60) as response:
            resp = await response.read()
    except Exception as e:
        print(e)
    else:
        return resp
    return


async def fetch_async(r):
    url = "https://www.uefa.com/uefaeuro-2020/"
    tasks = []
    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch_url_data(session, url))
            tasks.append(task)
        resp = await asyncio.gather(*tasks)
    return resp


if __name__ == '__main__':
    for ntimes in [1, 10, 50, 100, 500]:
        start_time = time.time()
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(fetch_async(ntimes))
        loop.run_until_complete(future)
        responses = future.result()
        print(f'Получено {ntimes} результатов запроса за {time.time() - start_time} секунд')
