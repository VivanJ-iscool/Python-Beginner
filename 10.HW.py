#1
for i in range(1,11):
    print("\n------------------------------------------------------------------------------------------------------------------------")
    for j in range(1,11):
        print("|", j * i, end = "|\t")
print("\n---------------------------------------------------------------------------------------------------------------------------")

#2
star = input("Do you want to make your triangle bigger? Enter y if yes")
i=1
j=1
while star == "y":
    for j in range(1,i):
        print(j * '*', end='\n')
    i+=1
    j+=1
    star = input("Do you want to make your triangle bigger? Enter y if yes")

#3
ustupid = input("Are you stupid")
while ustupid.lower() == "no" or ustupid.lower() =="nope" or ustupid.lower() =="nono" or ustupid.lower() =="nah" or ustupid.lower() =="nuhuh"or ustupid.lower() =="nuh" or ustupid.lower() == "n":
    ustupid = input("Are you stupid")
else:
    print('Yeah, I knew you stupid... just like Ms.Shreya!')
