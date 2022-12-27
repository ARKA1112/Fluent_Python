import asyncio
import itertools
import time
from spinner_async import spin

async def supervisor():
    spinner = asyncio.create_task(spin('thinking!'))
    print(f'spinner object: {spinner}')
    result = await slow()
    return result

async def slow() -> int:
    time.sleep(3)
    return 42

async def slow() -> int:
    time.sleep(3)
    return 42


if __name__ == "__main__":
    spin()