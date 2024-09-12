##name = input("What is your name?")
##letter = input("What is your favourite letter?")
##letter_count = 0
##vowel_count = 0
##for char in name:
##    if char == letter:
##        letter_count += 1
##    if char in "aeiouAEIOU":
##            vowel_count += 1
##print("You have", letter_count,\
##"instances of your favourite letter", letter,"in your name!")
##print("You have", vowel_count, "vowels in your name.")
##print("The total length of your name is", len(name))

##i=0
##while i<10:
##    print("Hello")
##    i += 1
##print(i)

#HOMEWORK(Classwork Questions)

#1.
##guess = "x"
##secret_letter = "b"
##while guess != secret_letter:
##    print("Wrong letter! Guess again!")

#2.
##dollars = 35
##while dollars < 20:
##print("Insufficient funds.")

#3.
##secret_word = "hatch"
##guess = "placeholder"
##while guess != secret_word:
##    print("I challenge you to guess the word!")
##    guess = input("Enter your guess: ")
##print("Wow! You got it!")
    
#4
##secret_word = "hatch"
##guess = "placeholder"
##while guess != secret_word:
##    print("I challenge you to guess the word!")
##    guess = input("Enter your guess: ")
##    if guess == "I don't know":
##        print("Alright, the word was", secret_word)
##print("Wow! You got it!(Unless you gave up and said you don't know)")

#5.
##even = 2
##odd = 1
##number = int(input("Write a number from 1-100: "))
##while number == odd:
##    number = int(input("Write a number from 1-100: "))
##else:
##    print("Even is good!!!")
    

#6
##for i in range(2,9):
##    print(i)
##num = 2
##while num < 9:
##    print(num)
##    num += 1


#7
##guess = "placeholder"
##number_of_marbles = 249
##while guess != number_of_marbles:
##    guess = int(input("Guess the number of marbles in the jar(will keep asking till you get answer): "))
##print("CORRECTAMUNDO!!! Congrats!")



#Shreya's annoying problems 😠:

##a = float(input("Enter your first decimal number"))
##b = float(input("Enter your second decimal number"))
##c = float(input("Enter your final decimal number"))
##if a > b and a > c:
##    print(a)
##elif b > a and b > c:
##    print(b)
##else:
##    print(c)


##num = int(input("Enter you factoring number: "))
##for i in range(1,num + 1):
##    if num % i == 0:
##        print(i)



###1 and 2
##phone_num =str(input("Enter your number: "))
##while len(phone_num) != 10:
##    phone_num =str(input("Enter your number: "))
##
###3 and 4
##symbol = "!@#$%^&*"
##ch = 0
##while ch<5:
##    password = input("Type a passcode:  ")
##    for letter in password:
##        if letter in symbol:
##            print("Your password is strong!!!")
##            ch=5
##            break
##    else:
##        ch+= 1
##        print("Make a password with special characters\n", ch)
##            
###5
##for i in range(0,101,3):
##    print(i)
##
###6
##i = 0
##while i < 101:
##    i += 3
##    print(i)
##    
###7
##num = 4
##guess = int(input("Guess a number from 1-10: "))
##while num != guess:
##    guess = int(input("Guess a number from 1-10: "))
##print("Congrats! You got it!")
##
###8
##num = 4
##guess = int(input("Guess a number from 1-9: "))
##while num != guess:
##    guess = int(input("Guess a number from 1-9: "))
##    if guess >= 10 or guess <= 0:
##        print("Try to guess a number between 1-9")
##print("You got it! Nice")
##
##
###9
##dollars = 35
##while dollars < 20:
##    print("Insufficient funds.")

#SHREYA'S ANNOYING PROBLEM
##choice = input("Enter a number with either 1,2,3 or 4")
##while choice not in  "1234":
##    if choice.isdigit() == True:
##        print("Enter your number with the circumstances")
##    else:
##        print("Do not enter words, enter digits/numbers")
##    choice = input("Enter either 1,2,3 or 4: ")
##print("BINGO!!!")

#Homework:
list_of_vowels = "aeiouAEIOU"
vowel_counter=0
word = input("Enter a Word: ")
for letter in word:
    if letter in list_of_vowels:
        vowel_counter += 1
print(vowel_counter)


