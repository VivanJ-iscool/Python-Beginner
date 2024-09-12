#STUDENT VERSION

# Here are all your hangman drawings
hangman0 = '''
  +---+
  |   |
      |
      |
      |
      |
========='''

hangman1 = '''
  +---+
  |   |
  O |
      |
      |
      |
========='''
hangman2 = '''
  +---+
  |   |
  O |
  |   |
      |
      |
========='''
hangman3 = '''
  +---+
  |   |
  O |
 /|   |
      |
      |
========='''
hangman4 = '''
  +---+
  |   |
  O |
 /|\  |
      |
      |
========='''
hangman5 = '''
  +---+
  |   |
 O  |
 /|\  |
 /    |
      |
========='''
hangman6 = '''
  +---+
  |   |
 O  |
 /|\  |
 / \  |
      |
========='''

# S1 - ask for user's name and word to guess
player1_name = input("PLAYER 1: What is your name?")
player2_name = input("PLAYER 2: What is your name?")
full_answer= input("PLAYER 1: What is your word or phrase?")
full_answer=full_answer.lower()
# S2 - initialize important variables
wrong_letters = ""
right_letters = ""
lives = 6

while lives > 0:
    # S3
    for i in full_answer:
        if i in right_letters:
            print(i, end =" ")
        else:
            print("_", end =" ")
    print()
    # S4 
    if lives == 6:
        print(hangman0)
    elif lives == 5:
        print(hangman1)
    elif lives == 4:
        print(hangman2)
    elif lives == 3:
        print(hangman3)
    elif lives == 2:
        print(hangman4)
    elif lives == 1:
        print(hangman5)
    elif lives == 0:
        print(hangman6)
    # S5
    guessed_letter = input("What is your guess of Player One's word(letters or entire word)?")
    guessed_letter=guessed_letter.lower()
    #S6
    if guessed_letter in full_answer:
        if guessed_letter in right_letters:
            print('you already guessed it. TRY AGAIN')
        right_letters += guessed_letter
    elif guessed_letter in wrong_letters:
            print('you already guessed it. TRY AGAIN')
    elif guessed_letter not in full_answer:
        wrong_letters += guessed_letter
        lives = lives - 1
        print('\nWrong Guess. Lost a life. Try Again! ')
    #S8
        if lives == 0 or guessed_letter == full_answer:
            break
        
# S9, S10 and S11
if guessed_letter == full_answer:
    print("Congratulations", player2_name, "! YOU WIN HANGMAN")
elif lives == 0:
    print("Good try", player2_name, "but you lost. Maybe you will win next time. Congrats to", player1_name, "for winning!\nThe answer was:", full_answer)

