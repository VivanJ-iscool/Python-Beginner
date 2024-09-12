print("Welcome to my super hard MATH QUIZ!")
print("Get 4 points to be a Rookie, 6 points to be a Big Brain Beginner, 8 points to be a Super Scientist, and 10 or more to be Mathematical Magician!")
print("Answer the questions right to gain points. Get one wrong and you lose points. You start with 5 points!")
points = 5
answer1 = int(input("What is 5 * 3 + 1 : "))
if answer1 == 16:
    points_after_1_right = points + 2
    print("CORRECT! Score: ", points_after_1_right)
else:
    points_after_1_right = points - 2
    print("INCORRECT! The answer was 16. Score: ", points_after_1_right)


answer2 = int(input("What is (3 + 1) * 2 + 1 : "))
if answer2 == 9:
    points_after_2_right = points_after_1_right + 2
    print("CORRECT! Score: ", points_after_2_right)
else:
    points_after_2_right = points_after_1_right - 2
    print("INCORRECT! The answer was 9. Score: ", points_after_2_right)


answer3 = int(input("What is 3 * 5 * 2 : "))
if answer3 == 30:
    points_after_3_right = points_after_2_right + 2
    print("CORRECT! Score: ", points_after_3_right)
else:
    points_after_3_right =  points_after_2_right - 2
    print("INCORRECT! The answer was 30. Score: ", points_after_3_right)

answer4 = int(input("What is 11 - 5 * 2 + 2 : "))
if answer4 == 3:
    points_after_4_right = points_after_3_right + 2
    print("CORRECT! Score: ", points_after_4_right)
else:
    points_after_4_right = points_after_3_right - 2
    print("INCORRECT! The answer was 3. Score: ", points_after_4_right)

answer5 = int(input("What is 100 * 101 : "))
if answer5 == 10100:
    points_after_5_right = points_after_4_right + 2
    print("CORRECT! Score: ", points_after_5_right)
else:
    points_after_5_right = points_after_4_right - 2
    print("INCORRECT! The answer was 10100. Score: ", points_after_5_right)

final_score = points_after_5_right
print("END OF TEST! Let's see your score!")
if final_score < 4:
    print("Score: ", final_score, "Try the test again!")
elif final_score > 4 and final_score<= 6:
    print("You have a score of 5 or 6! Rookie Score!")
elif final_score > 6 and final_score <= 8:
    print(" A score of 7 or 8! That makes you a Big Brain Beginner!")
elif final_score > 8 and final_score <= 10:
    print("WOAH! A score of 8-10 makes you a Super Scientist!")
elif final_score > 10:
    print("More than 10 points! We have a Mathematical Magician over here!")
