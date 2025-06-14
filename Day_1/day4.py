"""class parent:
    def feature1(self):
        print("feature 1 of parent")
    def feature2(self):
        print("feature 2 of parent")
class child(parent):
    def feature3(self):
        print("feature 3 of child")
    def feature4(self):
        print("feature 4 of child")

p=parent()
c=child()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
p.feature1()
class parent:
    def __init__(self):
        pass
    def feature1(self):
        print("feature 1 of parent")
    def feature2(self):
        print("feature 2 of parent")
class you(parent):
    def __init__(self):
        super().__init__()
    def feature3(self):
        print("feature 3 of child")
    def feature4(self):
        print("feature 4 of child")
class brother(parent):
    def __init__(self):
        pass
    def feature5(self):
        print("feature 5 of parent")
    def feature6(self):
        print("feature 6 of parent")
class sister(parent):
    def __init__(self):
        pass
    def feature7(self):
        print("feature 7 of child")
    def feature8(self):
        print("feature 8 of child
b=brother()
b.
class person:
     def __init__(self,name,lname):
         self.name=name
         self.lname=lname
         print("first name is {} and last name is {}".format(self.name,self.lname))
class student:
    _name=None
    _roll=None
    _branch=None
    def __init__(self,name,roll,branch):
        self._name=name
        self._roll=roll
        self._branch=branch
    def _display(self):
        print("roll:",self._roll)
        print("branch:",self._branch)
class learn(student):
    def __init__(self,name,roll,branch):
        student.__init__(self,name,roll,branch)
    def display(self):
        print("name:",self._name)
        self._display()
obj=learn("aditi",123,"data science")
obj.display()
#DUCK TYPING
class duck:
    def quack(self):
        print("quack!")
class person:
    def quack(self):
        print("i am quacking like a duck!")
d=duck()
p=person()
d.quack()
p.quack()
#function OVERLOADING
class bird:
    def fly(self):
        print("fly with wings")
class aeroplane:
    def fly(self):
        print("fly with fuel")
class fish:
    def fly(self):
        print("fish swim in sea")
for obj in bird(),aeroplane(),fish():
    obj.fly()
class myclass:
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
sm=myclass()
print(sm.sum(1,6))
print(sm.sum(1))
print(sm.sum(2,4,6))
class student:
    m1
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3
s1=student(34,56)
s2=student(67,78)
s3=s1+s2
print(s3.m1)
class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return vector(self.x-other.x,self.y-other.y)
    def __mul__(self,other):
        return vector(self.x*other.x+self.y*other.y)
    def __str__(self):
        return f"({self.x},{self.y})"
v1=vector(2,4)
v2=vector(4,6)
v3=v1+v2
v4=v1-v2
v5=v1*v2
print("v1:",v1)
print("v2:",v2)
print("v1+v2:",v3)
print("v1-v2:",v4)
print("v1*v2:",v5)
class bank:
    def __init__(self,acc,bal):
        self.acc=acc
        self.bal=bal
    def cal(self):
        return self.acc*0.01
    def display(self):
        print(f"account no: {self.acc}, balance:{self.bal}")
class savingacc(bank):
    def cal(self):
        return self.bal*0.04
class current(bank):
    def cal(self):
        return self.bal*0.02
sav=savingacc("s234",4000)
curr=current("c567",8000)
sav.display()
curr.display()
print(f"saving account interest:{sav.cal()}")
print(f"current account interest:{curr.cal()}")
from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass
    def message(self):
        print("Computer is electronic device")
class laptop(computer):
    def process(self):
        print("executing laptop process")
class desktop(computer):
    def process(self):
        print("executing desktop process")
c=laptop()
c1=desktop()
c1.process()
c.message()
c.process()
c1.message()"""
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def desc(self):
        return "this is a shape"
class circle(shape):
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        return 3.14*self.rad**2
    def perimeter(self):
        return 2*3.14*self.rad
c=circle(4)
print(f"circle area:{c.area()}")
print(f"circle perimeter:{c.perimeter()}")