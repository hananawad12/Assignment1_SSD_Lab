from math import sqrt
from datetime import datetime
from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4

############################################################################
try:
    n=int(input("""Enter the task number to execute it ( 1==>task1
                                      2==>task2
                                      3==>task3
                                      4==>task4)
                                      (1,2,3,4) : """))
except:
    print("Enter the integer number from 1 to 4 only!!!")
    exit()
############################################################################
    
#Quadratic Equation
"""@decorator_1
def quadfun(a,b,c):
    f=b*b-4*a*c
    sq=sqrt(abs(f))

    if f>0:
        print((-b+sq)/(2*a))
        print((-b-sq)/(2*a))
    elif f==0:
        print(-b/(2*a))
    else:
        print(-b/(2*a),"+i",sq)
        print(-b/(2*a),"-i",sq)


quadfun(1,5,6)"""
############################################################################
#Quadratic Equation using lambda function
@decorator_1
def quadf2(a,b,c):
    return lambda a, b, c: ((-b + sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - sqrt((b * b) - (4 * a * c))) / (2 * a))

#res=quadf2(1,5,6)
#print(res(1,5,6))

"""
quadfun2=lambda a, b, c: ((-b + sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - sqrt((b * b) - (4 * a * c))) / (2 * a))
res=quadfun2(1,5,6)
print(res)
"""

############################################################################
#pascal triangle
@decorator_1
def pascal(n):
    top=[1]
    app_val=[0]
    for _ in range(n):
        #print(top)
        top=[l+r for l,r in zip(top+app_val,app_val+top)]
############################################################################
@decorator_2
def fact(n):
    """this function to calculate the factorial
    e.g. n=4-->4!=4*3*2*1
    so the function return if n=4 =>24"""
    res=1
    while n>=1:
        res*=n
        n-=1
    return res
############################################################################
def fun1():
    for i in range(0,50):
        pass

def fun2():
    for i in range(0,100):
        pass
    
def fun3(n):
    for i in range(0,n+1):
        pass


def fun4(n):
    for i in range(0,n+1):
        pass
   
############################################################################
@decorator_4
def func(a,b):
    return a+b

    
############################################################################
#Run task 1
if n==1 and __name__=="__main__":
    pascal(10)
    quadf2(1,5,6)
    pascal(10)
    pascal(10)
    quadf2(1,5,6)
    pascal(10)
############################################################################
#Run task 2
if n==2 and __name__=="__main__":
    fact(4)

############################################################################
#Run task 3
if n==3 and __name__=="__main__":
    fun1=decorator_3(fun1)
    fun2=decorator_3(fun2)
    fun3=decorator_3(fun3)
    fun4=decorator_3(fun4)
    
    fun1()
    fun2()
    fun3(150)
    fun4(200)

    print("Function  |   Rank   |   Time Elapsed\n")
    with open("trial2.txt",'r') as f:
        data=f.readlines()

    res={}
    for item in data:
        item=list(item.strip('()\n').split(','))
        res[item[0].strip("'")]=float(item[1])
    
    res=dict(sorted(res.items(), key=lambda item: item[1]))
    print("Function  |     Rank   |   Time Elapsed\n")
    j=1
    for k,v in res.items():
        print(k,"\t\t",j,"\t",v,"s")
        j+=1     

   
############################################################################
#Run task 4
if n==4 and __name__=="__main__":
    try:
        func(1,2)
    except Exception as e:
        print("Error:",e,"=>see the log file")
        with open("log.txt","a") as f:
            f.write("Error: "+str(e)+"\t\t")
            f.write("Time: "+str(datetime.now())+"\n")
        
        
############################################################################

