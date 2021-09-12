def decorator_4(fun):
    def wrapper(*args):
        fn(*args)   # this is an error (I write fn istead of fun): I put it in log file with atimestamp
        

    return wrapper
