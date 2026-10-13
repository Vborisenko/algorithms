import random
import time
from threading import Thread


def random_delay():
    return random.random() * 5


def random_countdown():
    return random.randrange(5)


def launch_rockets(delay, countdown):
    time.sleep(delay)
    for i in reversed(range(countdown)):
        print(f"....{i}")
        time.sleep(1)
    print("Rocket Launched!")


def rockets():
    return [(random_delay(), random_countdown()) for _ in range(10000)]


def run_in_threads():
    threads = [Thread(target=launch_rockets, args=(d, c)) for d, c in rockets()]

    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    run_in_threads()
