#!usr/bin/python3

import numpy as np
 
x=(input("enter no: "))
a=[]
mul=[1]
f=0

while(x!='q'):
     a.append(x)
     x=input("enter no: ")

     

l=len(a)
if l==1 or l==2:
    x=input("please enter one more no: ")
    a.append(x)

for y in range(2,int(l/2)+1):
    if(l%y==0):
        mul.append(y)
        f=1
if f is 0:
     x=input("please enter one more no: ")
     a.append(x)
     l=len(a)
     for y in range(2,int(l/2)+1):
         if(l%y==0):
            mul.append(y)
     
   
print (mul,l)
for m in mul:
    m1=int((l)/(m))
    array1=np.array(a)
    array2=array1.astype(int)
    array3=np.reshape(array2,(m,m1))
    print(array3)

