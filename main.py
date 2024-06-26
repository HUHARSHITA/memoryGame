import os
import time
import sys
import random
def stringGame(GenerateFrom):
    for num in simonSaysList:    
        studentAnswer=input("Please enter the Element I asked(press enter after each number):")   
        if studentAnswer==num:
            print("Well done!")   
            continue 
        else:
            print("You did not write correct no.".upper())
            print("GAME OVER!!")
            print(simonSaysList)
            print("YOUR SCORE IS : ",question)
            sys.exit()
            break;

def numGame(GenerateFrom):
    for num in simonSaysList:    
        studentAnswer=int(input("Please enter the Element I asked(press enter after each number):") )  
        if studentAnswer==num:
            print("Well done!")   
            continue 
        else:
            print("You did not write correctly".upper())
            print("GAME OVER!!")
            print(simonSaysList)
            print("YOUR SCORE IS : ",question)
            sys.exit()
            #break;

print("Select category for Game:")
print("1.Numbers\n2.Alphabets\n3.Animals\n4.Birds")
print("5.Vehicles\n6.Fruits\n7.Vegetables\n")
try:
    choice=int(input("Enter your choice(1-7):"))
except:
    print("Invalid Datatype entered")
    exit(1)
GenerateFrom=[]
if choice==1:
    GenerateFrom=list(range(0,10))  #0,1,2,3,4,5,6,7,8,9,0

elif choice==2:
    GenerateFrom=[]
    for i in range(97,123):
        GenerateFrom.append(chr(i))

elif choice==3:
    GenerateFrom=['dog','cat','bear','monkey','rabbit','camel']
elif choice==4:
    GenerateFrom=['pigeon','crow','peacock','hen','duck','sparrow']
elif choice==5:
    GenerateFrom=['car','truck','bike','scooter','cycle','train','plane']
elif choice==6:
    GenerateFrom=['mango','strawberry','apple','banana','orange','papaya']
elif choice==7:
    GenerateFrom=['potato','tomato','brinjal','peas','carrot','beans']
else:
    print("Invalid Choice")
    exit(1)
simonQuestionAmount=True
simonSaysList=[]
question = 0

print("Let's test your Memory.\n")

while simonQuestionAmount:
    chosenNumber=random.choice(GenerateFrom)
    simonSaysList.append(chosenNumber)

    print("Elements you have to memorize :".upper(),simonSaysList)
    time.sleep(2)

    os.system("cls")
    if choice==1:
        numGame(GenerateFrom)
    else:
        stringGame(GenerateFrom)

    question+=1
