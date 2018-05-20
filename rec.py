#!/usr/bin/python3
import threading
import  socket,time
import matplotlib.pyplot as plt

rec_ip="127.0.0.1"
myport=9999
       
#  below method with argument creating a socket called  s 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#  now connecting ip  and port 
s.bind((rec_ip,myport)) 

#recieving code
'''
data=s.recvfrom(1000)
c=1
while data[0].decode()!='quit':
       print ("DATA: ",data[0].decode(),"IP: ",data[1][0],"port: ",data[1][1])
       data=s.recvfrom(1000)
'''
def recieve():
c=1
 try:  
   threading.Timer(1.0, recieve).start()
   data=s.recvfrom(1000)
   
   while data[0].decode()!='quit' and c<11:
       print (c)
       print ("DATA: ",data[0].decode(),"IP: ",data[1][0],"port: ",data[1][1])
       data=s.recvfrom(1000)
   c=c+1
 except:
   print ("ERROR")
      

recieve()


time.sleep(2)
print ("session 1 over")
c=1
recieve()
time.sleep(2)
print ("session 2 over")








'''

#data processing
ins=0
tempsol=[]
wc=[]
sol=[]
count=[]
datafinal=[]
data=0
dataf=0

data=input("please enter data: ")
dataf=data.strip()
datafinal=dataf.split()

for i in datafinal:
       if i in tempsol:
           index=tempsol.index(i)
           count[index]=(count[index]+1)
       else:
           tempsol.append(i)
           count.append(1)
ins=ins+1
    



for a in tempsol:
         if a in sol:
            index=sol.index(a)
            index1=tempsol.index(a)
            wc[index].append(count[index1])                                  # counter.append(count[index1])
          
         else:
            counter=[]
            sol.append(a)
            for q in range(0,ins-1): 
                   counter.append(0)
            index1=tempsol.index(a)
            counter.append(count[index1])
            wc.append(counter)
for char in wc:
     if len(char) < ins:
          for p in range(0,ins-1):
               char.append(0)            

print(sol,wc,ins)


tempsol=[]

count=[]
datafinal=[]
data=0
dataf=0

data=input("please enter data: ")
dataf=data.strip()
datafinal=dataf.split()

for i in datafinal:
       if i in tempsol:
           index=tempsol.index(i)
           count[index]=(count[index]+1)
       else:
           tempsol.append(i)
           count.append(1)
ins=ins+1

for a in tempsol:
         if a in sol:
            index=sol.index(a)
            index1=tempsol.index(a)
            wc[index].append(count[index1])                                  # counter.append(count[index1])
          
         else:
            counter=[]
            sol.append(a)
            for q in range(0,ins-1): 
                   counter.append(0)
            index1=tempsol.index(a)
            counter.append(count[index1])
            wc.append(counter)
for char in wc:
     if len(char) < ins:
          for p in range(0,ins-1):
               char.append(0) 
         

print(sol,wc,ins)

wc1=[]
wc2=[]
for i in range(0,len(wc)):
    wc1.append(wc[i][0])
    wc2.append(wc[i][1])
plt.bar(sol,wc1,color='g')
plt.show()
plt.bar(sol,wc2)
plt.show()



'''


