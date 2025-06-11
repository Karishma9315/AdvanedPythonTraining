#a=int(input("enter the number 1:"))
#b=int(input("enter the number 2:"))
#c=int(input("enter the number 3:"))
#sum=a+b+c
#print(sum)
"""a=str(input("enter the number:"))
b=str(input("enter the number:"))
c=str(input("enter the number:"))
#z=a+b+c
#print(z)
print({},{} are numbers,str.format(a,b))
age=int(input("enter the age"))
if age>=18:
    print("you can vote")
    print("congrats")
percentage=int(input("enter the percentage:"))
if percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("Grade B")
else:
    print("Grade C")
a=str(input("enter the number:"))
b=str(input("enter the number:"))
c=str(input("enter the number:"))
if a>b:
    if a>c:
        print(a,"is greatest")
elif b>c:
    print(b,"is greatest")
else:
    print(c,"is greatest")
n=intt("enter"))
sum=0
while n>0:
    sum=sum+n
    n=n-1
print("sum of numbers is",sum)
n=[10,29,30,45,67,87]
for x in n:
    i = 1;
    flag = 0
    while i<=x:
        if x%i==0:
            flag+=1
        i+=1;
    if flag==2:
        print(x)
def findsum(a,b):
    result=a+b
    return result
x=5
y=8
z=findsum(x,y)
print(z)
def sum_num(num1,*num):
    result=num1
    for i in num:
        result+=i
    return result
r=sum_num(10,20,30)
print(f"the sum of numbers is:{r}")
num=[1,2,3,4,5,6,7,8]
def iseven(n):
    if n%2==0:
       return 1
even_num=filter(iseven,num)
even_num_list=list(even_num)
print(even_num_list"from functools import reduce
num=[10,5,7,9,12]
large=reduce(lambda x,y:x if x>y else y,num)
print(large)
from functools import reduce
num=[10,5,7,9,12]
large=reduce(lambda x,y:x if x>y else y,num)
print(large)"""
def generate(name,marks,subject="python"):
    average=sum(marks)/len(marks)
    grade="A"if average>=90 else "B" if average>=75 else "C"
    print(f"{name}'s {subject}Report\nMarks:{marks}\nAverage:{average}\nGrade:{grade}\n")
generate(input("name:"),marks=str(input("marks:")))
"""cart={}
def item(name,price=100,qty=1):
    cart[name]=cart.get(name,0)+qty
    print(f"Added{qty}*{name}")
for i in range(3):
    item(input("item:"), qty=int(input("qty:")))
print(cart)"""
