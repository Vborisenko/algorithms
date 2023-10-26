import random
import asyncio
import arrow


async def waiter(name):
    for _ in range(5):
        # time_stamp = random.randint(1, 3) / 4
        time_stamp = 0.5
        await asyncio.sleep(time_stamp)
        print(f'The `{name}` is waiting {time_stamp} seconds')


async def main():
    await asyncio.wait([waiter('foo'), waiter('boo')])


if __name__ == '__main__':
    print(arrow.now())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    print(arrow.now())


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper

@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text

webpage = fetch_webpage('https://google.com')
print(webpage)