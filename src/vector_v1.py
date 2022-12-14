from array import array
import itertools
import math
from collections import abc
class Vector:
    __match_args__ = ('x','y','z','t')
    def __init__(self,args) -> None:
            self.args = [i for i in args]

    def __repr__(self) -> str:
            return f'{self.__class__.__name__}{self.args}'

    def __len__(self) -> int:
        return len(self.args)

    def __iter__(self):
        return iter(self.args)

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
    
    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self.args,other,fillvalue=0.0)
            return Vector(a+b for a,b in pairs)
        except TypeError:
            return NotImplemented
        

    def __radd(self, other):
        return self.args + other

    def __mul__(self, other):
        return Vector(n*other for n in self.args)

    def __rmul(self, other):
        return [i*other for i in self.args]


    def __matmul__(self, other):
        if (isinstance(other, abc.Sized) and
            isinstance(other, abc.Iterable)):
            if len(self) == len(other):
                return sum(a*b for a, b in zip(self,other))
            else:
                raise ValueError('@ requires vectors of equal length')
        else:
            return NotImplemented

    def __rmatmul__(self, other):
        return self @ other


    #def __eq__(self, __o: object) -> bool:
     #   return (len(self) == len(__o) and
      #          all(a==b for a,b in zip(self,__o)))

      #improved __eq__

    def __eq__(self, __o: object) -> bool:
        if isinstance(self, Vector):
            return (len(self) == len(__o) and all(a==b for a, b in zip(self, __o)))


    def __ne__(self, __o: object) -> bool:
        eq_result = self==__o
        if eq_result is NotImplemented:
            return NotImplemented
        else:
            return not eq_result