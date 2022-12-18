import asyncio
import httpx


async def downloads(query, current_page):
    header = {'Authorization': '563492ad6f91700001000001133f4c3a909346c6b22770988ead48cb'}
    params = {'query': query, "per_page": 1, "page": current_page}
    url = f'https://api.pexels.com/v1/search/'

    async with httpx.AsyncClient() as client:
        r = await client.get(url, headers=header, params=params)
        if r.status_code == 200:
            _r = r.json()
            for item in _r.get('photos'):
                print(item.get('src').get('original'))
        else:
            print(r.status_code)
        print(f'{query} = {current_page}')


async def main():
    query = input("Search? ")
    page_count = int(input("Count page "))

    current_page = 0
    task_list = []

    while current_page < page_count:
        current_page += 1
        task = asyncio.create_task(downloads(query, current_page))
        task_list.append(task)

    await asyncio.gather(*task_list, return_exceptions=True)

    print('done')


if __name__ == '__main__':
    asyncio.run(main())
