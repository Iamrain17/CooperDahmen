import random
print("I am the fortune teller, welcome to my house. If you want to see your future then give me 30 dollars lol nerd.")
try:
    q1 = int(input ("Whats your lucky number?\n> "))
    q2 = int(input ("How old are you?\n> "))
    q3 = float(input ("Pick a magic multiplier. \n> "))
except:
    print("Invalid Input. Try again lol you nerd.")
def fortune():
    print (random.randint(1,5)*q1*q2*q3)
fortune()
if fortune < 5:
    print("You're gonna be rich and join the U.S. Army!!")
elif fortune < 10:
    print("You're gonna join the U.S. Marine Corp")
elif fortune < 15:
    print("You're joining the Minnesota Army National Guard")
elif fortune < 20:
    print("You're joining the U.S. Navy")
elif fortune < 25:
    print("You're joining the U.S. Air Force")
elif fortune < 30:
    print("You're joining the U.S. Coast Guard")
else:
    print("Invalid Input. Please try again")
    fortune()
