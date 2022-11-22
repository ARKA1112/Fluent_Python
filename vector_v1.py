from array import array
import math

class Vector:
    __match_args__ = ('x','y','z','t')
    def __init__(self,*args) -> None:
            self.args = args

    def __repr__(self) -> str:
            return f'{self.__class__.__name__}{self.args}'

    def __len__(self) -> int:
        return len(self.args)

    def __getitem__(self, index):
        for i in range(len(self.args)):
            return self.args[index]

    def __getattr__(self, name):
        cls = type(self)
        try:
            pos = cls.__match_args__.index(name)
        except ValueError:
            pos = -1
        if 0<=pos< len(self._components):
            return self._components[pos]
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        raise AttributeError(msg)

    def __setattr__(self, __name: str, __value: any) -> None:
        if __name in self.__match_args__:
            if self.__name:
                raise AttributeError("already there")
            else:
                self.__name = __value
        super().__setattr__(__name, __value)

    def __format__(self, fmt_spec='') -> str:
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)],
                                     self.angles())  
            outer_fmt = '<{}>'  
        else:
            coords = self
            outer_fmt = '({})'  
        components = (format(c, fmt_spec) for c in coords)  
        return outer_fmt.format(', '.join(components))