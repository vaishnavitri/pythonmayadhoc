#!/usr/bin/python3

import  socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#socket declaration

#senders code
i=input("Enter Text: ").encode()
while i.decode()!='quit':
      s.sendto(i,("127.0.0.1",9999))    
      i=input("Enter Text: ").encode()





 

