while True:
    n = int(input("Enter a number from 0 to 7(-1 to quit):"))
    if n == -1:
        print("Not a permitted Number")
        break
    elif (n <= 0) or (n >= 8):
        print("Not a permitted Number")

    else:
        this_tuple = ("One for sorrow", "Two for joy", "Three for a girl", "Four for a boy", "Five for silver", "Six for gold", "Seven for a secret never to be told")
        n -= 1
        print(this_tuple[n])
