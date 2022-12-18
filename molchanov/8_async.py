import requests
from time import time


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
#     https://loremflickr.com/cache/resized/65535_48426983596_9d10a9c1ae_320_240_nofilter.jpg
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    to = time()
    url = 'https://loremflickr.com/320/240'

    for i in range(10):
        write_file(get_file(url))
    print(time() - to)


if __name__ == '__main__':
    main()
