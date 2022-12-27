import itertools
import time
from multiprocessing import Process, Event
from multiprocessing import synchronize
from spinner_thread import slow, spin

#def spin(msg: str, done: synchronize.Event) -> None:
    #from spinner_thread import spin

#def slow():
    #from spinner_thread import slow

def supervisor() -> int:
    done = Event()
    spinner  = Process(target=spin, args=('thinking!',done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

def main():
    result = supervisor()
    print(f'Answer is {result}')

if __name__ == '__main__':
    main()