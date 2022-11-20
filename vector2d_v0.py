from array import array
import math

class Vector2d:
    typecode = 'd'
    __match_args__ = ('x', 'y')  
    __slots__ = ('__x', '__y')

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y))
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __hash__(self) -> int:
        return hash((self.__x, self.__y))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    
    def __abs__(self):
        return math.hypot(self.__x, self.__y)
    
    def __eq__(self, o) -> bool:
        return tuple(self) == tuple(o)
    
    def __bool__(self):
        return bool(abs(self))
    @property     #add this method as property otherwise it will be a bound method
    def x(self):
        return self.__x
    
    
    def __complex__(self):
        return complex(self.__x,self.__y)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._components[key])
        index = operator.index(key)
        return self._components[index]



if __name__ == 'main':
    vi = Vector2d(3,4)
    vi