import socket
import  io

try:

    server = socket.socket()
    server.connect(("server",80))
    while(True):
        string=input("Problem Girin:")
        server.send(string.encode())
        result=server.recv(1024).decode()
        print("Cevap:",result)

    server.close()
except(Exception):
    server.send("Hata".encode())



