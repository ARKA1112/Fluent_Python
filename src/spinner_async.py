import asyncio
from spinner_thread import spin

def slow():
    time.sleep(3)
    return 42

def main() -> None:
    result = asyncio.run(supervisor())
    print(f'Anser: {result}')


async def supervisor():
    spinner = asyncio.create_task(spin('thinking!'))
    print(f'spinner object:{spinner}')
    result = await slow()
    spinner.cancel()
    return result

if __name__ == "__main__":
    supervisor()