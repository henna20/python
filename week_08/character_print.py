def character_print(integer, character):
    n = integer
    x = character
    i = 1
    while i <= n:
        print(x)
        i += 1


n = int(input("enter a number:"))
x = input("enter a character:")
character_print(n, x)
