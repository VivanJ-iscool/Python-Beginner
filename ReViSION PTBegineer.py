#1
##greetings = input("What type of greeting do you want 'type : christmas, halloween, etc.'")
##name = input("To whom do you greet this to?")
##print(greetings, "\nTo:", name)

#2
##while True:
##    age = int(input("How old are you?"))
##    if age >= 18 and age < 122:
##        print("You are old enough to vote for Obama!!!")
##    elif age < 18 and age > 0:
##        print("Awww. You can't vote :( ")
##    else:
##        print("Nice Try Buddy. Try Again.")
##    ch=input('\nEnter y to continue and do not enter y to exit')
##    if ch != "y":
##        break

#3
##print("COUNTDOWN:")
##for i in range(10,0,-1):
##    print(i)
##print("Happy New Year!!!")

#4
ustupid = input("Are you dumb or stupid?")
while ustupid.lower() != "yes" or  ustupid.lower() != "yup" or ustupid.lower() != "ya":
    ustupid = input("Are you dumb or stupid?")
    if ustupid == "yes":
        print("Hahaha! Your stupid dumdum!!! Just like my life :(")
        break
