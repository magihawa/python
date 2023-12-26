import random
import sys
ticket = ''
win = 0
tries = 0

while ticket != win:
        ticket = int(input("Your ticket number from 1 to 10: "))
        tries += 1
        win = random.randrange(1, 11, 1)
        if ticket != win:
            print (f"Sorry, the winning ticket is {win}. Better luck next time!")
        else:
            print (f"Your ticket {ticket} is the winning ticket! Congratulations!")    
            print (f"Your number of tries is {tries}.")
            sys.exit    