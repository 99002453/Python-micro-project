from socket import *
import re
import os
import pickle
from time import *
import csv
from design import * 
d=dict()
def p_welcome():
    print("Let's Start!!!\n")
    sleep(2)
    print("PRESS ENTER TO CONTINUE")
    val=input()
    if(val==""):
        os.system('clear')
        print("\n\n\n\n\n\n\n\n\n\n\n\t\t\t\tAll The Best",end="")
        print("\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\U0001f600","\U0001f600","\U0001f600") 
        sleep(2)
        os.system('clear')
def quiz_contest(filename):
    with open(filename, mode ='r')as file: 
            p_welcome()
            csvFile = csv.reader(file)
            for lines in csvFile:
                    print ('\033[1m \033[91m \033[4m' +  lines[1] + '\033[0m'+"\n")
                    #print(lines[1],"\t\n")
                    sleep(0.5)
                    print("1.",lines[2],"\n")
                    sleep(0.5)
                    print("2.",lines[3],"\n")
                    sleep(0.5)
                    print("3.",lines[4],"\n")
                    sleep(0.5)
                    print("4.",lines[5],"\n")
                    sleep(0.5)
                    ans=str(input("\U0001f600 enter your answer number:\n"))
                    sleep(2)
                    os.system('clear')
                
                    if(ans=="1"):
                            d[lines[0]]=lines[2]
                    elif(ans=="2"):
                            d[lines[0]]=lines[3]
                    elif(ans=="3"):
                            d[lines[0]]=lines[4]
                    elif(ans=="4"):
                            d[lines[0]]=lines[5]
                    else:
                        d[lines[0]]="wrong"  
                    print("good going!!!:-)") 
                    sleep(1) 
                    os.system('clear')  