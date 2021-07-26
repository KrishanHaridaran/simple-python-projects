#Note that this code can only use a port at a time for understanding purposes.

import socket

ip = input("Enter Target IP : ")
port = int(input("Enter Target Port : "))

socket = socket.socket()
socket.connect((ip,port))
banner = socket.recv(1024)
print (banner.decode())
socket.close()

