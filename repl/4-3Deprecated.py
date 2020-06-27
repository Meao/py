"""
Выводит предупреждение DeprecationWarning
"""
import functools
import warnings

def deprecated(cls):
    orig_init = cls.__init__
    
    @functools.wraps(cls.__init__)
    def new_init(self, *args, **kwargs):
        warnings.warn(cls.__name__ + " is deprecated", category=DeprecationWarning)
        orig_init(self, *args, **kwargs)
        
    cls.__init__ = new_init
    return cls 

@deprecated
class Counter:
    def __init__(self, initial=0):
        self.value = initial
        print(initial)
        
        
c = Counter(10)
