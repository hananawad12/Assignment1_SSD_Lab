import inspect
import time,io
import contextlib

def decorator_2(fun):
    f=fun
    def wrapper(*args):
        wrapper.count+=1
        start=time.perf_counter()
        with contextlib.redirect_stderr(io.StringIO()) as file:
            f(*args)
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
    


        







