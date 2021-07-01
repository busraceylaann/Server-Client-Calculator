import socket
server = socket.socket()

host = socket.gethostname()
port = 1234
server.bind((host, port))
server.listen(5)
print("Server Çalışıyor")


while(True):
    client, address = server.accept()
    print('Bağlanan Adres', address)
    while(True):
         try:
              problem=client.recv(1024).decode()
              print("Problem:", problem)
              result=eval(problem)
              client.send(str(result).encode())
         except (Exception ):
               client.send("Hata".encode())


    client.close()
