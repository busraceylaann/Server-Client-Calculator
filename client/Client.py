import socket
import signal, sys, time
import argparse

#Docker işlemi yapacağımız için,serverin hostunu burada parse ediyoruz.Bunun için argparse modülü kullanıyoruz.
#ArgumentParser üzerinden yeni bir nesne oluşturuyoruz.
parser = argparse.ArgumentParser(description='calculation descrription')
# gerekli argümanları ekliyoruz
parser.add_argument('--host', action="store", dest="host", required=True, help="joblist as dict")
args = parser.parse_args()

server = socket.socket()

#Ctrl-C ile programı sonlandırmak istiyorum,sinyal  oluşturuyorum.
def signal_handler(signal, frame):
    print ('Ctrl+C ')
    server.close()
    time.sleep(1)
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

try:
    server.connect((args.host, 4444))
    while True:
        string = input("Problem Girin:") #kullanıcıdan problemi alıyoruz
        server.send(string.encode()) #servera problemı gönderiyoruz
        result = server.recv(1024).decode() #serverdan gelen cevabı alıp result değişkenine atıyoruz
        print("Cevap:", result) #cevabı yazdırıyoruz

except(Exception):
    server.send("Hata".encode())



