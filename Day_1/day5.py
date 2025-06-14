"""def outer(x):
    x=x
    def inner():
        print(x)
    return inner
a=outer("hello")
print(a())
print(type(a))
print(type(outer))

def counter():
    count=0
    def counte():
        nonlocal count
        count+=1
        return count
    return counte
c1=counter()
c2=counter()
print(c1())
print(c1())
print(c1())
print(c2())
print(c2())


def decor(add):
    def inner():
        result=add()
        num3=float(input("Enter number 3:"))
        result =result+num3
        return result
    return inner
@decor
def add():
    num1=float(input("Enter number 1:"))
    num2=float(input("Enter number 2:"))
    result=num1+num2
    return result
#a=decor(add)
print("Addition:",add())


def decor(fun):
    def inner():
        print("___________________________")
        fun()
        print("***************")
    return inner
def msg():
    print("python programming")
msg=decor(msg)
msg()


from datetime import datetime
def night(fun):
    def inner():
        if 7<=datetime.now<22:
            fun()
        else:
            print("sorry! unable to play music")
        return



def twice(fun):
    def wrapper(*args,**kwargs):
        fun(*args,**kwargs)
        fun(*args, **kwargs)
    return wrapper
@twice
def msg(name):
    print(f"hello {name}")
msg("mohit ")


def decor1(fun):
    def inner():
        x=fun()
        return x*x
    return inner
def decor(fun):
    def inner():
        x=fun()
        return 2*x
    return inner
@decor1
@decor
def num():
    return 10
print(num())

def generate():
    for num in range(1,11):
        yield num
n=generate()
print(type(n))
for number in n:
    print(number)
from operator import truediv


def prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def primes(start,end):
    for num in range(start,end+1):
        if prime(num):
            yield num
p=primes(3,50)
for prime in p:
    print(prime,end=',')"""


def my_gen(x):
    while(x>0):
        if x%2==0:
            yield 'even'
        else:
            yield 'odd'
        x-=1
for i in my_gen(7):
    print(i)
