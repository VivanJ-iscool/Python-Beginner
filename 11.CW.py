#MINI CHALLENGES:

#1
##for i in range(1,101):
##    if i % 15 == 0:
##        print("FIZZBUZZ")
##    elif i % 3 == 0:
##        print('Fizz')
##    elif i % 5 == 0:
##        print("Buzz")
##    else:
##        print(i)
##
#2
for i in range(10):
    for j in range(10):
        print(' '* j * j,end='*\n')
    for j in range(10,-1,-1):
        print(' '* j * j,end='*\n')

#3
##cash = float(input("How much money do you have and I will convert it to coins"))
##t = 0
##l = 0
##q = 0
##d = 0
##n = 0
##while cash > 2.00:
##    t += 1
##    cash = cash - 2
##while cash >= 1.00:
##    l += 1
##    cash = cash - 1
##while cash >= 0.25:
##    q += 1
##    cash = cash - 0.25
##while cash >= 0.1:
##    d += 1
##    cash = cash - 0.1
##while cash >= 0.05:
##    n += 1
##    cash = cash - 0.05
##print("Your fewest coins add up to:", t, "toonies, ", l, "loonies, ", q, "quarters, ", d, "dimes, ", n, "nickels.")

#BONUS:
##i = 4
##j = 7
##operation = input("What mathematical operation do you want to perform from addition, subtraction, multiplication or division. Say add, subtract, multiply or divide and say exit to get out.")
##while operation != "exit":
##    if operation == "add":
##        print("Random addition question: 4 + 7 = ", i + j)
##        operation = input("What mathematical operation do you want to perform from addition, subtraction, multiplication or division. Say add, subtract, multiply or divide and say exit to get out.")
##    elif operation == "subtract":
##        print("Random subtraction question: 4 - 7 = ", i - j)
##        operation = input("What mathematical operation do you want to perform from addition, subtraction, multiplication or division. Say add, subtract, multiply or divide and say exit to get out.")
##    elif operation == "multiply":
##        print("Random multiplication question: 4 * 7 = ", i * j)
##        operation = input("What mathematical operation do you want to perform from addition, subtraction, multiplication or division. Say add, subtract, multiply or divide and say exit to get out.")
##    elif operation == "divide":
##        print("Random division question: 4 / 7 = ", i / j)
##        operation = input("What mathematical operation do you want to perform from addition, subtraction, multiplication or division. Say add, subtract, multiply or divide and say exit to get out.")
##    else:
##        print("Try using the sugested options:")
##        operation = input("What mathematical operation do you want to perform from addition, subtraction, multiplication or division. Say add, subtract, multiply or divide and say exit to get out.")
##
##
