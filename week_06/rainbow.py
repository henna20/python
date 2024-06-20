while True:
    n = int(input("Enter a number from 0 to 7(-1 to quit):"))
    if n == -1:
        break
    else:
        this_tuple = ("Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet")
        n -= 1
        print(this_tuple[n])
