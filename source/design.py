import os
import time
from sys import *
class intro():

    def design(self):
        os.system('clear')
        user_choice=""
        print("************************************************************************************")
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<        QUIZZZYY           >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("************************************************************************************")

        print("\n\t\t\t*------------**-------------*")
        print("\t\t\t|  CHOOSE YOUR CATEGORY   |")
        print("\t\t\t*-----------**--------------*")
        print("\n\t*-----------------------------****----------------------------------*")
        print("\t|  1. MATHEMATICS  |  2. SCIENCE  |  3. HISTORY  |  4. GK  |  5.Quit  |")
        print("\t*-------------------------------****-----------------------------------*")

        try:
            user_choice = int(input("\n\t\t\tYOUR CHOICE : "))
            if(user_choice==1):
                filename = "maths_ques.csv"
            elif(user_choice==2):
                filename = "science_ques.csv"
            elif(user_choice==3):
                filename = "history_ques.csv"
            elif(user_choice==4):
                filename = "GK_ques.csv"
            elif(user_choice==5):
                exit(0)
        except ValueError:
            print("\n\t\tSORRY PLEASE ENTER INTEGER VALUE")
            time.sleep(1)
            obj = intro()
            obj.design()
            
        return filename

      
    
