# Dice simulation


import random   # To generate random numbers
while True:
    x = input("Want to roll the dice or quit?!!!Press 'R' for rolling and any other key for quitting")
    if x.lower() == 'r':
        y = random.randint(1, 6)
        print('Chosen number is', y)

    else:
        print("Quitting!!!")
        break
