"""n=10
x=n+5
print(x)
y=n.__add__(5)
print(y)
str='10'
x=str+'5'
print(x)
class mass:
    def __init__(self,kg=0,g=0):
        self.kg=kg+g//1000
        self.g=g%1000
    def __add__(self,other):
        total_kg=self.kg+other.kg
        total_g=self.g+other.g
        if total_g>=1000:
            total_kg+=total_g//1000
            total_g=total_g%1000
        return mass(total_kg,total_g)
    def __repr__(self):
        return f"{self.kg}kg and {self.g}g"
m1=mass(2,400)
m2=mass(5,700)
m3=m1+m2
print(m3)
class year:
    def __init__(self,yr=0,mon=0):
        self.yr=yr+mon//12
        self.mon=mon%12
    def __add__(self,other):
        total_yr=self.yr+other.yr
        total_mon=self.mon+other.mon
        if total_mon>=12:
            total_yr+=total_mon//12
            total_mon=total_mon%12
        return year(total_yr,total_mon)
    def __repr__(self):
        return f"{self.yr}yr and {self.mon}months"
m1=year(2,6)
m2=year(5,7)
m3=m1+m2
print(m3)
class large:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        def __gt__(self,other):
            r1=self.m1+self.m2
            r2=other.m1+other.m2
            if r1>r2:
                return True
            else:
                return False
s1=large(45,67)
s2=large(78,39)
if s1>s2:
    print("s1 is greater")
else:
    print("s2 is greater")
import math
class fract:
    def __init__(self,num,deno):
        self.num=num
        self.deno=deno
        self.simple()
    def simple(self):
        common=math.gcd(self.num,self.deno)
        self.num//=common
        self.deno//=common
    def __add__(self,other):
        new_num=self.num*other.deno+other.num*self.deno
        new_deno=self.deno*other.deno
        return fract(new_num,new_deno)
    def __eq__(self,other):
        return self.num==other.num and self.deno==other.deno
    def __it__(self,other):
        return self.num*other.deno<other.num*self.deno
    def __repr__(self):
        return f"{self.num}/{self.deno}"
f1=fract(3,5)
f2=fract(3,5)
f3=f1+f2
print(f3)
print(f1==f2)
print(f1<f2)
class myclass:
    def __init__(self,value):
        self.value=value
def printvalue(obj):
    print(f"the value is:{obj.value}")
obj=myclass(10)
printvalue(obj)
class person:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return f"person({self.name})"
class greet:
    def generate(self,person):
        return f"hello,{person.name}!welcome!"
p=person("alien")
g=greet()
msg=greet.generate(p)
print(msg)"""
class rectangle:
    def __init__(self,w,h):
        self.w=w
        self.h=h
    def area(self):
        return self.w*self.h
    def combine(self,other):
        newarea=self.area()+other.area()
        new_w=self.w
        new_h=newarea/new_w
        return rectangle(new_w,new_h)
    def __repr__(self):
        return f"rectangle({self.w},{self.h})"
r1=rectangle(4,5)
r2=rectangle(6,8)
c=r1.combine(r2)
print(c)
