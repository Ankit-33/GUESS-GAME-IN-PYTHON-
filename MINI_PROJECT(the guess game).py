import random
randnumber=random.randint(1,100)
#print(randnumber)
input_user=None
while(input_user!=randnumber):
    input_user=int(input("Enter the number you guessed\n"))
    if(input_user==randnumber):
        print("you guessed the correct number...\n")
    elif(input_user>randnumber):
        print("guessed number is greater!!\n")
    else:
        print("guessed number is smaller!!!\n")
