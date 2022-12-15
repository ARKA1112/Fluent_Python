from collections.abc import Generator
from typing import Union, NamedTuple

class Result(NamedTuple):
    count: int
    average: float

class Sentinel:
    def __repr__(self) -> str:
        return f'<sentinel>'


STOP = Sentinel()
SendType = Union[float, Sentinel]