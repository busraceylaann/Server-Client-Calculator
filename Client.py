import socket
import signal, sys, time
server = socket.socket()


def signal_handler(signal, frame):
  print ('Ctrl+C ')
  time.sleep(1)
  sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

try:
    host = socket.gethostname()
    port = 1234
    server.connect((host, port))
    while(True):

        string=input("Problem Girin:")
        server.send(string.encode())
        result=server.recv(1024).decode()
        print("Cevap:",result)


    server.close()
except(Exception):
    server.send("Hata".encode())




