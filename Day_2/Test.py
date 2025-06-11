"""class apple_design:
    count=0  #classvariable or static variable
    def __init__(self,cpu,ram):#constructor
        self.cpu=cpu
        self.ram=ram
    def mobile(self,cpu,ram): #instances variable
        print("this is phone")
        print(self.cpu,self.ram)
m1=apple_design(4.5,8)
m2=apple_design(6.8,7)
m1.mobile()
m2.mobile()
print(id(m1))
print(id(m2))
print(type(self))
class car:
    wheel=4 #class variable
    def __init__(self,modal,mil,year):
        self.modal=modal
        self.mil=mil
        self.year=year
    def car_info(self):
        print("modal no",self.modal)
        print("car mil", self.mil)
        print("car year", self.year)
        print("car wheels", self.wheel)
car1=car(modal=input(),mil=str(input()),year=int(input()))
#car2=car("hyundi",67.9,2030)
car1.car_info()
#car2.car_info()
class employee:
    office="NIET"
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
    def show_detail(self):
        print(f"company name:{employee.office}\nname:{self.name}\ndesignation:{self.designation}")
e1=employee("mohit","hod of data science")
e1.show_detail()
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"the name is{self.name} and age is {self.age}"
e=person("mohan",34)
class student:
    count=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        student.count+=1
    def msg(self):
        print("hello"+self.name+"you get",self.marks,"%marks")
    @classmethod
    def object_count(cls):
        return cls.count
s1=student("aman",56)
s2=student("naman",89)
print(student.object_count())
print(s1.object_count())
class mathoperation:
    @staticmethod
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
obj=mathoperation()
r1=mathoperation.add(12,5)
r2=mathoperation.sub(12,5)
print(f"addition:{r1}")
print(f"subtraction:{r2}")
class student:
    #default constructor
    def __init__(self):
        print("Default constructor called")
    def __init__(self,name,marks,age):
        self.name=name
        self.marks=marks
        self.age=age
        print("parameterized constructor called")
    def show_info(self):#instance
        print("name",self.name)
        print("marks", self.marks)
        print("age",self.age)
    def __del__(self):
        print("destructor called")
#s1=student()
s2=student("rohan",67,16)
s2.show_info()
del s2
class add:
    first=0
    second=0
    answer=0
    def __init__(self,f,s):
        self.first=f
        self.second=s
    def display(self):
        print("first number=",self.first)
        print("second number=",self.second)
        print("addition=",self.answer)
    def calculate(self):
        self.answer=self.first+self.second
obj=add(1000,2000)
obj.calculate()
obj.display()"""
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
person=person("alice",34)
#use getattr to get the valueof attribute
name=getattr(person,"name")
print(f"name:{name}")
#use setattr to set the value of attribute
setattr(person,"age",56)
print(f"updated age:{person.age}")
#use hasattr to check if attribute exist
has_name=hasattr(person,"name")
print(f"has attribute 'name':{has_name}")
#use delattr to delete attribute
delattr(person,"age")
has_age=hasattr(person,"age")
print(f"has attribute 'age' after deletion:{has_age}")
