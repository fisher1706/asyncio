import time
import random
import heapq
import types
from enum import Enum, auto

def random_delay():
    return random.random() * 5

def random_countdown():
    return random.randrange(5)

@types.coroutine
def sleep(delay):
    yield Op.WAIT, delay

async def launch_rocket(delay, coundown):
    # block WAITING
    await sleep(delay)
    # block COUNTING
    for i in reversed(range(coundown)):
        print(f"{i + 1}...")
        await sleep(1)
    # block LAUNCHING
    print("Rocket launched!")

class Op(Enum):
    WAIT = auto()
    STOP = auto()

def now():
    return time.time()

def run_fsm(rockets):
    start = now()
    work = [(start, i, launch_rocket(d, c))
            for i, (d, c) in enumerate(rockets)]

    while work:
        step_at, id, launch = heapq.heappop(work)
        wait = step_at - now()
        if wait > 0:
            time.sleep(wait)

        try:
            op, arg = launch.send(None)
        except StopIteration:
            continue

        if op is Op.WAIT:
            step_at = now() + arg
            heapq.heappush(work, (step_at, id, launch))
        else:
            assert False, op

def rockets():
    N = 10_000
    return [
        (random_delay(), random_countdown())
         for _ in range(N)
    ]


if __name__ == '__main__':
    run_fsm(rockets())

