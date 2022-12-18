import requests
import time


stat_time = time.time()


def get_page_data(category, model):
    url = f'https://www.flagman.kiev.ua/{category}-{model}'
    print(f'get_url: {url}')

    response = requests.get(url)
    return response.status_code


def load_site_data():
    categories_list = ['fidernoe-udilishche-flagman-cast-master-feeder-heavy-']
    models = ['420-180g/p180707/', '3.9m-150g/p180706/', '3.3m-140g/p191675/', '3.6m-120g/p180705/']
    for cat in categories_list:
        for model in models:
            code = get_page_data(cat, model)
            print(code)


if __name__ == '__main__':
    load_site_data()

    end_time = time.time() - stat_time
    print(f'\nExecution time: {end_time} seconds')
