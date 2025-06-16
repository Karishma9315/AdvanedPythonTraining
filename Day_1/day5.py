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
    print(prime,end=',')"


def my_gen(x):
    while(x>0):
        if x%2==0:
            yield 'even'
        else:
            yield 'odd'
        x-=1
for i in my_gen(7):
    print(i)

#immutable tuple
cor=[10,23]
new_cor=cor+[30,]
print(cor)
print(new_cor)

from time import sleep
student=["Atul","manu","naman","divya"]
def read():
    sleep(3)
    print("reading done.")
    data=student
    while True:
        name=(yield)
        if name in data:
            print("found")
        else:
            print("not found")
search=read()
print("reading all data...")
next(search)
next(search)
next(search)
next(search)
search.send("arvind")
search.send("manu")

def print_name(prefix):
    print("searching prefix:{}".format(prefix))
    while True:
        name=(yield)
        if prefix in name:
            print(name)
coro=print_name("dear")
coro.__next__()
coro.send("atul")
coro.send("dear atul")

def print_name(prefix):
    print("searching prefix:{}".format(prefix))
    try:
        while True:
            name=(yield)
            if prefix in name:
                print(name)
    except:
        print("closing coroutine!")
coro=print_name("dear")
coro.__next__()
coro.send("atul")
coro.send("dear atul")
coro.close()

import sys
l=[1,34,56,78,59,87]
for i in l:
    print(i)
print("for list:",sys.getsizeof(l))
obj=range(5)
for i in obj:
    print(i)
print("for range:",sys.getsizeof(obj))

l=[12,34,5,6,67,89,60] #iterable
iter_obj=iter(l)  #iterator:it is an object
print(iter_obj)
print(type(iter_obj))
print(next(iter_obj))
for i in iter_obj:
    print(i)

l=[5,6,8,9]
iter_obj=iter(l)
print(type(iter_obj))
print("id of iter_obj:",id(iter_obj))
iter_obj1=iter(iter_obj)
print(type(iter_obj1))
print("id of iter_obj1",id(iter_obj1))

l=[45,67,70,10,28]
def myloop(iterable):
    iterator=iter(iterable)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
       pass
myloop(l)

class power:
    def __next__(self,max):
        self.limit=max
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.limit:
            result = self.current
            self.current=self.currenrt*2
            return result
        else:
            raise StopIteration
n=int(input("Enter the limit:"))
iter_obj=power(n)
print(next(iter_obj))
#for num in iter_obj:
 #   print(num)
print("Memory of two ")

class myrange: #iterable class
    def __init__(self,start=0,stop=None,step=1):
        self.start=start
        self.stop=stop
        self.step=step
    def __iter__(self):
        return myrange_iterator(self)
class myrange_iterator: #iterator class
    def __iter__(self,iterable_obj):
        self.iterable_obj=iterable_obj
    def __iter(self):
        return self
    def __next__(self):
        if self.iterable_obj.start<=self.iterable_obj.stop:
            result=self.iterable_obj.start
            self.iterable_obj.start=self.iterable_obj.start+self.iterable_obj.step
            return result
        else:
            raise StopIteration
n=myrange(1,10)
iter_obj=iter(n)
for num in iter_obj:
    print(num)"""
