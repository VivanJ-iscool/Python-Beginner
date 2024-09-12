##i = 10
##while i > 2:
##    print(i)
##    i = i - 3
### what does the code above print?
##for i in range(10,2,-3):
##    print(i)
# what does the code above print?
##print("when you have a certain start, end and pattern point, even just a start and end point, we can use a for loop, but when we only have an end point and we need to bail out of a loop when a cretain condition is met, we use a whileloop point and we need to bail out of a loop when a cretain condition is met, we use a while loop.")

#Customized Print Senetences

#To not enter a new line in the shell, we use end="" and if we want a
#tab, we do end="\t"
#Examples:
##print("Hello World")
##print("Hello World")
##print("Hello", end="\t")
##print("World!", end="\t")
##print()
##for i in range(10):
##    print(i, end="\t")
##print()
##for i in range(5):
##    print(i, end="0\n")

#String Formatting

#This is how you write longer statements with multiple variables:
##user_name = "Gurleen"
##user_age = 13
##name = "Kyle"
##print("%s is your name, and %s is mine."%(user_name,name))
##print("Username:%s, age:%d years old."%(user_name, user_age))
# %s represents placeholder for strings
# and %d is the placeholders for numbers

###Nested Loops Examples:
##
##for i in range(2):
##    print("inner")
##    for j in range(2):
##        print("outer")
##
##for i in range(10): # 10 rows
##    for j in range(5): # 5 columns
##        print("*", end="\t")
##        print() # this will JUST print a newline character        
##
##
##for x in range(8): # 8 rows
##    for char in "abcd": # 4 columns
##        print(char, end=" ")
##    print("----")
##
##for i in range(6):
##    for j in range(1):
##        print("3 3 3 3")
##    print(" ")
###
##for a in range(1,6):
##    for b in range(a): # using the iterator variable here!
##        print("#", end="") # no extra characters added
##    print()
###The shape above which i am guessing is a rhombus
###I was very wrong... oh gosh
##
##for i in range(1,11):
##    for j in range(1,11):
##        print(i * j, end="\t")
##    print()
###This works because python will repeat all times tables of 1, then 2,3...all the-
###way up to eleven. This is due to how python recieves info in order from 1, to 11.


#CLASSWORK QUESTIONS:

###1
##for i in range(4):
##    print("* "*4)

###2
##stars = input("If you want more stars say 'more stars'. Else, type anything else to stop it.")
##while stars == 'more stars':
##    for i in range(4):
##        print("* "*4)
##    stars = input("If you want more stars say 'more stars'. Else, do anything else to stop it.")

###3
##name = input("What is your name?")
##for i in range(3):
##    for i in range(5):
##        print(name, end = "  ")
##    print()
##

###4
##for i in range(1,11):
##    for j in range(1,11):
##        print(i * j, end="\t")
##    print()

#5
##for i in range(3):
##    print("         |         |")
##    if i < 2:
##        print("----------------------------")

#6
##print("-------------------------------------------------")
##for i in range(3):
##    for i in range(1):
##        print("         |         |         |         |")
##    print("-------------------------------------------------")



