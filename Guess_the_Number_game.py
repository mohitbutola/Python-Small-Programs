'''This is simple gme of Gussing a Number Between You and Machine. 
Who ever Guesses the other number is less Guesses will win the game. 
Prass 'Q' or 'q' for quiting the game

---> Created By Mohit Butola. TCET.'''

import random

while(True):

    print("\n----->  Number Guess using Pytho:  <------")
    print("\n----->  PRESS q TO QUIT THE GAME:  <------")
    try:
        n = int(input("\nPlease Enter a Number between 1 to 10 for Machine to guess : "))
        if n>=1 and n<=10:
            count = 0
            g = 0
            while g == 0:
                gussNo = random.randint(1,10)
                count += 1
                
                if gussNo == n:
                    g = 1
                    break

            print(f"\nThe Mechine Gussed your Nuber in {count} guses.")

            print("\n(o)---___--(o) \nNow Its your Turn to guss the Number:")

            mNumber =  random.randint(1,10)
            userGussed = None
            count2 = 0

            while(userGussed != mNumber):
                userGussed = int(input("\nEnter Your Gussed Number from 1 to 10 : "))

                if(userGussed < mNumber):
                    print("Your Number is Less then Machine Picked Number.")
                    count2 += 1
                else:
                    print("Your Number is Greater then Machine Picked Number.")
                    count2 += 1
            print(f"\nYou Have Gussed Machine Number in {count2} Guess.")

            if count2 < count:
                print(f"\nHURRY!!! You Woned the Game By {count-count2} Gusess")
            elif count2 == count:
                print(f"\nLOL!! The Game is Tied.")
            else:
                print(f"\nMachine Woned the Game By {count2-count} Gusess")
        else:
            print(f"Enter a Number in Range 1 to 10. You Entred {n}")

    except Exception as e:
        print(f"Please Provide a Number Only NO ALPHABATES (error) :  ") 

    quit = input("\nPRESS Q TO QUITE THE GAME : ")
    if (quit == 'q' or quit == 'Q'):
        break



        
