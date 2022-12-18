import asyncio
import aiohttp
import time


stat_time = time.time()
all_data = []


async def get_page_data(session, category, model):
    url = f'https://www.flagman.kiev.ua/{category}-{model}'
    print(f'get_url: {url}')

    async with session.get(url) as resp:
        # assert resp.status == 200
        resp_text = await resp.text()
        all_data.append(resp_text)
        return resp_text


async def load_site_data():
    categories_list = ['fidernoe-udilishche-flagman-cast-master-feeder-heavy-']
    models = ['420-180g/p180707/', '3.9m-150g/p180706/', '3.3m-140g/p191675/', '3.6m-120g/p180705/']

    async with aiohttp.ClientSession() as session:
        tasks = []
        for cat in categories_list:
            for model in models:
                task = asyncio.create_task(get_page_data(session, cat, model))
                tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(load_site_data())

    end_time = time.time() - stat_time
    print(f'\nExecution time: {end_time} seconds')



