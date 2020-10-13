from socket import *
import re
import os
import pickle
from time import *
import csv
from design import * 
from client_funcs import *
import random
d=dict()
host_ip = "192.168.60.127"
port = 9999
client = socket(AF_INET, SOCK_STREAM)

def client_connection():

    print('Waiting for connection response')
    try:
        client.connect((host_ip,port))
    except socket.error as e:
        print(str(e))

    while True:
        obj = intro()
        filename=obj.design()  
          #graphical input
        res = re.match('[\w]+_ques\.csv',filename)
        client.send(filename.encode()) #request server to send questions
        try:
            if(res!= None):
                print("yes")
                if(os.path.exists(filename)):
                #filename_ques.csv already exists
                    pass
                else:
                    file = open(filename,'wb')
                    filedata = client.recv(1024)
                    file.write(filedata)
                    file.close()
            else:
                pass #wrong filename (file doesnt exists)
        except:
            print("Error Occured while reading file")
        quiz_contest(filename)
            #clients all answers list to be sent to server for validation 
        #print("after quiz")
        #print(d)
        answers_list = pickle.dumps(d)  #dict cannot be sent directly, send() requires bytes not dict
        #print(answers_list)
        res = random.randrange(6)
        print("\n\n\n\n\t\tCongratulations!!!!")
        sleep(2)
        os.system('clear')
        print("YOUR SCORE is",res)
        sleep(3)
        os.system('clear')       
        print("THANK YOU!!! STAY SAFE \U0001F637 \U0001F637")
        sleep(2)
       


client_connection()
