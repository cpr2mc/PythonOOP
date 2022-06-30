from time import time


import time

class Container:
    
    def get_current_time():
        return time.strftime('%H:%M:%S', time.localtime())

    get_current_time = staticmethod(get_current_time) # this is the "standard way" of declaring a method vs a decorator @
    
t1 = Container

print(t1.get_current_time())