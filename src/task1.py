import time,io
import contextlib
def decorator_1(fun):
    def wrapper(*args):
        wrapper.count+=1
        start=time.perf_counter()
        with contextlib.redirect_stderr(io.StringIO()) as f:
            fun(*args)
        end=time.perf_counter()
        s=f.getvalue()
        print(f"{fun.__name__} call {wrapper.count} executed in {end-start} sec")

    wrapper.count=0

    return wrapper
