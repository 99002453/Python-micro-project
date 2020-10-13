from socket import *
import pickle
from _thread import *
import csv
import time
host_ip = "192.168.60.127" #192.168.60.127
port = 9999
ThreadCount = 0
server = socket(AF_INET, SOCK_STREAM)

def multi_threaded_client(connection,address):
    #accepting requests/message from client
    while True:
        try:
            filename = connection.recv(1024)
            filename = filename.decode()
            file = open(filename,'rb')
            filedata = file.read(1024)
            connection.send(filedata)
            file.close()
        except FileNotFoundError:
            print(FileNotFoundError.args())

        clients_answers = connection.recv(1024)
        clients_answers =pickle.loads(clients_answers)
        fname=filename.split("_")
        ansfilename=fname[0]+"_ans.csv"
        f=open(ansfilename)
        csv_f=csv.reader(f)
        keys=list(clients_answers.keys())
        score=0
        for row in csv_f:
            if(row[0] in keys):
                if row[1]==clients_answers.get(row[0]):
                    score=score+1
                        
        print("SCORE :"+str(score))
        connection.close()
        return

        

def server_connection():
    try:
        server.bind((host_ip,port))
    except socket.error as e:
        print(str(e))

    print('Socket is listening..')
    server.listen(20)
    while True:
        connection, address = server.accept()
        print("Connection established to client IP:Port - "+str(address[0])+" : "+str(address[1]))
        start_new_thread(multi_threaded_client, (connection,address ))
      


server_connection()
server.close()
