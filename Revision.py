subject1 = float(input("What did you get in math?"))
subject2 = float(input("What did you get in english?"))
subject3 = float(input("What did you get in science? "))
subject4 = float(input("What did you get in history? "))
subject5 = float(input("What did you get in french? "))

avg = (subject1 + subject2 + subject3 +subject4 + subject5) / 5
print(avg)

if avg <= 100 and avg >= 80:
    print("A is great! Excellent!")
elif avg <=79 and avg >= 60:
    print("B is BOT. Just kidding. good job!")
elif avg <=59 and avg >= 50:
    print("Just off C. Nice try. Satisfactory")
elif avg <=49 and avg >= 35:
    print("Wow... Just wow. Need's Improvment badly")
elif avg<35 and avg >= 0:
    print("Boooooooo!!! FAIL")
else:
    print("Sorry! Your grade can't be in words, negative or over 100... Try again")
