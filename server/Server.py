import socket

host = "0.0.0.0"  #socket.gethostname()
port = 4444 #4444 portuna baglanmasını istiyorum
server = socket.socket()  #soket nesnesi olusturdum
server.bind((host, port)) #verdiğimiz host ve ip adreslerine bağlan
server.listen(5) #sunucunun aynı anda 5 istemciyi dinlemesini istedim
print("Server Çalışıyor")


while(True):
    client, address = server.accept() #istemci ve adresi kabul edilir
    print('Bağlanan Adres', address)
    while(True):
         try:
              problem=client.recv(1024).decode()#istemciden gelen,ara bellek boyutu 1024 olan byte tipindeki mesaj stringe dönüşür
              print("Problem:", problem) #istemciden gelen mesaj
              result=eval(problem) #eval fonksiyonu ile matematiksel işlemi yaptıktan sonra result değişkenıne atanır
              client.send(str(result).encode())   # İstemciye gelen mesajı yanıt olarak geri gönderiyoruz.
         except (Exception ):
               client.send("Hata".encode())

    client.close() #istemciyi sonlandırıyoruz.
