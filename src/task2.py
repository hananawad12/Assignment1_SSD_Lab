import inspect
def decorator_2(fun):
    f=fun
    def wrapper(*args):
        lst=inspect.getmembers(f)
        for item in lst:
            if item[0]=="__name__":
                Name=item[1]
            elif item[0]=="__class__":
                Type=item[1]
            elif item[0]=="__doc__":
                Doc=item[1]
        Source=inspect.getsource(f)
        params=inspect.getargspec(f)   
        Sign=params[0]  
        Args=params[1:]
        print("Name: ",Name)
        print("Type: ",Type)
        print("Sign: ",Sign)
        print("Args: ",Args)
        print("Doc: ",Doc)
        print("Source: ",Source)
        print("Output: ",f(*args)) 
    return wrapper
    


        







