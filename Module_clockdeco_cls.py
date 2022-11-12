import time

DEFAULT_FMT = '[{elapsed:0.7f}s] {name} ({args}) -> {result}'

class clock:
    def __init__(self, fmt=DEFAULT_FMT) -> None:
        self.fmt = fmt

    def __call__(self, func):
        def clocked(*args):
            t0 = time.perf_counter()
            result = func(*args)
            elapsed = result - t0
            args = ','.join(repr(arg) for arg in args)
            result_ = repr(result)
            print(self.fmt.format(**locals()))
            return result
        return clocked