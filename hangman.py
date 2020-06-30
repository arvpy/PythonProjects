#  Hangman
import random

def get_word():
    words = ['top', 'tea', 'dine', 'fine', 'kite', 'coffee', 'ice', 'smile']
    return random.choice(words).lower()  # randomly chooses a word


def check(x, y, z):  # x= word, y= guess, z= guesses
    status = ''
    matches = 0
    for letter in x:
        if letter in z:
            status += letter

        else:
            status += '*'
        if y == letter:
            matches += 1
    if matches >= 1:
        print("There is a match!!!\n")
        print("Word contains {} match of {}".format(matches, y))
    return status


word = get_word()  # word to find
guesses = []  # Guessed words list
guessed = True  # Loop continues till right guess
print("Lets play Hangman!!!The word contains {} letters".format(len(word)))
while guessed:
    guess = input("Guess the {} letter word or a single letter".format(len(word)))  # input word or letter from user
    if guess == word:
        if len(guesses) + 1 == 1:
            print("Congrats!!Guessed right in {} try!!\n".format(len(guesses)+1))
            guessed = False
        else:
            print("Wow!!!That was awesome..You guessed it right in {} tries".format(len(guesses)+1))
            guessed = True
            break

    if guess in guesses:
        print("Already tried guessing", guess)
    else:
        guess = guess.lower()
        guesses.append(guess)
        # pdb.set_trace()
        result = check(word, guess, guesses)
        print("Your Word -->", result)
        if result == word:
            if len(guesses)+1 == 1:
                print("Congrats!!Guessed right in {} try!!\n".format(len(guesses)+1))
                guessed = False
            else:
                print("Congrats!!Guessed right in {} tries!!\n".format(len(guesses)+1))
                guessed = False
        else:
            print("Keep trying\n\n")
