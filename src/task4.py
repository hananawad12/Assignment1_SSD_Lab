import inspect
import time,io
import contextlib


"""I wrote the try and except at the start of calling of decorated function
(in main.py) to catch any error in the decorator_4
"""
def decorator_4(fun):
    f=fun
    def wrapper(*args):
        wrapper.count+=1
        start=time.perf_counter()
        with contextlib.redirect_stderr(io.StringIO()) as file:
            #f(*args)
            ff(*args)  #the name of function is wrong so it will send the error to log file
        end=time.perf_counter()
        s=file.getvalue()
        print(f"{fun.__name__} call {wrapper.count} executed in {end-start} sec")

        #lst=inspect.getmembers(f)
        Source=inspect.getsource(f)
        #params=inspect.getargspec(f)   
        #Sign=params[0]  
        #Args=params[1:]
        print("Name: ",f.__name__)
        print("Type: ",f.__class__)
        print("Sign: ",Sign)
        print("Args: ","positional ",f.__defaults__)
        print("\tkey=worded  ",f.__kwdefaults__)

        print("Doc: ",f.__doc__)
        print("Source: ",Source)
        print("Output: ",f(*args))

    wrapper.count=0

    return wrapper
