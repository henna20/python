import random

i = random.randint(1, 13)
print("A random card:", i)
if i == 1:
    print("The corresponding card value is Ace")
elif i == 2:
    print("The corresponding card value is 2")
elif i == 3:
    print("The corresponding card value is 3")
elif i == 4:
    print("The corresponding card value is 4")
elif i == 5:
    print("The corresponding card value is 5")
elif i == 6:
    print("The corresponding card value is 6")
elif i == 7:
    print("The corresponding card value is 7")
elif i == 8:
    print("The corresponding card value is 8")
elif i == 9:
    print("The corresponding card value is 9")
elif i == 10:
    print("The corresponding card value is 10")
elif i == 11:
    print("The corresponding card value is Jack")
elif i == 12:
    print("The corresponding card value is Queen")
elif i == 13:
    print("The corresponding card value is King")
else:
    print("Invalid Number")
# =====================Part 2=============================


y = input("Guess the next card is higher or lower:")

j = random.randint(1, 13)
if j == 1:
    print("The next random card value is Ace")
elif j == 2:
    print("The next random card value is 2")
elif j == 3:
    print("The next random card value is 3")
elif j == 4:
    print("The next random card value is 4")
elif j == 5:
    print("The next random card value is 5")
elif j == 6:
    print("The next random card value is 6")
elif j == 7:
    print("The next random card value is 7")
elif j == 8:
    print("The next random card value is 8")
elif j == 9:
    print("The next random card value is 9")
elif j == 10:
    print("The next random card value is 10")
elif j == 11:
    print("The next random card value is Jack")
elif j == 12:
    print("The next random card value is Queen")
elif j == 13:
    print("The next random card value is King")
else:
    print("Invalid Number")


if y == "higher":
    if j > i:
        print("Congrats, You Win..!")
    else:
        print("Sorry, You Lose..!")
elif y == "lower":
    if j < i:
        print("Congrats, You Win..!")
    else:
        print("Sorry, You Lose..!")
else:
    print("Invalid String")
