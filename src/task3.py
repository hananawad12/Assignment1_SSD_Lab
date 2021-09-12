import time,io
import contextlib
import inspect


class decorator_3:
    def __init__(self,fun):
        self.fun=fun
        self.res={}
        
    def __call__(self,*args):
        #lst=inspect.getmembers(self.fun)
        for item in lst:
            if item[0]=="__name__":
                name=item[1]       
        start=time.perf_counter()
        with contextlib.redirect_stderr(io.StringIO()) as f:
            self.fun(*args)
        end=time.perf_counter()
        s=f.getvalue()
        self.res[name]=end-start
        for item in self.res.items():
            with open('trial2.txt','a')as f:
                f.write(str(item)+"\n")
            
        
        
        
        
