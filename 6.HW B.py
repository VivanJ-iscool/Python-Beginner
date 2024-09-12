#1
##var = int(input("What is your age?"))
##
##if var < 12:
##    print("You are very young!")
##elif var >= 12 and var < 20:
##    print("You are a teenager")
##elif var >= 20 or var <=100:
##    print("You are an adult")
##elif var > 100:
##    print("You are very old!")

#2
##var = int(input("Guess a number between 1-100"))
##if var>35 and var<100:
##    print("Your guess is too high")
##elif var<35 and var>0:
##    print("Your guess is too low")
##elif var == 35:
##    print("You got it!")
##else:
##    print("It is between 1-100. Try again")
#3
var = float(input("Type a number either negative or positive"))

if var<0:
    print("That is a negative number")
elif var>0:
    print("That is not a negative number but instead a positive number")
else:
    print("Zero is neither negative or positive")
