###CLASSWORK:
###1
##for v in range(1,11):
##    print("Vivan")
##
###2
##lyric = "I will not obey. You cannot tell when I cannot say"
##for letter in lyric:
##    if letter in "aeiouAEIOU":
##        print(letter)
##
###3
##sum = 0
##for var in range(1,101):
##    sum = sum + var
##print(sum)
##
###4
##number_of_b = 0
##for letter in "Barry B.Benson":
##    if letter == "b":
##        number_of_b = number_of_b + 1
##        print(number_of_b)
#5
##lenght = (input("What is your name? "))
##lenght2 = 0
##for letter in lenght:
##    lenght2 = lenght2 + 1
##print(lenght2)
##
#HOMEWORK:
#1
star = ""
for i in range(1,6):
    star = i * "*"
    print(star)
2
star = ""
for i in range(6,0,-1):
    star = i * "*"
    print(star)
#3
word = str(input("What is your favourite word?"))
letter = str(input("What is your favourote letter?"))
count = 0
for v in word:
     if v == letter:
          count = count + 1
print(count)
4
sentence = str(input("Write a sentence:  "))
spaces = 0
for character in sentence:
     if character == " ":
          spaces = spaces + 1
print(spaces +1)



5
for i in range(0,101,5):
     print(i)

#6
# an iterator pretty much is the string which can have written anything written in it and print it out line by line.

#7
#a range determines how many times the loop repeats. the first input in a range is the end point. The second input is the start point but you would format it as the first and the thid input is the pattern rule for example, addin by 5.



#BONUS:
##sentence = str(input("Write a sentence:  "))
##special_charac = 0
##for character in sentence:
##     if character in "!@#$%^&() ":
##          special_charac = special_charac + 1
##print(special_charac)

#HOMEWORK:

# I HAVE BEEN TRYING FOR 2 HOURS AND I STILL CAN'T FIGURE IT OUT. I'M SORRY
word = str(input("Name a word: "))
underscore = "_"
for letter in word:
     if letter == "_":
          underscore = underscore * len(word)
print (underscore)






