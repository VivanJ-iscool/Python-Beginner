rating = float(input("What do you rate the movie Puss in Boots: The Last Wish from 1-10?"))

if rating <= 5 and rating >= 0:
    print("That is a very low rating, but that is your opinion, not mine")
elif rating > 5 and rating <= 7:
    print("That is an average rating which most people pick but it makes the most sence")
elif rating >= 8 and rating <= 10:
    print("This is an amazing rating and me personally, it is my rating for this movie to")
else:
    print("That is not a real rating and you must pick the ratings from 1-10")
